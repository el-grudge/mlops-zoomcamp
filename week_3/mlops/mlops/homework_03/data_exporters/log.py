from typing import Tuple
from scipy.sparse._csr import csr_matrix
from pandas import DataFrame, Series
import pandas as pd
from numpy import float64, ndarray
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
import pickle


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(
    settings: Tuple[
        csr_matrix, 
        ndarray,
        DictVectorizer, 
        LinearRegression
    ], **kwargs
    ):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    # print('working')
    X_train, y_train, dv, lr = settings
    # Logging the model with MLflow
    mlflow.set_tracking_uri("http://mlflow:5000")

    # Ensure there are no active runs
    if mlflow.active_run():
        mlflow.end_run()

    with mlflow.start_run() as run:
        # Log model
        mlflow.sklearn.log_model(lr, "model")
        # Optionally log other artifacts
        mlflow.log_param("dict_vectorizer", dv)
        print(f"Model logged with run_id: {run.info.run_id}")