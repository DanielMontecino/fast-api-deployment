"""
This module contains constants used in the fast-api-deployment project.

Constants:
- PROJECT_ID: The GCP project ID.
- TOP_10_FEATURES: A list of the top 10 features.
- THRESHOLD_IN_MINUTES: The threshold value in minutes.
- MODEL_PKL: The filename of the logistic regression model.
- DATA_PATH: The path to the data file.
- FEATURE_DOMAIN: A dictionary containing the feature domains.
"""
PROJECT_ID = "alien-airfoil-417901"
TOP_10_FEATURES = [
    "OPERA_American Airlines",
    "OPERA_Avianca",
    "OPERA_Air Canada",
    "MES_7",
    "MES_12",
    "OPERA_Qantas Airways",
    "OPERA_Latin American Wings",
    "OPERA_Gol Trans",
    "OPERA_Copa Air",
    "TIPOVUELO_I",
]

THRESHOLD_IN_MINUTES = 15
MODEL_PKL = "logistic_regression_model-rc-0-0-1.pkl"
RELEASE_MODEL_PKL = f"gs://lg-api/lg-modek/{MODEL_PKL}"
DATA_PATH = "gs://lg-api/lg-data/data.csv"

FEATURE_DOMAIN = {
    "OPERA": [
        "American Airlines",
        "Air Canada",
        "Air France",
        "Aeromexico",
        "Aerolineas Argentinas",
        "Austral",
        "Avianca",
        "Alitalia",
        "British Airways",
        "Copa Air",
        "Delta Air",
        "Gol Trans",
        "Iberia",
        "K.L.M.",
        "Qantas Airways",
        "United Airlines",
        "Grupo LATAM",
        "Sky Airline",
        "Latin American Wings",
        "Plus Ultra Lineas Aereas",
        "JetSmart SPA",
        "Oceanair Linhas Aereas",
        "Lacsa",
    ],
    "TIPOVUELO": ["I", "N"],
    "MES": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
}
