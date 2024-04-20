from src.emotion.config.configuration import ConfigurationManager
from src.emotion.entity.config_entity import ModelTrainerConfig
from src.emotion import logging, ModelException
import pandas as pd
from sklearn.model_selection import train_test_split
#from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle, sys, os
from src.emotion.ml.model import ModelArchitecture
from keras.utils import pad_sequences


class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        try:
            self.config = config 
        except Exception as e:
            raise ModelException(e,sys)
        
    def train_test_data(self):
        try:
            data_path = self.config.data_path
            data = pd.read_csv(data_path)
            data.dropna(inplace=True)
            data.drop_duplicates(inplace=True)
            X = data['text']
            y = data['label']
            X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.1, random_state=42)
            return X_train,X_test,y_train,y_test
        except Exception as e:
            raise ModelException(e,sys)
        
    def tokenizing(self,X_train):
        try:
            tokenizer = Tokenizer(num_words=60000)
            tokenizer.fit_on_texts(X_train)
            sequences = tokenizer.texts_to_sequences(X_train)
            sequences_matrix = pad_sequences(sequences,maxlen=300)
            return sequences_matrix,tokenizer
        except Exception as e:
            raise ModelException(e,sys)
        
    def model_trainer(self):
        try:
            X_train,X_test,y_train,y_test = self.train_test_data()
            model_architecture = ModelArchitecture()   

            model = model_architecture.get_model()
            
            sequences_matrix,tokenizer =self.tokenizing(X_train)
            
            model.fit(sequences_matrix, y_train, 
                        batch_size=200, 
                        epochs = 5, 
                        validation_split=0.1, 
                        )
            model.save(self.config.model_path)
            #os.makedirs(self.config.tokenizer_path)
            with open(self.config.tokenizer_path, 'wb') as handle:
                pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
            #os.makedirs(self.config.model_path,exist_ok=True)
            #model.save(self.config.model_path)
        except Exception as e:
            raise ModelException(e,sys)