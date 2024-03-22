"""
This module contains the API routes for the model check.
"""
from random import choice

import pandas as pd
from fastapi import APIRouter
from loguru import logger as logging

import challenge.app.src.classifier as CLF
from challenge.app.src.logistic_regression_classifier import (
    LogisticRegressionCheckResponse,
)
from challenge.constants import FEATURE_DOMAIN

app_log_reg_check = APIRouter()

@app_log_reg_check.post(
    "/check",
    tags=["Check"],
    response_model=LogisticRegressionCheckResponse,
    description="Get Regression Response from random data",
)
async def check_model() -> dict:
    """Get Logistic Regression Response from random data

    Returns
    -------
    dict
        Data and Prediction
    """
    logging.info("Check model")
    data_samp = [choice(domain) for domain in FEATURE_DOMAIN.values()]
    data = pd.DataFrame([data_samp], columns=list(FEATURE_DOMAIN.keys()))
    logging.info(f"Data: {data}")
    logging.info(f"Model: {type(CLF)}")
    input_feat = CLF.model.preprocess(data)
    prediction = CLF.model.predict(input_feat)
    logging.info(f"Prediction: {prediction}")
    logging.info(f"data: {data.values.tolist()}")
    return {"flights": data.values.tolist(), "predict": prediction}
