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