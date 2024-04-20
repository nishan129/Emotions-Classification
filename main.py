from src.emotion.components.data_ingestion import DataIngenstion
from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.constant import *
from src.emotion.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.emotion.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.emotion.pipeline.training_pipeline import TrainingPipeline
import sys
import tensorflow as tf
import numpy as np
import pandas as pd


STAGE_NAME   = "Model Prediction"

if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logging.info(f">>>>>>> Stage {STAGE_NAME} Completed  <<<<<<<<")
    except Exception as e:
        raise ModelException(e,sys)