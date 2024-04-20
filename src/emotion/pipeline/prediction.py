
from src.emotion import logging, ModelException
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.constant import *
from src.emotion.entity.config_entity import PredictionConfig
from tensorflow.keras.models import load_model
from keras.utils import pad_sequences
from src.emotion.utils.common import save_json, load_object
from src.emotion.components.data_transformation import DataTransformation
from src.emotion.entity.config_entity import DataTransformationConfig
import sys
import numpy as np
import pandas as pd

STAGE_NAME   = "Model Prediction"


class PredictionPipeline:
    def __init__(self,config:PredictionConfig):
        self.config = config
        self.data_transform = DataTransformation(config=DataTransformationConfig)
    def predict(self, text:str):
        try:
            
            text = {"text":text, "index": 0}
            text = pd.DataFrame(text, index=[0])
            
            text['text'] = self.data_transform.data_cleaning(words=text['text'])
            model = load_model(self.config.model_path)
            tokenizer = load_object(self.config.tokenizer_path)
            
            token = tokenizer.texts_to_sequences(text["text"])
            data = pad_sequences(token, maxlen=300)
            pred = model.predict(data)
            
            predict = np.argmax(pred , axis=1)
            prediction = "Sadness"
            if predict == 1:
                prediction = "Joy"
            elif predict == 2:
                prediction = "Love"
            elif predict == 3:
                prediction = "Anger"
            elif predict == 4:
                prediction = "Fear"
            elif predict == 5:
                prediction = "Surprise"
            else:
                prediction
            return prediction
        except Exception as e:
            raise ModelException(e,sys)
        
    

