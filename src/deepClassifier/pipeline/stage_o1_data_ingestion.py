import logging
from deepClassifier.config import Configuration
from deepClassifier.entity import DataIngestionConfig
from deepClassifier.components import DataIngestion
from deepClassifier import logger


stage_name = " Data ingestion stage"


def main():
    config = Configuration()
    config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>stage {stage_name} started <<<<<<<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>>>>>>>>>>>>stage {stage_name} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
