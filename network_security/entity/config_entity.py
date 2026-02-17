from datetime import datetime
import os 
from network_security.constants.train_pipe import train_pipe

print(train_pipe.ARTIFACTS_DIR)

class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir = os.path.join(
            train_pipe.ARTIFACTS_DIR,
            f"{train_pipe.PIPELINE_NAME}_{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        self.pipeline_name = train_pipe.PIPELINE_NAME
        self.artifact_name = train_pipe.FILE_NAME

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir,
            train_pipe.D_I_DIR_NAME
        )
        self.database_name = train_pipe.D_I_DB_NAME
        self.collection_name = train_pipe.DATA_INGESTION_NAME
        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir,
            train_pipe.D_I_FEATURE,
            train_pipe.FILE_NAME
        )
        self.train_file_path = os.path.join(
            self.data_ingestion_dir,
            train_pipe.D_I_FEATURE,
            train_pipe.TRAIN_FILE_NAME
        )
        self.test_file_path = os.path.join(
            self.data_ingestion_dir,
            train_pipe.D_I_FEATURE,
            train_pipe.TEST_FILE_NAME
        )
        self.test_size = train_pipe.D_I_TRAIN_TEST_SPLIT_RATIO
        collection_name = train_pipe.DATA_INGESTION_NAME
        db_name = train_pipe.D_I_DB_NAME

##__________Data Validation Config__________##
class DataValidation:
    def __init__(self,train_config:TrainingPipelineConfig):
        self.data_val_dir = os.path.join(
            train_config.artifact_dir,
            train_pipe.Data_val_dir_name
        )
        self.valid_data_dir = os.path.join(
            self.data_val_dir,
            train_pipe.Data_val_valid_dir
        )
        self.invalid_data_dir = os.path.join(
            self.data_val_dir,
            train_pipe.Data_val_invalid_dir
        )
        self.valid_train_file = os.path.join(
            self.valid_data_dir,
            train_pipe.TRAIN_FILE_NAME
        )
        self.valid_test_file = os.path.join(
            self.valid_data_dir,
            train_pipe.TEST_FILE_NAME
        )
        self.invalid_train_file = os.path.join(
            self.invalid_data_dir,
            train_pipe.TRAIN_FILE_NAME
        )
        self.invalid_test_file = os.path.join(
            self.invalid_data_dir,
            train_pipe.TEST_FILE_NAME
        )
        self.drift_report_dir = os.path.join(
            self.data_val_dir,
            train_pipe.Data_val_drift_report_dir,
            train_pipe.Data_val_report_name
        )
        
class TransformationConfig:
    def __init__(self,train_config:TrainingPipelineConfig):
        self.data_transformation_dir:str = os.path.join(train_config.artifact_dir,train_pipe.data_transform_dir)
        self.data_transformed_file_path:str = os.path.join(self.data_transformation_dir,train_pipe.data_transform_transformed_dir)
        self.data_tranformed_train_path:str = os.pah.join(self.data_transformation_dir,train_pipe.TRAIN_FILE_NAME)
        self.data_tranformed_test_path:str = os.pah.join(self.data_transformation_dir,train_pipe.TEST_FILE_NAME)
        self.transformed_object:str = os.path.join(self.data_transformation_dir,train_pipe.transformed_object_dir)

class ModelTrainerConfig:
    def __init__(self,train_config:TrainingPipelineConfig):
        self.data_trainer_dir:str = os.path.join(train_pipe.artifact_dir,train_pipe.model_trainer_dir)
        self.train_model_path:str = os.path.join(train_pipe.trained_dir,train_pipe.model_file_name)
        self.expected_acc: float = os.path.join(train_pipe.model_trainer_expected_score)
        self.overfitting_threshold = train_pipe.model_threshold


