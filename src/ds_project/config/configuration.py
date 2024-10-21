from src.ds_project.constants import *
from src.ds_project.utils.common import read_yaml, create_directories
from src.ds_project.entity.entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        print(self.config.artifacts_root)

        create_directories(self.config.artifacts_root)

    def get_data_ingestion_path(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories(config.root_dir)

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

