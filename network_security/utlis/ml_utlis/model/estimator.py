from network_security.constants.train_pipe import *
import os 
import sys
from network_security.logging import logging
from network_security.exceptions.exceptions import CustomException

class Network_Model:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise CustomException(e,sys)
    
    def predict(self,x):
        x_tranform = self.preprocessor.transform(x)
        y_hat = self.model.predict(x_tranform)
        return y_hat