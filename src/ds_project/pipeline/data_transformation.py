from src.ds_project.config.configuration import ConfigurationManager
from src.ds_project.components.data_transformation import DataTransformation
from src.ds_project import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            #with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
             #   status=f.read().split(" ")[-1]

            status = "True"

            if status=="True":
                config=ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.data_tansformation_pro()
            else:
                raise Exception("Your data scheme is not valid")
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_tansformation = DataTransformationTrainingPipeline()
        data_tansformation.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
         

