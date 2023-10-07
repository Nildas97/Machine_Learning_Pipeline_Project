# importing libraries
import os
import sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
# creating data_ingestion_config class
class DataIngestionConfig:
    # creating data path for raw, train and test data
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "raw.csv")
# defining data_ingestion


class DataIngestion:
    # defining constructor
    def __init__(self):
        logging.info("******DATA_INGESTION******")
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            # read data
            logging.info("Reading the data from local system")
            data = pd.read_csv(os.path.join(
                "D:/Data Science/Python_Projects/ml_pipeline_project/Machine_Learning_Pipeline_Project/notebook/data", "income_cleandata.csv"))
            logging.info("Reading data completed")

            # creating artifact folder
            os.makedirs(os.path.dirname(
                self.ingestion_config.raw_data_path), exist_ok=True)

            # saving the raw data
            data.to_csv(self.ingestion_config.raw_data_path, index=False)

            # splitting the raw data
            logging.info("Splitting the data into train and test")
            train_set, test_set = train_test_split(
                data, train_size=.70, test_size=.30, random_state=42)

            # saving the train data
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True)

            # saving the test data
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)
            logging.info("Data ingestion completed")

            # return
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("Error occurred in data ingestion stage")
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
