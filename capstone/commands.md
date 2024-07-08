to start mlflow

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

to start tracking experiments

```python
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("nyc-taxi-experiment")
```

simple way to track runs:

```python
with mlflow.start_run(): # save model with mlfow

    mlflow.set_tag("develop","cristian") # set tags
    
    mlflow.log_param("train-data-path", "./data/green_tripdata_2021-01.csv") # logs relevant information, such as training data
    mlflow.log_param("valid-data-path", "./data/green_tripdata_2021-02.csv") 

    alpha = 0.01
    mlflow.log_param("alpha", alpha) # log hyperparameter
    lr = Lasso(alpha)
    lr.fit(X_train, y_train)

    y_pred = lr.pred(X_val)
    rmse = mean_squared_error(y_val, y_pred, squared=False)
    mlflow.log_metric("rmse", rmse) # log metric
```

log hyperparameter tuning with mlflow

1- use `hyperopt` library for hyperparameter tuning:
    * `fmin` method identifies the parameters that minimize the loss value
    * `tpe` is the algorithm that fmin uses 
    * `hp` is where we define the search space
    * `STATUS_OK` a signal that we send at the end of each run to signal success
    * `Trails` keeps track of the information after each run
    * `pyll.scope` is used to define range of type integer

2- define the objective function
3- define search space, use `hyperopt.hp`
4- pass the objective function and the search space to the `fmin` method, which will try to minimize the error

autologging

works with some frameworks (scikitlearn, lightgbm, xgboost, etc...), and simplifies the logging process. you may still want to log other information on your own

```python
params = {
    ...
}

mlflow.xgboost.autolog() # replace with mflow.start_run() with this line

booster = xgb.train(
    params=params,
    dtrain=train,
    num_boost_round=1000,
    evals=[(valid, "validation")],
    early_stopping_rounds=50
)

```

machine learning lifecycle

[link](https://neptune.ai/blog/ml-experiment-tracking)

simple method to save the model as an artifact

```python
mlflow.log_artifact(local_path="models/lin_reg.bin", artifact_path="models_pickle/")
```

alternatively, you can use this command:

```python
mlflow.xgboost.log_model(booster, artifact_path="models_mlflow")
```

```python
mlflow.xgboost.autolog(disable=True)

with mlflow.start_run():
    
    train = xgb.DMatrix(X_train, label=y_train)
    valid = xgb.DMatrix(X_val, label=y_val)

    best_params = {
        'learning_rate': 0.09585355369315604,
        'max_depth': 30,
        'min_child_weight': 1.060597050922164,
        'objective': 'reg:linear',
        'reg_alpha': 0.018060244040060163,
        'reg_lambda': 0.011658731377413597,
        'seed': 42
    }

    mlflow.log_params(best_params)

    booster = xgb.train(
        params=best_params,
        dtrain=train,
        num_boost_round=1000,
        evals=[(valid, 'validation')],
        early_stopping_rounds=50
    )

    y_pred = booster.predict(valid)
    rmse = mean_squared_error(y_val, y_pred, squared=False)
    mlflow.log_metric("rmse", rmse)

    with open("models/preprocessor.b", "wb") as f_out:
        pickle.dump(dv, f_out)
    mlflow.log_artifact("models/preprocessor.b", artifact_path="preprocessor")

    mlflow.xgboost.log_model(booster, artifact_path="models_mlflow")



from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.svm import LinearSVR

mlflow.sklearn.autolog()

for model_class in (RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, LinearSVR):

    with mlflow.start_run():

        mlflow.log_param("train-data-path", "./data/green_tripdata_2021-01.csv")
        mlflow.log_param("valid-data-path", "./data/green_tripdata_2021-02.csv")
        mlflow.log_artifact("models/preprocessor.b", artifact_path="preprocessor")

        mlmodel = model_class()
        mlmodel.fit(X_train, y_train)

        y_pred = mlmodel.predict(X_val)
        rmse = mean_squared_error(y_val, y_pred, squared=False)
        mlflow.log_metric("rmse", rmse)
```

model registry

train different models (lightgbm, randomforest, linear svr, extratrees)

once we conclude the experimentation phase (training and regsitering the models in mlflow registry), we move to the next phase in which we decide which models are ready for production. model registration takes place on the mlflow ui, and you can also stage the models you want to consider for production. 

for production, we use the MLFlowClient class. the client can interact with the experiments and the registry, where it can find specific runs

```python
# import mlflow client
from mlflow.tracking import MlflowClient


MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"

# initiate mlflow client
client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

client.list_experiments()

# create experiment
client.create_experiment(name="my-cool-experiment")

# search runs
from mlflow.entities import ViewType

runs = client.search_runs(
    experiment_ids='1',
    filter_string="metrics.rmse < 7",
    run_view_type=ViewType.ACTIVE_ONLY,
    max_results=5,
    order_by=["metrics.rmse ASC"]
)

# Interacting with the Model Registry
run_id = "b8904012c84343b5bf8ee72aa8f0f402"
model_uri = f"runs:/{run_id}/model"
mlflow.register_model(model_uri=model_uri, name="nyc-taxi-regressor")

# getting latest model version
model_name = "nyc-taxi-regressor"
latest_versions = client.get_latest_versions(name=model_name)

for version in latest_versions:
    print(f"version: {version.version}, stage: {version.current_stage}")

# staging
model_version = 4
new_stage = "Staging"
client.transition_model_version_stage(
    name=model_name,
    version=model_version,
    stage=new_stage,
    archive_existing_versions=False
)

# updating model version
from datetime import datetime

date = datetime.today().date()
client.update_model_version(
    name=model_name,
    version=model_version,
    description=f"The model version {model_version} was transitioned to {new_stage} on {date}"
)

# download artifact
client.download_artifacts(run_id=run_id, path='preprocessor', dst_path='.')

# compare models
def test_model(name, stage, X_test, y_test):
    model = mlflow.pyfunc.load_model(f"models:/{name}/{stage}")
    y_pred = model.predict(X_test)
    return {"rmse": mean_squared_error(y_test, y_pred, squared=False)}

%time test_model(name=model_name, stage="Production", X_test=X_test, y_test=y_test)

%time test_model(name=model_name, stage="Staging", X_test=X_test, y_test=y_test)

# transition to production
client.transition_model_version_stage(
    name=model_name,
    version=4,
    stage="Production",
    archive_existing_versions=True
)
```


mlflow in practice 

configuring mlflow:
    * backend store (local file, db)
    * artifact store (local, remote - s3)
    * tracking server (no tracking, localhost, remote)



training an xgboost classifier

```python
dv = DictVectorizer()

train_dicts = df_train[categorical + numerical].to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)
y_train = df_train['duration'].values

xgb_model = xgb.XGBClassifier(eta=eta, max_depth=depth, min_child_weight=child_weight, objective='binary:logistic', eval_metric='auc', random_state=42)        
xgb_model.fit(X_train, y_train)
```

```python
dv = DictVectorizer()

train_dicts = df_train[categorical + numerical].to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)
y_train = df_train['duration'].values

train = xgb.DMatrix(X_train, label=y_train)
booster = xgb.train(
    params=params,
    dtrain=train,
    num_boost_round=1000,
    evals=[(valid, 'validation')],
    early_stopping_rounds=50
)
```