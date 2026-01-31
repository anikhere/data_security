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


DATA_INGESTION_NAME: str = 'NetworkData'
D_I_DB_NAME:str = 'KRISHAI'
D_I_DIR_NAME:str = 'data_ingestion'
D_I_FEATURE:str = 'ingested'
D_I_TRAIN_TEST_SPLIT_RATIO:float = 0.2