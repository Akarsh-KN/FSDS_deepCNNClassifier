import logging
from deepClassifier.config import Configuration
from deepClassifier.entity import PrepareBaseModelConfig, TrainingConfig
from deepClassifier.components import PrepareCallBack, Training
from deepClassifier import logger


stage_name = "Model Training "


def main():
    config = Configuration()
    prepare_callback_config = config.get_prepare_callback_config()
    prepare_callbacks = PrepareCallBack(config=prepare_callback_config)
    callback_list = prepare_callbacks.get_ckpt_callbacks()

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(callback_list=callback_list)


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>stage {stage_name} started <<<<<<<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>>>>>>>>>>>>stage {stage_name} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
