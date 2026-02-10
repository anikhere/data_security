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

def save_numpy(file_path:str,array:np.array):
    dir_name= os.path.dirname(file_path)
    os.makedirs(dir_name,exist_ok=True)
    with open(file_path,'wb') as file:
        np.save(file,array)

def save_obj(file_path:str,obj:object):
    try:
        logging.info('starting pickel saving')
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file:
            pickle.dump(obj,file)
        logging.info('saved the pickel file')
    except Exception as e:
        raise CustomException(e,sys) 