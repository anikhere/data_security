import yaml
from network_security.exceptions.exceptions import CustomException
import sys
from logging import logging 
import numpy as np 
import pickle
import os 

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,'r') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e,sys)
def write_yaml_file(file_path:str,content:object,replace:bool)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            with open(file_path,'w') as file:
                 yaml.dump(content,file)
    except Exception as e:
        raise CustomException(e,sys)