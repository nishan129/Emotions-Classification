from src.emotion.components.data_ingestion import DataIngenstion
from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.constant import *
from src.emotion.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.emotion.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.emotion.pipeline.data_ingestion_pipeline import DataIngenstionPipeline
from src.emotion.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.emotion.pipeline.data_validation_pipeline import DataValidationPipeline
from src.emotion.pipeline.prediction import PredictionPipeline
import sys
import tensorflow as tf
import numpy as np
import pandas as pd

class TrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        logging.info(f"Data Ingenstion Started")
        dataingenstion = DataIngenstionPipeline()
        dataingenstion.main()
        logging.info(f"Data Ingenstion End")
        logging.info(f"Data Validation Started")
        datavalidation = DataValidationPipeline()
        datavalidation.main()
        logging.info(f"Data Validation End")
        logging.info(f"Data Transformation Started")
        datatransformation = DataTransformationPipeline()
        datatransformation.main()
        logging.info(f"Data Transformation Started")
        logging.info(f"Model Training Started")
        model_trainer = ModelTrainerPipeline()
        model_trainer.main()
        logging.info(f"Model Training End")
        logging.info(f"Model Evaluation Started")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.main()
        logging.info(f"Model Evaluation End")
        