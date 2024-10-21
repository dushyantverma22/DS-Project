from src.ds_project.config.configuration import ConfigurationManager
from src.ds_project.components.model_evaluation import ModelEvaluation
from src.ds_project import logger
from pathlib import Path


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            config=ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        Model_evaluation = ModelEvaluationPipeline()
        Model_evaluation.initiate_model_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
         

