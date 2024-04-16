from src.emotion.components.data_ingestion import DataIngenstion
from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.constant import *
import sys

STAGE_NAME   = "Data Ingestion"

class DataIngenstionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:  
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngenstion(config=data_ingestion_config)
            data_ingestion.download_kaggle_data(username=USER_NAME,api_key=API_KEY,dataset_name=DATASET_NAME)

        except Exception as e:
            raise ModelException(e,sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        obj = DataIngenstionPipeline()
        obj.main()
        logging.info(f">>>>>>> Stage {STAGE_NAME} Completed  <<<<<<<<")
    except Exception as e:
        raise ModelException(e,sys)