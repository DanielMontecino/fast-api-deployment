import pandas as pd
import os
from pathlib import Path


def ingestion():
    data_path = os.path.join(
        Path(os.path.dirname(__file__)).parent.parent, "data/data.csv"
    )
    return pd.read_csv(filepath_or_buffer=data_path)

self.model = DelayModel()
    data_path = os.path.join(
        Path(os.path.dirname(__file__)).parent.parent, "data/data.csv"
    )
    self.data = pd.read_csv(filepath_or_buffer=data_path)

features, target = self.model.preprocess(data=self.data, target_column="delay")

_, features_validation, _, target_validation = train_test_split(
    features, target, test_size=0.33, random_state=42
)

self.model.fit(features=features, target=target)

predicted_target = self.model._model.predict(features_validation)

report = classification_report(
    target_validation, predicted_target, output_dict=True
        )