import logging
from typing import List, Tuple, Union, Dict, Any
from datetime import datetime
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle

from .constants import THRESHOLD_IN_MINUTES, TOP_10_FEATURES, MODEL_PKL, FEATURE_DOMAIN
from .preprocess_utils import get_min_diff, get_period_day, is_high_season


class DelayModel:
    """
    A class representing a delay prediction model.

    Attributes:
        _model: The trained logistic regression model.
        _model_path: The path to save the model.

    Methods:
        preprocess: Prepare raw data for training or prediction.
        fit: Fit the model with preprocessed data.
        predict: Predict delays for new flights.
    """

    def __init__(
        self,
    ):
        """Contructor for DelayModel.

        Parameters
        ----------
        save_model_path : str, optional
            Path to save the model, by default "logistic_regression_model-rc-0-0-1.pkl"
        """

        self._model = None  # Model should be saved in this attribute.
        self._model_path = MODEL_PKL

    def preprocess(
        self, data: pd.DataFrame, target_column: str = None
    ) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Prepare raw data for training or predict.

        Args:
            data (pd.DataFrame): raw data.
            target_column (str, optional): if set, the target is returned.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: features and target.
            or
            pd.DataFrame: features.
        """
        data = data.copy()
        data["period_day"] = data["Fecha-I"].apply(get_period_day)
        data["high_season"] = data["Fecha-I"].apply(is_high_season)

        if target_column:
            data = shuffle(data, random_state=111)

            # function get_min_diff requires the feature Fecha-O (Date and time of flight operation),
            # so this function can not be used for predictions in production.
            # Therefore, it is not used for preprocessing when target_column is None
            data["min_diff"] = data.apply(get_min_diff, axis=1)
            data[target_column] = np.where(
                data["min_diff"] > THRESHOLD_IN_MINUTES, 1, 0
            )

            target = data[[target_column]]

        features = pd.concat(
            [
                data["high_season"],
                pd.get_dummies(data["period_day"], prefix="period_day"),
                pd.get_dummies(data["OPERA"], prefix="OPERA"),
                pd.get_dummies(data["TIPOVUELO"], prefix="TIPOVUELO"),
                pd.get_dummies(data["SIGLADES"], prefix="SIGLADES"),
                pd.get_dummies(data["MES"], prefix="MES"),
                pd.get_dummies(data["DIANOM"], prefix="DIANOM"),
            ],
            axis=1,
        )
        
        for feature in TOP_10_FEATURES:
            if feature not in features.columns:
                features[feature] = 0

        if target_column:
            return features[TOP_10_FEATURES], target
        return features[TOP_10_FEATURES]

    def fit(
        self,
        features: pd.DataFrame,
        target: pd.DataFrame,
    ) -> None:
        """
        Fit model with preprocessed data.

        Args:
            features (pd.DataFrame): preprocessed data.
            target (pd.DataFrame): target.
            save_model_path (str, optional): path to save the model.
        """
        n_y0 = len(target[target.values == 0])
        n_y1 = len(target[target.values == 1])

        self._model = LogisticRegression(
            class_weight={1: n_y0 / len(target), 0: n_y1 / len(target)}
        )

        self._model.fit(features, target)
        if self._model_path:
            joblib.dump(self._model, self._model_path)

        return

    def predict(self, features: pd.DataFrame) -> List[int]:
        """
        Predict delays for new flights.

        Args:
            features (pd.DataFrame): preprocessed data.

        Returns:
            (List[int]): predicted targets.
        """
        assert (
            self._model is not None or self._model_path is not None
        ), "Model is not fitted."
        if self._model is None:
            logging.info(f"Loading model from {self._model_path}")
            self._model = joblib.load(self._model_path)

        predictions = self._model.predict(features)
        return predictions.astype(int).tolist()
    
    def validate_inputs(self, data: List[Dict[str, Any]]) -> bool:
        for data_i in data:
            if not set(FEATURE_DOMAIN.keys()).issubset(set(data_i.keys())):
                return False
            
            for feature in FEATURE_DOMAIN.keys():
                if feature == "Fecha-I":
                    try:
                        datetime.strptime(data_i[feature], '%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        return False
                else:
                    if data_i[feature] not in FEATURE_DOMAIN[feature]:
                        return False
        return True
        
