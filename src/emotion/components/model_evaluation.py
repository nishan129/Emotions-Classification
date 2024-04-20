
from src.emotion.entity.config_entity import ModelEvaluationConfig
from src.emotion import logging, ModelException
import pandas as pd
from tensorflow.keras.models import load_model
import pickle, sys, os
from keras.utils import pad_sequences
from src.emotion.utils.common import save_json, load_object
import tensorflow as tf
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        try:
            self.config = config
        except Exception as e:
            raise ModelException(e,sys)
        
    def evaluation_data(self):
        try:
            data_path = self.config.data_path
            data = pd.read_csv(data_path)
            data.dropna(inplace=True)
            data.drop_duplicates(inplace=True)
            X = data['text']
            y = data['label']
            return X, y
        except Exception as e:
            raise ModelException(e,sys)
        
    def tokeinzer_model_load(self):
        try:
            tokenizer_path = self.config.tokenizer_path
            tokenizer = load_object(file_path=tokenizer_path)
            model_path = self.config.model_path
            model = load_model(model_path)
            
            return tokenizer, model
        except Exception as e:
            raise ModelException(e,sys)
        
    def model_evaluation(self, model, tokenizer, X, y):
        try:
            tokenizer = tokenizer
            sequences = tokenizer.texts_to_sequences(X)
            x = pad_sequences(sequences=sequences,maxlen=300)
            model = model
            model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
            loss, accuracy = model.evaluate(x, y)
            #loss, accuracy = 0.2, 0.3
            print(f"loss : {loss}, accuracy : {accuracy}")
            metrix = {"loss": loss, "accuracy": accuracy}
            
            save_json(file_path=Path(self.config.matrix_path),data=metrix)
            model.save(self.config.mode_evaluation_path)
        except Exception as e:
            raise ModelException(e,sys)
        
    def initatiate_evaluation(self):
        try:
            logging.info("Enter Model evaluation")
            X, y = self.evaluation_data()
            tokenizer, model = self.tokeinzer_model_load()
            self.model_evaluation(model=model,tokenizer=tokenizer,X=X, y=y)
            logging.info("Model Evaluation Successfully")
        except Exception as e:
            raise ModelException(e,sys)