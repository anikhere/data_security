from network_security.exceptions.exceptions import CustomException
import sys
from data_schema import schema
from network_security.logging.logging import logging
from network_security.entity.config_entity import DataValidation, TrainingPipelineConfig
from network_security.entity.artifacts_entity import Artifact, DataValidationArtifact
from network_security.constants.train_pipe import SCHEMA_FILE_PATH
from scipy.stats import ks_2samp
import os
import pandas as pd
from network_security.utlis.main_utils.utils import read_yaml_file,write_yaml_file

class DataValidate:
    def __init__(self,data_ingestion_artifact:Artifact,
                 data_validation_config:DataValidation):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def read_csv(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CustomException(e, sys)    
    
    def check_cols(self,df:pd.DataFrame)-> bool:
        try:
            num= len(self.schema_config['columns'])
            df_cols = len(df.columns)
            logging.info(f'Number of the columns in schema: {num} and in df: {df_cols}')
            if num==df_cols:
                return True
            else:
                return False

        except Exception as e:
            raise CustomException(e,sys)
    
    def check_drift(self,train_df:pd.DataFrame,test_df:pd.DataFrame,threshold)-> bool:
        try:
            status= True
            drift_report = {}
            for col in train_df.columns:
                train_data = train_df[col]
                test_data = test_df[col]
                p_value = ks_2samp(train_data, test_data).pvalue
                if threshold > p_value:
                    drift_report[col] = 'drifted'
                    status = False
                else:
                    drift_report[col] = 'not drifted'
                    status = True
                logging.info(f'P-value for column {col}: {p_value}')
            drift_report_file = self.data_validation_config.drift_report_dir
            dir_path = os.path.dirname(drift_report_file)
            os.makedirs(dir_path, exist_ok=True)
            write_yaml_file(file_path=drift_report_file,content=drift_report)
            
        except Exception as e:
            raise CustomException(e,sys)            

            

    def initiate_validation(self)-> DataValidationArtifact:
        try:
            train_file_path= self.data_ingestion_artifact.trained_file_path
            test_file_path= self.data_ingestion_artifact.test_file_path
            train_df = self.read_csv(train_file_path)
            test_df = self.read_csv(test_file_path)
            train_status = self.check_cols(train_df)
            test_status = self.check_cols(test_df)
            status = self.check_drift(train_df,test_df,0.5)
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file)
            test_path =os.path.dirname(self.data_validation_config.valid_test_file)
            os.makedirs(test_path,exist_ok=True)
            os.makedirs(dir_path,exist_ok=True)
            train_df.to_csv(self.data_validation_config.valid_train_file,index=False,header=True)
            test_df.to_csv(self.data_validation_config.valid_test_file,index=False,header=True)

            data_validation = DataValidationArtifact(
                validation_status=train_status,
                valid_train_file=self.data_ingestion_artifact.trained_file_path,
                valid_test_file=self.data_ingestion_artifact.test_file_path,
                invalid_test_file=None,
                invalid_train_file=None,
                drift_report_file=self.data_validation_config.drift_report_dir

            )
        except Exception as e:
            raise CustomException(e,sys)