from src.emotion.components.data_ingestion import DataIngenstion
from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.constant import *
from src.emotion.pipeline.data_transformation_pipeline import DataTransformationPipeline
import sys



STAGE_NAME   = "Data Transformation"

if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logging.info(f">>>>>>> Stage {STAGE_NAME} Completed  <<<<<<<<")
    except Exception as e:
        raise ModelException(e,sys)