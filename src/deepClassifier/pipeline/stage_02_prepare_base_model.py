import logging
from deepClassifier.config import Configuration
from deepClassifier.entity import PrepareBaseModelConfig
from deepClassifier.components import PrepareBaseModel
from deepClassifier import logger


stage_name = " Prepare Base model"


def main():
    config = Configuration()
    config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>stage {stage_name} started <<<<<<<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>>>>>>>>>>>>stage {stage_name} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
