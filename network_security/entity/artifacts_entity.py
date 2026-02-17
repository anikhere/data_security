from dataclasses import dataclass

@dataclass
class Artifact:
    trained_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status:str
    valid_train_file:str
    invalid_train_file:str
    valid_test_file:str
    invalid_test_file:str
    drift_report_file:str

@dataclass
class DataTransformArtifact:
    trans_file_path: str
    transformed_train_file: str
    transformed_test_file: str

@dataclass
class ClassificationMetric:
    f1_score:float
    prediction_score:float
    recall:float

@dataclass
class DataTrainerArtifact:
    trained_model_file_path:str
    train_metric_artifact:ClassificationMetric
    test_metric_artifact:ClassificationMetric