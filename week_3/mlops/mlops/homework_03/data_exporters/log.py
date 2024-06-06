from typing import Tuple
from scipy.sparse._csr import csr_matrix
from pandas import DataFrame, Series
import pandas as pd
from numpy import float64
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
import pickle


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


def log_model_and_artifact(model, vectorizer, model_name='linear_regression_model', artifact_name='dict_vectorizer.pkl'):
    # Start a new MLflow run
    with mlflow.start_run():
        # Log the linear regression model
        mlflow.sklearn.log_model(model, model_name)
        
        # Save the DictVectorizer object to a file
        with open(artifact_name, 'wb') as f:
            pickle.dump(vectorizer, f)
        
        # Log the DictVectorizer object as an artifact
        mlflow.log_artifact(artifact_name)

        print(f"Model and artifact logged successfully. Run ID: {mlflow.active_run().info.run_id}")


@data_exporter
def export_data(
    settings: Tuple[
        csr_matrix, 
        Series,
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
    X_train, y_train, dv, lr = settings

    # train the model
    lr.fit(X_train, y_train)

    # Log the model and vectorizer
    # log_model_and_artifact(dv, lr)
