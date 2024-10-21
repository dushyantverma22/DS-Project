import os
import urllib.request as request
from src.ds_project import logger
import zipfile
import requests
import pandas as pd

from src.ds_project.entity.entity import (DataValidationConfig)

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config=config

    def Validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_col = list(data.columns)
            all_schema = self.config.all_schema.keys()
            print(all_col)
            print(all_schema)
    
            for col in all_col:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation failed: Column not found in schema: {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation passed: Column found in schema: {validation_status}")

            return validation_status
        except Exception as e:
            raise e

