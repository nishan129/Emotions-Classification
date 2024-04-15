import os
import yaml
import json
import sys
from pathlib import Path
from src.emotion import ModelException, logging
from ensure import ensure_annotations
from box import ConfigBox



@ensure_annotations
def read_yaml(file_path:Path) -> ConfigBox:
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            return ConfigBox(data)
    except Exception as e:
        raise ModelException(e,sys)
    


@ensure_annotations    
def save_json(file_path:Path, data) -> ConfigBox:
    try:
        with open(file_path, 'w') as f:
            json.dump(data,f, indent= 4)
    except Exception as e:
        raise ModelException(e,sys)
   
      
   
@ensure_annotations   
def create_directory(path_directory:list, verbose=True) :
    try:
        for path in path_directory:
            os.makedirs(path,exist_ok=True)
            if verbose:
                logging.info(f"Create directory as {path}")
    except Exception as e:
        raise ModelException(e,sys)