from src.emotion.entity.config_entity import DataIngestionConfig
from src.emotion import logging, ModelException
from src.emotion.utils.common import read_yaml, create_directory
from pathlib import Path
from src.emotion.constant import *
import sys
class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        try:
            
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            
            create_directory([self.config.artifacts_root])
        except Exception as e:
            raise ModelException(e,sys)
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_dir = self.config.data_ingestion
            create_directory([data_dir.root_dir])
            data_ingenstion_config = DataIngestionConfig(
                root_dir=data_dir.root_dir
            )
            return data_ingenstion_config
        except Exception as e:
            raise ModelException(e,sys)