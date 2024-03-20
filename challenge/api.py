from fastapi import FastAPI
from loguru import logger as logging

import challenge.app.src.classifier as clf
from challenge.app.routes.home import app_home
from challenge.app.routes.logistic_regression_predict import app_log_reg_predict
from challenge.app.routes.model_check import app_log_reg_check
from challenge.model import DelayModel

logging.add("logs/app_logs", level="INFO")
clf.model = DelayModel()

app = FastAPI(
    title="Flights Delay Classification API",
    description="API to predict if a flight is delayed",
    version="1.0",
)

app.include_router(app_home)
app.include_router(app_log_reg_predict)
app.include_router(app_log_reg_check)
