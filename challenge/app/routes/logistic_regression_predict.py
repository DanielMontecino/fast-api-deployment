import challenge.app.src.classifier as clf
import fastapi
import pandas as pd
from challenge.app.src.logistic_regression_classifier import (
    LogisticRegression,
    LogisticRegressionPredictionResponse,
)
from fastapi import APIRouter
from loguru import logger as logging

app_log_reg_predict = APIRouter()


@app_log_reg_predict.post(
    "/predict",
    tags=["Predictions"],
    response_model=LogisticRegressionPredictionResponse,
    description="Get Regression Response",
)
async def post_predict(log_reg: LogisticRegression, status_code=200) -> dict:
    data = dict(log_reg)["flights"]
    is_valid = clf.model.validate_inputs(data)
    if not is_valid:
        raise fastapi.HTTPException(status_code=400)
    data = pd.DataFrame.from_dict(data)
    data.rename(columns={"fecha_i": "Fecha-I"}, inplace=True)
    logging.info(f"Data: {data}")
    logging.info(f"Model: {type(clf.model)}")
    input_feat = clf.model.preprocess(data)
    prediction = clf.model.predict(input_feat)
    logging.info(f"Prediction: {prediction}")
    return {"predict": prediction}
