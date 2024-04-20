from src.emotion import logging, ModelException
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM,Activation,Dense,Dropout,Input,Embedding,SpatialDropout1D, Bidirectional,BatchNormalization, Flatten, GRU
from keras import layers
from tensorflow.keras.layers import *

class ModelArchitecture:
    def __init__(self):
        pass
    
    def get_model(self):
        model = Sequential()
        #model.add(Embedding(50000,100, input_length=300))
        model.add(Embedding(input_dim=60000, output_dim=100,input_shape=(79,)))
        #model.add(Bidirectional(LSTM(128,  activation='tanh')))
        # model.add(LSTM(128, activation='tanh'))
        model.add(GRU(128))
        model.add(Dropout(0.5))
        model.add(BatchNormalization())
        model.add(Flatten())
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(6, activation='softmax'))
        # model.add(layers.Dropout(0.5))
        # model.add(layers.Conv1D(128, 7, padding="valid", activation="relu", strides=3))
        # model.add(layers.Conv1D(128, 7, padding="valid", activation="relu", strides=3))
        # model.add(layers.GlobalMaxPooling1D())
        # model.add(layers.Dense(128, activation="relu"))
        # model.add(layers.Dropout(0.5))
        
        # model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
        # model.add(Dense(6, activation='softmax'))
        model.summary()
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        
        return model