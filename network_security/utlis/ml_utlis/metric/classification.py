from network_security.entity.artifacts_entity import ClassificationMetric
from sklearn.metrics import f1_score,precision_score,recall_score
from network_security.exceptions.exceptions import CustomException
import os 
import sys
def get_classify(Y_true,y_pred)->ClassificationMetric:
    try:
        model_f1 = f1_score(Y_true,y_pred)
        model_recall = recall_score(Y_true,y_pred)
        model_precise = precision_score(Y_true,y_pred)

        claasification= ClassificationMetric(
            f1_score=model_f1,
            prediction_score=model_precise,
            recall=model_recall
        )
        return claasification
    except Exception as e:
        raise CustomException(e,sys)