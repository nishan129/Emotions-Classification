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
            self.X_train, self.X_test = train_test_split(data,test_size=0.1, random_state=42)
        except Exception as e:
            raise ModelException(e,sys)
        
    def validate_all_columns(self) -> bool:
        try:
            train_validation_status = None
            
            train = self.X_train
            test = self.X_test
            all_coll = list(train.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_coll:
                if col not in all_schema:
                    train_validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Train Data Validation status is {train_validation_status}")
                else:
                    train_validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Train Data Validation status is {train_validation_status} \n")
                        logging.info(f"Train Data Validation status is {train_validation_status}")
                        
            test_validation_status = None
            all_coll = list(test.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_coll:
                if col not in all_schema:
                    test_validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Test Data Validation status is {test_validation_status}")
                else:
                    test_validation_status = True
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"Test Data Validation status is {test_validation_status}\n")
                        f.close()
                        logging.info(f"Test Data Validation status is {test_validation_status}")
        except Exception as e:
            raise ModelException(e,sys)