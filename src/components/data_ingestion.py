import os
import sys
#E:\workspace\projects\mlproject\src\exception
#from exception import CustomException
#from logger import logging
#from src import exception
#from src import logger
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components import data_transformation
from src.components.data_transformation import DataTransformationConfig
from src.components import model_trainer
#from src.components.model_trainer import ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        #logger.logging.info("Entered the initiate_data_ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            #logging.info("data has been read as a Data Frame sucessfully")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            #logging.info("Train Test Split Initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            #logging.info("Data Ingestion has been completed successfully.")

            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path)
        except Exception as e:
            #raise CustomException(e,sys)
            print(e)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=data_transformation.DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=model_trainer.ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
