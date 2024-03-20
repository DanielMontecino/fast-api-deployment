from typing import Any, List, TypedDict

from pydantic import BaseModel, conlist


class InputData(TypedDict):
    """
    Represents the structure of input data for the logistic regression classifier.

    Attributes:
        fecha_i (str): The start date of the flight.
        OPERA (str): The airline operator.
        TIPOVUELO (str): The type of flight.
        SIGLADES (str): The destination airport code.
        MES (int): The month of the flight.
        DIANOM (str): The day of the week of the flight.
    """

    fecha_i: str
    OPERA: str
    TIPOVUELO: str
    SIGLADES: str
    MES: int
    DIANOM: str


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
        flights (List[List[Any]]): A list of flights, where each flight is represented as a list of 6 items.
        predict (List[int]): A list of predicted values corresponding to each flight.
    """

    flights: List[conlist(Any, min_items=6, max_items=6)]
    predict: List[int]
