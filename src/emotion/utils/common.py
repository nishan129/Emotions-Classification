import os
import yaml
import json
import sys
from pathlib import Path
from src.emotion import ModelException, logging
from ensure import ensure_annotations
from box import ConfigBox
import pickle
import h5py
from keras.models import model_from_json
import tensorflow as tf



@ensure_annotations
def read_yaml(file_path:Path) -> ConfigBox:
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            return ConfigBox(data)
    except Exception as e:
        raise ModelException(e,sys)
    


@ensure_annotations    
def save_json(file_path:Path, data) :
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
    
    
def load_object(file_path:str) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file path{file_path} is not exists")
        with open(file_path,'rb') as file:
            return pickle.load(file)
    except Exception as e:
        raise ModelException(e,sys)
    
def load_model(file_path:str) :
    try:
        model = tf.keras.models.load_model(file_path)
        model 
    except Exception as e:
        raise ModelException(e,sys)