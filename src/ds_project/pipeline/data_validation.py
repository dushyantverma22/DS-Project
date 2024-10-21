from src.ds_project.config.configuration import ConfigurationManager
from src.ds_project.components.data_validation import DataValidation
from src.ds_project import logger


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
            config=ConfigurationManager()
            data_validation_config = config.get_data_validation()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.Validate_all_columns()
            #data_ingestion.extract_zip()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
         

