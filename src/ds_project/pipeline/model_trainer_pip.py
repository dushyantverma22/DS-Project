from src.ds_project.config.configuration import ConfigurationManager
from src.ds_project.components.model_trainer import ModelTrainer
from src.ds_project import logger
from pathlib import Path


STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        try:
            config=ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        Model_trainer = ModelTrainingPipeline()
        Model_trainer.initiate_model_training()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
         

