import os
from typing import Dict, Optional, Tuple, Union

import mlflow
from mlflow import MlflowClient
from mlflow.sklearn import log_model as log_model_sklearn
from mlflow.xgboost import log_model as log_model_xgboost
import xgboost as xgb
from sklearn.base import BaseEstimator


# setup experiment
DEFAULT_DEVELOPER = os.getenv('EXPERIMENTS_DEVELOPER', 'mager')
DEFAULT_EXPERIMENT_NAME = 'bank-marketing-mage'
DEFAULT_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI', '"http://mlflow:5000"')


def setup_experiment(experiment_name, tracking_uri):
    mlflow.set_tracking_uri(tracking_uri or DEFAULT_TRACKING_URI)
    experiment_name = experiment_name or DEFAULT_EXPERIMENT_NAME

    client = MlflowClient()
    experiment = client.get_experiment_by_name(experiment_name)

    if experiment:
        experiment_id = experiment.experiment_id
    else:
        experiment_id = client.create_experiment(experiment_name)

    return client, experiment_id


def track_experiment(
    model: Optional[Union[BaseEstimator, xgb.Booster]] = None,
    block_uuid: Optional[str] = None,
    partition: Optional[str] = None,
    pipeline_uuid: Optional[str] = None,
    run_name: Optional[str] = None,
    hyperparameters: Dict[str, Union[float, int, str]] = {},
    metrics: Dict[str, float] = {},
    **kwargs,
):
    experiment_name = DEFAULT_EXPERIMENT_NAME
    tracking_uri = DEFAULT_TRACKING_URI

    client, experiment_id = setup_experiment(experiment_name, tracking_uri)

    if not run_name:
        run_name = ':'.join(
            [str(s) for s in [pipeline_uuid, partition, block_uuid] if s]
        )

    run = client.create_run(experiment_id, run_name=run_name or None)
    run_id = run.info.run_id

    for key, value in [
        ('developer', DEFAULT_DEVELOPER),
        ('model', model.__class__.__name__),
    ]:
        if value is not None:
            client.set_tag(run_id, key, value)

    for key, value in [
        ('block_uuid', block_uuid),
        ('partition', partition),
        ('pipeline_uuid', pipeline_uuid),
    ]:
        if value is not None:
            client.log_param(run_id, key, value)

    for key, value in hyperparameters.items():
        client.log_param(run_id, key, value)
        print(f'Logged hyperparameter {key}: {value}.')

    for key, value in metrics.items():
        client.log_metric(run_id, key, value)
        print(f'Logged metric {key}: {value}.')
    #client.log_metric(metrics)

    if model:
        log_model = None

        if isinstance(model, BaseEstimator):
            log_model = log_model_sklearn
        elif isinstance(model, xgb.Booster):
            log_model = log_model_xgboost

        if log_model:
            opts = dict(artifact_path='models', input_example=None)
            print(log_model)
            print(opts)

            log_model(model, **opts)
            print(f'Logged model {model.__class__.__name__}.')

    return run

    
