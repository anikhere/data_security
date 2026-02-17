import os 
import sys
import numpy as np
import pandas as pd

TARGET_COLUMN = 'Result'
PIPELINE_NAME: str = 'network_security_pipeline'
ARTIFACTS_DIR: str = 'artifacts'
FILE_NAME: str = 'network_data.csv'
TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'
SCHEMA_FILE_PATH: str = os.path.join(
    'data_schema',
    'schema.yaml'
)
SAVED_MODEL_DIR = os.path.join("saved_models")



DATA_INGESTION_NAME: str = 'NetworkData'
D_I_COLLECTION_NAME: str = "Network_data"

D_I_DB_NAME:str = 'KRISHAI'
D_I_DIR_NAME:str = 'data_ingestion'
D_I_FEATURE:str = 'ingested'
D_I_TRAIN_TEST_SPLIT_RATIO  :float = 0.2

##------ Data Validation Constants--------
Data_val_dir_name:str = 'data_validation'
Data_val_valid_dir:str = 'validated'
Data_val_invalid_dir:str= 'invalid'
Data_val_drift_report_dir:str= 'drift_report'
Data_val_report_name:str = 'report.yaml'

data_transform_dir: str="data transformation"
data_transform_transformed_dir: str = 'transformed'
transformed_object_dir:str="transformed_object"

Data_transformation_input_params: dict = {
    'missing_values': np.nan,
    'n_neighbors':3,
    'weights':'uniform'
}
###----------------------------model Trainer----------------------------------------

model_trainer_dir:str = "model_trainer"
trained_dir:str = 'Trained_model'
MODEL_FILE_NAME:str = 
model_trainer_expected_score:float = 0.6
model_threshold:float = 0.05


