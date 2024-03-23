# Solution Description

## Repository Management

The repository created for this challenge is [fast-api-deployment](https://github.com/DanielMontecino/fast-api-deployment). It adhered to the GitFlow paradigm, utilizing the `main` branch for production. A protection rule was added to the `main` branch to prevent unauthorized pushes, ensuring only accepted pull requests can merge into it.

### CI/CD Process

In the CI/CD process, the CI workflow must pass to allow a feature branch merge into the `main` branch.

## Part I: Model Transcription

In this section, transcription of the model from the provided Jupyter notebook (`exploration.ipynb`) into the `model.py` file was done. Here are the key changes made:

1. **Bug Fixes**: Resolved two bugs, including fixing the `sns.barplot` function and correcting the `get_period_day` function to return values within defined limits.
2. **Code Optimization**: Condensed plotting and training/evaluation functions to avoid code duplication.
3. **Model Selection**: Chose the logistic regression model with balanced weights and feature importance, based on its F1-score and interpretability.


### Model Selection

The choice of model should depend on the business requirements and the rationale behind building a delay prediction system.

For instance, one intuitive reason might be to preemptively take actions to prevent flights from being delayed. Depending on the nature of these actions, the delay prediction system could be more tolerant to different kind of errors. If the cost of the preemptible action is low, then the system might be tolerant for False Positives (FP). Otherwise, if the cost of the action is high, the system might not be tolerant to False Positives (FP). In the first case, the metric for evaluation could be recall, whereas in the second case precision is more appropriate.


Without knowledge of the specific business objectives, an appropriate metric for many imbalanced classification problems is the F1-score; therefore, F1-score is the chosen metric for selecting the model.

Both XGBoost and Logistic Regression with feature importance and weights balancing have the greatest F1-score. Also, they have the same metric values, not just F1-score. Therefore, since its complexity is lower and it is more interpretable, the selected model to deploy is Logistic Regression with "balance" and feature importance.

It is worth noting that the current model selection is not set in stone and may be subject to change based on improvements to other models, such as XGBoost, or consideration of additional requirements.

## Model transcription

Some of the features about transcribe the model into the `DelayModel` class are:

1.  Features and threshold in minutes were defined in constants.py file to separate static parameters from the code.
2.  Processing function were defined in processing_utils.py file to separate them from the model.
3.  When preprocessing, feature "min_diff" is only computed when target_column is given, meaning that ground truth is available in the data. In production, "min_diff" can not be computed since the time of flight operation is unknown.
4.  When fitting the model, the fitted model is dumped so it can be loaded in future executions.
5.  When predicting, if the model was not fitted but it was dumped before, it is loaded.

On the other hand, the data path defined in test_model.py was wrong, so it was changed. The features defined in this file were also modified to match computed ones.


## Part II: FastAPI Implementation

### Implementation Details

In this part, the API was implemented using FastAPI (`api.py`). Key points include:

1. **API Methods**: Implemented `predict`, `health`, and `check_model` methods for model prediction, API health check, and model validation, respectively.
2. **Folder Structure**: Organized the API into separate folders for routes and source code, with a dedicated module for data models.
3. **Local Deployment**: Provided a script (`./bin/init_app.sh`) to run the API locally.


To run the api locally, just run:

```
./bin/init_app.sh
```

## Part III: Cloud Deployment

### GCP Deployment

In order to deploy the API in a cloud provider, GCP was purchased. 

The selected service was Cloud Run, since it one of the serverless solutions in GCP. Other serverless service is Cloud Function, but it is less customizable since it does not allow the developer to use a custom image. Key steps included:

1. **GCP Services Setup**: Acquired necessary GCP services and enabled required services such as Artifact Registry, Cloud Run, and Vertex AI Workbench.
2. **Repository Configuration**: Created a repository in Artifact Registry and set up a workbench in Vertex to work with.
3. **Docker Image Creation**: Wrote a `Dockerfile`, built the Docker image locally, and submitted it to the Artifact Registry repository.
4. **Cloud Run Service Creation**: Created a Cloud Run service using the Docker image, making it publicly accessible.
5. **Deployment Script**: Consolidated deployment steps into a bash script (`bin/deploy_api.sh`).



## Part IV: CI/CD Implementation

### Continuous Integration

Implemented a GitHub Actions workflow (`ci.yml`) for continuous integration. This workflow tests repository changes, sets up a virtual environment, runs model and API tests, and performs code quality checks using pylint.

### Continuous Delivery

For continuous delivery, a GitHub Actions workflow (`cd.yml`) was implemented. This workflow clones the repo, authenticates the run in GCP, builds and pushes the Docker image, and deploys it to a Cloud Run service.

By following these steps, a streamlined process for model deployment and continuous integration/delivery is ensured.

The GCP setting for CD was implemented in `bin/cd_setting.sh` script.
