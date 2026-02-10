import sys
import os
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
import numpy as np
from network_security.constants.train_pipe import TARGET_COLUMN,Data_transformation_input_params
from network_security.entity.artifacts_entity import DataTransformArtifact,DataValidationArtifact
from network_security.entity.config_entity import TransformationConfig
from network_security.exceptions.exceptions import CustomException
from network_security.logging import logging 
from network_security.utlis.main_utils.utils import save_numpy,save_obj

class DataTransform:
    def __init__(self,DataValidationArtifact:DataValidationArtifact,transform_config:TransformationConfig)->DataValidationArtifact:
        try:
            self.dataValidateArtifact = DataValidationArtifact
            self.transform_config = transform_config
            self.Target = TARGET_COLUMN
            self.params = Data_transformation_input_params
        except Exception as e:
            raise CustomException(e,sys)
    @staticmethod
    def read_csv(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CustomException(e, sys)
    
    def get_data_transform(self)->Pipeline:
        logging.info('Entered the data transformation')
        try:
            self.imputer:KNNImputer=KNNImputer(**Data_transformation_input_params)
            logging.info(f'starting the imputer step')
            self.preprocessor:Pipeline = Pipeline([('imputer',self.imputer)])
            return self.preprocessor
        except Exception as e:
            raise CustomException (e,sys)


    def initiate_transform(self) ->DataTransformArtifact:
        logging.info('starting the Data_transformation======')
        try:
            train_df = DataTransform.read_csv(self.dataValidateArtifact.valid_train_file)
            test_df= DataTransform.read_csv(self.dataValidateArtifact.valid_test_file)

            input_features = train_df.drop(columns=[self.Target],axis=1)
            output_feature = train_df[self.Target]
            output_feature = output_feature.replace(-1,0)
            preprocesor = self.get_data_transform()
            obj = preprocesor.fit(input_features)
            transformed_input_train_feature = obj.transform(input_features)
            transformed_input_test_feature = obj.transform(output_feature)

            train_arr = np.c_[transformed_input_train_feature, np.array(input_features)]
            test_arr = np.c_[transformed_input_test_feature, np.array(output_feature)]
            save_numpy(self.transform_config.data_tranformed_train_path,train_arr)
            save_numpy(self.transform_config.data_tranformed_test_path,test_arr)
            save_obj(self.transform_config.transformed_object,obj)
        except Exception as e:
            raise CustomException(e,sys)
        
