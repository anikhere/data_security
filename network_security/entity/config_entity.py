from datetime import datetime
import os 
from network_security.constants import train_pipe

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
