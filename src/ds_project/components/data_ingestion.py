import os
import urllib.request as request
from src.ds_project import logger
import zipfile
import requests

from src.ds_project.entity.entity import (DataIngestionConfig)

## Components

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    ## Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):  # Check if the file already exists
            try:
                # Send an HTTP GET request to download the file
                response = requests.get(self.config.source_URL)
                
                # Check if the request was successful
                if response.status_code == 200:
                    # Write the content to the local file
                    with open(self.config.local_data_file, 'wb') as file:
                        file.write(response.content)
                    logger.info(f"{self.config.local_data_file} downloaded successfully.")
                else:
                    logger.error(f"Failed to download the file. Status code: {response.status_code}")
            except Exception as e:
                logger.error(f"An error occurred while downloading the file: {e}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists. Skipping download.")
    ## extract the zip file
    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

            