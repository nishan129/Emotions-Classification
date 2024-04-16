from src.emotion.components.data_validation import DataValidation
from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.constant import *
import sys


STAGE_NAME   = "Data Validation"
class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.split_data()
        except Exception as e:
            raise ModelException(e,sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logging.info(f">>>>>>> Stage {STAGE_NAME} Completed  <<<<<<<<")
    except Exception as e:
        raise ModelException(e,sys)