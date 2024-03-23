import pandas as pd
import os
from challenge.model import DelayModel
from typing import Tuple
from challenge.constants import MODEL_PKL, DATA_PATH

def ingestion() -> pd.DataFrame:
    data_path = os.path.join(DATA_PATH)
    return pd.read_csv(filepath_or_buffer=data_path)

def preprocess(data: pd.DataFrame, model: DelayModel) -> Tuple[pd.DataFrame, pd.Series]:
    features, target = model.preprocess(data=data, target_column="delay")
    return features, target
    
def train(model: DelayModel, X_train: pd.DataFrame, y_train: pd.Series) -> None:
    model.fit(features=X_train, target=y_train)
    
def save_model(model: DelayModel, dst: str) -> DelayModel:
    model.save(dst=dst)
    return model
    
if __name__ == "__main_":
    model = DelayModel()
    data = ingestion()
    X_train, y_train = preprocess(data=data, model=model)
    model = train(model=model, X_train=X_train, y_train=y_train)
    model.save(dst=MODEL_PKL)
    
    