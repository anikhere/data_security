from network_security.components.di import DataIngestion
from network_security.components.dv import *
from network_security.components.dt import *
from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidation, TransformationConfig
from network_security.logging.logging import logging
from network_security.exceptions.exceptions import CustomException
import sys


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()

        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config=training_pipeline_config
        )

        data_ingestion = DataIngestion(
            data_ingestion_config=data_ingestion_config
        )

        artifacts = data_ingestion.initiate_data_ingestion()
        
        logging.info("Started ingestion")
        print(artifacts)
        data_validate_config = DataValidation(training_pipeline_config)
        data_validate = DataValidate(data_validation_config=data_validate_config,data_ingestion_artifact=artifacts)
        logging.info(f'created the config')
        data_validate_artifact = data_validate.initiate_validation()
        logging.info(f'created the artifact')
        data_transform_config = TransformationConfig(training_pipeline_config)
        data_Transformation = DataTransform(data_validate_artifact,TransformationConfig)
        transformer = data_Transformation.get_data_transform()
        data_Transformation_artifact = data_Transformation.initiate_transform()
    except Exception as e:
        raise CustomException(e, sys)
