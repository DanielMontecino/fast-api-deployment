"""
This module contains the implementation of a delay prediction model.

The DelayModel class represents a delay prediction model that uses logistic regression.
It provides methods to preprocess data, fit the model, and make predictions.

Attributes:
    _model (LogisticRegression): The trained logistic regression model.
    _model_path (str): The path to save the model.

Methods:
    preprocess(data: pd.DataFrame, target_column: str = None) -> \
        Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        Prepare raw data for training or prediction.
    fit(features: pd.DataFrame, target: pd.DataFrame) -> None:
        Fit the model with preprocessed data.
    predict(features: pd.DataFrame) -> List[int]:
        Predict delays for new flights.
    validate_inputs(data: List[Dict[str, Any]]) -> bool:
        Validate inputs.
"""

import logging
from typing import Any, Dict, List, Tuple, Union

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle

from .constants import FEATURE_DOMAIN, MODEL_PKL, THRESHOLD_IN_MINUTES, TOP_10_FEATURES
from .preprocess_utils import get_min_diff


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
        validate_inputs: Validate inputs.
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

        if target_column:
            data = shuffle(data, random_state=111)

            # function get_min_diff requires the feature Fecha-O (Date and time of
            # flight operation),
            # so this function can not be used for predictions in production.
            # Therefore, it is not used for preprocessing when target_column is None
            data["min_diff"] = data.apply(get_min_diff, axis=1)
            data[target_column] = np.where(
                data["min_diff"] > THRESHOLD_IN_MINUTES, 1, 0
            )

            target = data[[target_column]]

        features = pd.concat(
            [
                pd.get_dummies(data["OPERA"], prefix="OPERA"),
                pd.get_dummies(data["TIPOVUELO"], prefix="TIPOVUELO"),
                pd.get_dummies(data["MES"], prefix="MES"),            ],
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
            logging.info("Loading model from %s", self._model_path)
            self._model = joblib.load(self._model_path)

        predictions = self._model.predict(features)
        return predictions.astype(int).tolist()

    def validate_inputs(self, data: List[Dict[str, Any]]) -> bool:
        """
        Validate inputs.

        Parameters
        ----------
        data : List[Dict[str, Any]]
            Data to validate.

        Returns
        -------
        bool
            True if data is valid, False otherwise.
        """
        for data_i in data:
            if not set(FEATURE_DOMAIN.keys()).issubset(set(data_i.keys())):
                return False

            for feature, domain in FEATURE_DOMAIN.items():
                if data_i[feature] not in domain:
                    return False
        return True
