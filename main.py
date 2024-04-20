from src.emotion.components.data_ingestion import DataIngenstion
from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.constant import *
from src.emotion.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.emotion.pipeline.model_trainer_pipeline import ModelTrainerPipeline
import sys
import tensorflow as tf


STAGE_NAME   = "Model Evaluation"

if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        #model = tf.keras.models.load_model("artifacts/model_trainer/model/model.h5")
        aa = ModelTrainerPipeline()
        aa.main()
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(f">>>>>>> Stage {STAGE_NAME} Completed  <<<<<<<<")
    except Exception as e:
        raise ModelException(e,sys)