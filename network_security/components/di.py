from network_security.exceptions.exceptions import CustomException
import sys
from network_security.logging.logging import logging 
from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.artifacts_entity import ArtifactsEntity
import os 
import pymongo
 
import pandas as pd
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
load_dotenv()
uri = os.getenv('uri')
class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)
    def Export_collect(self):
        try:
            db_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(uri)
            collection = self.mongo_client[db_name][collection_name]
            data = list(collection.find())
            df = pd.DataFrame(data)
            print("Documents found:", collection.count_documents({}))

            if "_id" in df:
                df.drop("_id", axis=1, inplace=True)
            return df
        except Exception as e:
            raise CustomException(e,sys)
    def export_data(self,df:pd.DataFrame):
        try:
            feature_store_path= self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_path)
            os.makedirs(dir_path,exist_ok=True)
            df.to_csv(feature_store_path,index=False)
            return df
        except Exception as e:
            raise CustomException(e,sys)
    def split_data(self,df:pd.DataFrame):
        try:
            train_set,test_set= train_test_split(df,test_size=0.2,random_state=42)
            train_file_path=self.data_ingestion_config.train_file_path
            test_file_path=self.data_ingestion_config.test_file_path
            dir_path=os.path.dirname(train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            train_set.to_csv(train_file_path,index=False)
            test_set.to_csv(test_file_path,index=False)
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_ingestion(self):
        try:
            df = self.Export_collect()
            df = self.export_data(df)
            self.split_data(df)
            logging.info('Data Ingestion Completed')
            return ArtifactsEntity.Artifact(
                trained_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)

            