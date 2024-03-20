from typing import Any, List

from pydantic import BaseModel, conlist
from typing_extensions import TypedDict


class InputData(TypedDict):
    fecha_i: str
    OPERA: str
    TIPOVUELO: str
    SIGLADES: str
    MES: int
    DIANOM: str


class LogisticRegression(BaseModel):
    flights: List[InputData]


class LogisticRegressionPredictionResponse(BaseModel):
    predict: List[int]


class LogisticRegressionCheckResponse(BaseModel):
    flights: List[conlist(Any, min_items=6, max_items=6)]
    predict: List[int]
