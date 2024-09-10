import logging
from typing import Dict, Tuple
import csv
import os 
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_error, r2_score,accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data[parameters["features"]]
    y = data["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )

    # Define the path using ~ and expand it
    home_directory = os.path.expanduser("~")
    x_test_path = os.path.join(home_directory,'spaceflights', 'data', '06_models', 'X_test.csv')
    y_test_path = os.path.join(home_directory, 'spaceflights', 'data', '06_models', 'y_test.csv')

    # Save the files
    X_test.to_csv(x_test_path, index=False)
    y_test.to_csv(y_test_path, index=False)

    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


# def evaluate_model(
#     regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series
# ) -> Dict[str, float]:
#     """Calculates and logs the coefficient of determination.

#     Args:
#         regressor: Trained model.
#         X_test: Testing data of independent features.
#         y_test: Testing data for price.
#     """
#     y_pred = regressor.predict(X_test)
#     score = r2_score(y_test, y_pred)
#     mae = mean_absolute_error(y_test, y_pred)
#     me = max_error(y_test, y_pred)
    # logger = logging.getLogger(__name__)
    # logger.info("Model has a coefficient R^2 of %.3f on test data.", score)
#     return {"r2_score": score, "mae": mae, "max_error": me}

def predict(regressor: LinearRegression, X_test: pd.DataFrame) -> pd.Series:
    """
    Generates predictions from the trained model.

    Args:
        regressor: Trained model.
        X: Data of independent features for prediction.

    Returns:
        Predictions as a pandas Series.
    """
    logger = logging.getLogger(__name__)
    logger.info("Predict the trained model in the X_test dataset.")
    y_pred = regressor.predict(X_test).ravel()
    y_pred = pd.Series(y_pred)
    return y_pred

def evaluate_model(
    y_test: pd.Series, 
    y_pred: pd.Series,
    y_pred_proba: pd.Series = None  # Optional: Probabilities for ROC AUC score
) -> Dict[str, float]:
    """
    Calculates and logs evaluation metrics for the model.

    Args:
        y_test: Actual values of the target variable.
        y_pred: Predicted values from the model.
        y_pred_proba: Predicted probabilities from the model (used for ROC AUC score, if applicable).

    Returns:
        A dictionary containing evaluation metrics.
    """
    metrics = {}
    
    # For regression tasks
    if y_pred_proba is None:
        score = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        me = max_error(y_test, y_pred)
        metrics.update({
            "r2_score": score,
            "mae": mae,
            "max_error": me
        })
    else:
        # For classification tasks
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')  # Use 'weighted' or other average methods as needed
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        metrics.update({
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "roc_auc_score": roc_auc
        })

    logger = logging.getLogger(__name__)
    logger.info("Model evaluation metrics: %s", metrics)
    
    return metrics

# def fetch_test_data(X_test: pd.DataFrame, y_test: pd.Series):
#     """Fetch the test data from training pipeline output."""
#     return X_test, y_test

