from network_security.exceptions.exceptions import CustomException
from network_security.logging import logging 
from network_security.entity.artifacts_entity import DataTransformArtifact,DataTrainerArtifact
from network_security.entity.config_entity import ModelTrainerConfig
from network_security.utlis.ml_utlis.model.estimator import Network_Model
from network_security.utlis.ml_utlis.metric.classification import get_classify
from network_security.utlis.main_utils.utils import save_numpy,save_obj,load_numpy,load_obj,Evaluate
from network_security.entity.config_entity import ModelTrainerConfig
import os 
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier,RandomForestClassifier

class Model_trainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig,data_trans_artifact:DataTransformArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transform_artifact = data_trans_artifact
        except Exception as e:
            raise CustomException(e,sys)
    
        self.model = {
            'Random Forest': RandomForestClassifier(verbose=1),
            'Decision Tree': DecisionTreeClassifier(),
            'Gradient Descent': GradientBoostingClassifier(verbose=1),
            'Log reg': LogisticRegression(verbose=1),
            "AdaBoost": AdaBoostClassifier()
        }
        self.params = {

    'Random Forest': {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    },

    'Decision Tree': {
        'criterion': ['gini', 'entropy', 'log_loss'],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    },

    'Gradient Descent': {   # (Actually Gradient Boosting 😉)
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 10]
    },

    'Log reg': {
        'C': [0.01, 0.1, 1, 10],
        'solver': ['lbfgs', 'liblinear'],
        'max_iter': [100, 200]
    },

    "AdaBoost": {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 1]
    }
}
    
        
    
    def Initiate_model_trainer(self) -> DataTrainerArtifact:
        try:
            train_file_path = self.data_transform_artifact.transformed_train_file
            test_file_path = self.data_transform_artifact.transformed_test_file
        
            train_arr = load_numpy(train_file_path)
            test_arr = load_numpy(test_file_path)

            x_train,y_train,x_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            best_model,report = Evaluate(x_train=x_train,x_test=x_test,y_train=y_test,y_test=y_test,models=self.model,params=self.params)    
