from network_security.components.di import DataIngestion
from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
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

    except Exception as e:
        raise CustomException(e, sys)
