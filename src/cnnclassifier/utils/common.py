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
    

@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """Create list of directories
    args: path_to_directories,
    ignore_log(bool,optional): ignore if multuple files to created defaults to False

    
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory:{directory}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """Save JSON
    args: path, data
    
    """
    with open(path,'w') as f:
        json.dump(data,f)

    logger.info(f"created JSON: {Path}")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """Load JSON
    args: path
    
    """
    with open(path,'r') as f:
        data = json.load(f)
    logger.info("json file loaded from:{path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data:any,path:Path):
    """
    save binary file
    args: data, path
   
    
    """
    data=joblib.dump(value=data,filename=path)
    logger.info("nimary file saved to:{path}")

@ensure_annotations
def load_bin(path:Path)->Any:
    """
    loads the binary file
    args: path
    returns:
    Any: Any object
    """
    data=joblib.load(path)
    logger.info("binary file loaded from:{path}")
    return data

def get_size(path:Path)->str:
    """
    gets the size of the file
    args: path
    returns:
    str: size of the file
    """
    size_in_kb=round(joblib.get_size(path)/1024)
    return f"~{size_in_kb}KB"
    
def decode_image(imgstring, filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()
        logger.info(f"image saved to:{filename}")

def encode_image_into_base64(cropped_image_path):
    with open(cropped_image_path ,'rb') as f:
        imgdata=f.read()
        imgstring=base64.b64encode(imgdata)

       