import os
import urllib.request as request
from src.ds_project import logger
import zipfile
import requests
import pandas as pd
from sklearn.model_selection import train_test_split

from src.ds_project.entity.entity import (DataTransformationConfig)

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config

        ### Add any techniques here

    def data_tansformation_pro(self):
        try:
            data = pd.read_csv(self.config.data_path)

            train, test = train_test_split(data)
            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
            
            logger.info("splliting data into train test split")
            logger.info(train.shape)
            logger.info(test.shape)

            print(train.shape)
            print(test.shape)
        except Exception as e:
            raise e