from random import choice

import challenge.app.src.classifier as clf
import pandas as pd
from challenge.app.src.logistic_regression_classifier import (
    LogisticRegressionCheckResponse,
)
from challenge.constants import FEATURE_DOMAIN
from fastapi import APIRouter
from loguru import logger as logging

app_log_reg_check = APIRouter()

DATE_SAMPLES = {
    "Fecha-I": [
        "2017-01-01 23:30:00",
        "2018-01-02 23:30:00",
        "2018-04-03 23:30:00",
        "2019-12-25 14:55:00",
        "2020-10-29 14:55:00",
        "2022-05-31 14:55:00",
    ],
}


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
    domain_dict = {**FEATURE_DOMAIN, **DATE_SAMPLES}
    data_samp = [choice(domain_dict[col]) for col in domain_dict.keys()]
    data = pd.DataFrame([data_samp], columns=list(domain_dict.keys()))
    data

    logging.info(f"Data: {data}")
    logging.info(f"Model: {type(clf)}")
    input_feat = clf.model.preprocess(data)
    prediction = clf.model.predict(input_feat)
    logging.info(f"Prediction: {prediction}")
    logging.info(f"data: {data.values.tolist()}")
    return {"flights": data.values.tolist(), "predict": prediction}
