from src.emotion.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from src.emotion import logging, ModelException
from src.emotion.utils.common import read_yaml, create_directory
from pathlib import Path
from src.emotion.constant import *
import sys
class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        try:
            
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            self.schema = read_yaml(schema_filepath)
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
        
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            data_dir = self.config.data_validation
            schema = self.schema.COLUMNS
            create_directory([data_dir.root_dir])
            data_validation_config = DataValidationConfig(
                root_dir= data_dir.root_dir,
                data_path=data_dir.data_path,
                STATUS_FILE= data_dir.STATUS_FILE,
                all_schema=schema
            )
            return data_validation_config
        except Exception as e:
            raise ModelException(e,sys)
        
    def get_data_transformation_config(self) -> DataTransformationConfig :
        try:
            data_dir = self.config.data_transformation
            create_directory([data_dir.root_dir])
            data_transformation_config = DataTransformationConfig(
                root_dir= data_dir.root_dir,
                data_path= data_dir.data_path,
                transform_data_path=data_dir.transform_data_path,
            )
        
            return data_transformation_config
        except Exception as e:
            raise ModelException(e,sys)
        
        
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            data_dir = self.config.model_trainer
            create_directory([data_dir.root_dir,data_dir.model])
            model_trainer_config = ModelTrainerConfig(
                root_dir=data_dir.root_dir,
                data_path=data_dir.data_path,
                model = data_dir.model,
                tokenizer_path=data_dir.tokenizer_path,
                model_path=data_dir.model_path,
            )
            
            return model_trainer_config
        except Exception as e:
            raise ModelException(e,sys)