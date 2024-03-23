"""
This module contains the API routes for model prediction.
"""
import fastapi
import pandas as pd
from fastapi import APIRouter
from loguru import logger as logging

import challenge.app.src.classifier as CLF
from challenge.app.src.logistic_regression_classifier import (
    LogisticRegression,
    LogisticRegressionPredictionResponse,
)

app_log_reg_predict = APIRouter()


@app_log_reg_predict.post(
    "/predict",
    tags=["Predictions"],
    response_model=LogisticRegressionPredictionResponse,
    description="Get Regression Response",
)
async def post_predict(log_reg: LogisticRegression) -> dict:
    """Get Logistic Regression Response

    Parameters
    ----------
    log_reg : LogisticRegression
        Logistic Regression data

    Returns
    -------
    dict
        Prediction

    Raises
    ------
    fastapi.HTTPException
        If the data is not valid
    """
    data = dict(log_reg)["flights"]
    is_valid = CLF.model.validate_inputs(data)
    if not is_valid:
        raise fastapi.HTTPException(status_code=400)
    data = pd.DataFrame.from_dict(data)
    logging.info(f"Data: {data}")
    logging.info(f"Model: {type(CLF.model)}")
    input_feat = CLF.model.preprocess(data)
    prediction = CLF.model.predict(input_feat)
    logging.info(f"Prediction: {prediction}")
    return {"predict": prediction}
