from src.emotion import logging, ModelException
from src.emotion.components.model_evaluation import ModelEvaluation
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.entity.config_entity import ModelEvaluationConfig
from src.emotion.constant import *
import sys

STAGE_NAME   = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.initatiate_evaluation()
        except Exception as e:
            raise ModelException(e,sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(f">>>>>>> Stage {STAGE_NAME} Completed  <<<<<<<<")
    except Exception as e:
        raise ModelException(e,sys)