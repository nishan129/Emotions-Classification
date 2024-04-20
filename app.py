
from fastapi import FastAPI
import uvicorn
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.emotion.pipeline.prediction import PredictionPipeline
from src.emotion.config.configuration import ConfigurationManager
from src.emotion.pipeline.training_pipeline import TrainingPipeline
from src.emotion import ModelException, logging
import pandas as pd

text:str = "feel curiou previou earli dawn time seek troubl"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")




@app.get("/train")
async def training():
    try:
        train_pipeline = TrainingPipeline()

        train_pipeline.main()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    


@app.post("/predict")
async def predict_route(text):
    try:
        config = ConfigurationManager()
        pre_config = config.get_prediction_config()
        predict = PredictionPipeline(config=pre_config)
        text = predict.predict(text)
        return text
    except Exception as e:
        raise ModelException(e, sys) from e
    



if __name__=="__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)


    