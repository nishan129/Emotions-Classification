import os
from kaggle.api.kaggle_api_extended import KaggleApi
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.entity.config_entity import DataIngestionConfig
from src.emotion import ModelException,logging
import sys


class DataIngenstion:
    def __init__(self,config:DataIngestionConfig):
        try:
            self.config = config
        except Exception as e:
            raise ModelException(e,sys)
        
    def download_kaggle_data(self,username, api_key, dataset_name):
        """
        Download a dataset from Kaggle.

        Parameters:
        - username: Your Kaggle username.
        - api_key: Your Kaggle API key.
        - dataset_name: The name of the dataset in the format 'owner/dataset'.
        - destination: The directory where you want to save the downloaded files (default is current directory).
        """
        # Set Kaggle API credentials
        os.environ["KAGGLE_USERNAME"] = username
        os.environ["KAGGLE_KEY"] = api_key
        destination = self.config.root_dir
        # Authenticate with Kaggle API
        api = KaggleApi()
        api.authenticate()

        try:
            # Download dataset files
            api.dataset_download_files(dataset_name, path=destination, unzip=True)
            logging.info("Dataset downloaded successfully!")
        except Exception as e:
            logging.info(f"Error downloading dataset: {str(e)}")
            raise ModelException(e,sys)

    # Example usage:
    # Replace 'your_username', 'your_api_key', and 'dataset-owner/dataset-name' with your own values
    # download_kaggle_data('your_username', 'your_api_key', 'dataset-owner/dataset-name', destination='./')
