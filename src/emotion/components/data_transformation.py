from src.emotion import logging, ModelException
from sklearn.model_selection import train_test_split
from src.emotion.entity.config_entity import DataTransformationConfig
import nltk
import pandas as pd
import re, os, sys
from pathlib import Path
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


try:
    nltk.download('stopwords')
    nltk.download('punkt')
except Exception as e:
    raise ModelException(e,sys)



class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        try:
            self.config = config
        except Exception as e:
            raise ModelException(e,sys)
        
    def load_data(self):
        try:
            data = pd.read_csv(self.config.data_path)
            data.drop(columns="Unnamed: 0", inplace=True)
            return data
        except Exception as e:
            raise ModelException(e,sys)
        
    @staticmethod
    def data_cleaning(words):
        try:
            stemmer = PorterStemmer()
            stopword = set(stopwords.words('english'))
            words = str(words).lower()
            words = re.sub(r'http\S+', '', words)
            words = re.sub(r'www\.\S+', '', words)
            words = re.sub(r'[^\w\s]', '', words)
            words = re.sub('\w*\d\w*', '', words)
            tokens = word_tokenize(words)
            # Remove stopwords and stem tokens
            cleaned_tokens = [stemmer.stem(token) for token in tokens if token not in stopword]
            # Join the tokens back into a single string
            cleaned_text = ' '.join(cleaned_tokens)
            return cleaned_text
        except Exception as e:
            raise ModelException(e,sys)
        
    def initiate_data_transformation(self) :
        try:
            logging.info("Entering data transformation function")
            data = self.load_data()
            data['text']=data['text'].apply(self.data_cleaning)
            data.to_csv(self.config.transform_data_path)
            logging.info("Data transformation is done")
        except Exception as e:
            raise ModelException(e,sys)