import os
import yaml
from src.ds_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            print(yaml_file)
            content = yaml.safe_load(yaml_file)
            print(content)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_of_directories: list,verbose=True):
    for path in path_of_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

    logger.info(f"jason file saved at: {path}")


@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:any, path:Path):
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path):
    data=joblib.load(path)
    logger.info(f"Binary file loaded fro :{path}")
    return data