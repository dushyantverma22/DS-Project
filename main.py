from src.ds_project import logger
from src.ds_project.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.ds_project.pipeline.data_validation import DataValidationTrainingPipeline
from src.ds_project.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.ds_project.pipeline.model_trainer_pip import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_tansformation = DataTransformationTrainingPipeline()
    data_tansformation.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

