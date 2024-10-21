from src.ds_project.config.configuration import ConfigurationManager
from src.ds_project.components.data_ingestion import DataIngestion
from src.ds_project import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
            config=ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_path()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            #data_ingestion.extract_zip()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
         

