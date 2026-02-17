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
    
def load_obj(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception('no file found',file_path)
        with open(file_path,'rb') as f:
            print(f'the model is{f} ')
            return pickle.load(f)
    except Exception as e:
        raise CustomException(e,sys)

def load_numpy(file_path:str)->np.array:
    try:
        with open(file_path,'rb') as f:
            return np.load(f)
    except Exception as e:
        raise CustomException(e,sys)
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def Evaluate(x_train, y_train, x_test, y_test, models, params):
    try:
        report = {}
        best_models = {}

        for model_name, model_obj in models.items():

            print(f"Running GridSearchCV for {model_name}")

            param_grid = params[model_name]

            gs = GridSearchCV(
                estimator=model_obj,
                param_grid=param_grid,
                cv=3,
                n_jobs=-1
            )

            gs.fit(x_train, y_train)

            best_model = gs.best_estimator_

            y_pred = best_model.predict(x_test)

            score = accuracy_score(y_test, y_pred)

            report[model_name] = score

            best_models[model_name] = {
                "model": best_model,
                "params": gs.best_params_,
                "score": score
            }

        # Select Best Model
        best_model_name = max(report, key=report.get)
        best_model_info = best_models[best_model_name]

        print(f"\nBest Model: {best_model_name}")
        print(f"Best Score: {best_model_info['score']}")
        print(f"Best Params: {best_model_info['params']}")

        return best_model_info, report

    except Exception as e:
        raise e
     


