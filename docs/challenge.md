# Solution description

The repository created for this challenge is [fast-api-deployment](https://github.com/DanielMontecino/fast-api-deployment).
This repository was managed with GitFlow paradigm. The production branch is main and a protection rule was added to this branch to block pushes over it, only accepted PR can merge to the main branch.

## Part I

In this part the following chages were added to the exploration.ipynb file:

1. Solve two bugs. The first in sns.barplot function, which needs to type parameters x and y. The second in the get_period_day function which returns None when date is on the defined limits.
2. Plotting was condensed in function plot_flights_by_feature to avoid code duplication
3. Some features were computed but not used (high_season, and period_day), while other were filtered to form the training data, but they neither were used (SIGLADES and DIANOM). These features were added to the feature dataframe.
4. The training and evaluation were also condensed in one function (train_and_eval_model) to avoid duplicated code.
5. Since we added more features, the previously selected ones are not the most important for the model. Moreover, even without adding feaures of step (3), the most important features are not the same as the previously defined. Thefero, most importatn features were obtained.

### Model Selection

The choice of model should depend on the business requirements and the rationale behind building a delay prediction system.

For instance, one intuitive reason might be to preemptively take actions to prevent flights from being delayed. Depending on the nature of these actions, the delay prediction system may incur errors of one type or another. If the action involves simply alerting the crew and passengers to expedite boarding, then the system may produce False Positives (FP) as the cost of predicting a flight as delayed when it is not is relatively low. Conversely, if the action entails preparing another plane, which is a costly action, it is undesirable for the model to have False Negative (FN) errors. In the first case, the metric for evaluation could be recall, whereas in the second case precision is more appropriate.

However, without knowledge of the specific business objectives, an appropriate metric for many imbalanced classification problems is the F1-score; therefore, F1-score is the chosen metric for selecting the model.

Models with highest F1-score are the ones "balanced" and with feature importance.
Both XGBoost and Logistic Regression with feature importance and weights balancing have the greatest F1-score. Also, they have the same metric values, not just F1-score. Therefore, since its complexity is lower and it is more interpretable, the selected model to deploy is Logistic Regression with "balance" and feature importance.

The current model selection is not static and can be changed if improvements are implemented in other models such as XGBoost or if other requirements need to be considered.

## Model transcription

Some of the features about transcribe the model into the DelayModel class are:

1.  Features and threshold in minutes were defined in constants.py file to separate static parameters from the code.
2.  Processing function were defined in processing_utils.py file to separate them from the model.
3.  When preprocessing, feature "min_diff" is only computed when target_column is given, meaning that ground truth is available in the data. In production, "min_diff" can not be computed since the time of flight operation is unknown.
4.  When fitting the model, the fitted model is dumped so it can be loaded in future executions.
5.  When predicting, if the model was not fitted but it was dumped before, it is loaded.

On the other hand, the data path defined in test_model.py was wrong, so it was changed. The features defined in this file were also modified to match computed ones.
