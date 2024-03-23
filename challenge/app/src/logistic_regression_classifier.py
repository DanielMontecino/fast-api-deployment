"""
This module contains the data models for the logistic regression classifier.
"""
from typing import Any, List, TypedDict

from pydantic import BaseModel, conlist


class InputData(TypedDict):
    """
    Represents the structure of input data for the logistic regression classifier.

    Attributes:
        OPERA (str): The airline operator.
        TIPOVUELO (str): The type of flight.
        MES (int): The month of the flight.
    """
    OPERA: str
    TIPOVUELO: str
    MES: int


class LogisticRegression(BaseModel):
    """
    Represents the input data for logistic regression prediction.

    Attributes:
        flights (List[InputData]): Input data
    """
    flights: List[InputData]


class LogisticRegressionPredictionResponse(BaseModel):
    """
    Represents the response of a logistic regression prediction.

    Attributes:
        predict (List[int]): The predicted values.
    """
    predict: List[int]


class LogisticRegressionCheckResponse(BaseModel):
    """
    Represents the response object for the logistic regression check.

    Attributes:
        flights (List[List[Any]]): A list of flights, where each flight is represented \
            as a list of 6 items.
        predict (List[int]): A list of predicted values corresponding to each flight.
    """

    flights: List[conlist(Any, min_items=3, max_items=3)]
    predict: List[int]
