"""
This module contains the main FastAPI application for the Flights Delay Classification API.

It imports the necessary modules and sets up the FastAPI application
with routers for different routes.
"""

from fastapi import FastAPI
from loguru import logger as logging

import challenge.app.src.classifier as CLF
from challenge.app.routes.home import app_home
from challenge.app.routes.logistic_regression_predict import app_log_reg_predict
from challenge.app.routes.model_check import app_log_reg_check
from challenge.model import DelayModel
from challenge.constants import RELEASE_MODEL_PKL

logging.add("logs/app_logs", level="INFO")
CLF.model = DelayModel()
CLF.model.load(RELEASE_MODEL_PKL)

app = FastAPI(
    title="Flights Delay Classification API",
    description="API to predict if a flight is delayed",
    version="1.0",
)

app.include_router(app_home)
app.include_router(app_log_reg_predict)
app.include_router(app_log_reg_check)
