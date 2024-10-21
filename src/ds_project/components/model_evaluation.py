import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path
from src.ds_project.utils.common import save_json

from src.ds_project.entity.entity import (ModelEvaluationConfig)

#os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/dushyantverma414/DS-Project.mlflow"
#os.environ["MLFLOW_TRACKING_USERNAME"]="dushyantverma414"
#os.environ["MLFLOW_TRACKING_PASSWORD"]="25dab9c8e5112fc3db379fd131b2ba826a9fcb5f"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config=config

        ### Add any techniques here

    def eval_metrics(self, actual, pred):
        rmse=np.sqrt(mean_squared_error(actual, pred))
        mse=mean_absolute_error(actual, pred)
        r2=r2_score(actual, pred)
        return rmse, mse, r2
    
    def log_into_mlflow(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop([self.config.target_column], axis=1)
        test_y=test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            ## saving metrics a slocal
            scores = {"rmse":rmse, "mae":mae, "r2":r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            ## model registry does not work with file store
            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.save_model(model, "model")

      