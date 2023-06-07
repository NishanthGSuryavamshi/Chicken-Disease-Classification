import os
from box.exceptions import BoxValueError
import yaml
from src.cnnclassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """Reads yaml file and returns in terms of coonfigbox type
    args:
    path_yaml(str): path to yaml file

    Raises:
    BoxValueError: if yaml file is not valid
    e: empty file

    returns:
    configbox:Configbox type

    """
    try:
        with open(path_to_yaml) as yaml_file:
            data = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e