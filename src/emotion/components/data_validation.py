from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.entity.config_entity import DataValidationConfig
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        try:
            self.config = config
        except Exception as e:
            raise ModelException(e,sys)

    def split_data(self):
        try:
            data = pd.read_csv(self.config.data_path)
            data.drop(columns='Unnamed: 0', inplace=True)
            X_train, X_test = train_test_split(data,test_size=0.1, random_state=42)
            X_train.to_csv(self.config.train_data_dir)
            X_test.to_csv(self.config.test_data_dir)
        except Exception as e:
            raise ModelException(e,sys)