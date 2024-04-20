from src.emotion.components.data_ingestion import DataIngenstion
from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.constant import *
from src.emotion.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.emotion.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.emotion.pipeline.prediction import PredictionPipeline
import sys
import tensorflow as tf
import numpy as np
import pandas as pd


STAGE_NAME   = "Model Prediction"

if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        #model = tf.keras.models.load_model("artifacts/model_trainer/model/model.h5")
        # aa = ModelTrainerPipeline()
        # aa.main()
        # obj = ModelEvaluationPipeline()
        # obj.main()
        config = ConfigurationManager()
        pre_config = config.get_prediction_config()
        predict = PredictionPipeline(config=pre_config)
        text = {"text":"feel realli helpless heavi heart", "index": 0}
        data = pd.DataFrame(text, index=[0])
        pred = predict.predict(text=data['text'])
        
        print(pred)
        logging.info(f">>>>>>> Stage {STAGE_NAME} {pred}Completed  <<<<<<<<")
    except Exception as e:
        raise ModelException(e,sys)