In week 2️⃣ of the MLOps Zoomcamp we learned about

Experiment tracking
Is the process of tracking all the relevant information of an ML experiment. Deciding which inforamtion to track can vary from role to role, a data scientist might be more interested in tracking the hyperparameters, while a data engineer might be more interested in tracking the training data. Tracking the source code, environment, data, model, hyperparameters, and metrics is usually a good practice. Tracking is important for reproducibility, organization, and optimization

MLFlow
Is an open source platform for managing the machine learning lifecycle. It contains four main modules: 
* tracking - focuses on experiment tracking, allows you to log and query experiments, metrics, parameters, and artifacts related to machine learning models. It helps in tracking the performance of models and experiments, facilitating reproducibility, and collaboration among teams. 
* models - functionality for saving, loading, and deploying models in a standardized format. This module allows you to package machine learning models along with their associated metadata, enabling easy sharing, reproducibility, and deployment across different environments
* model registry - useful for managing models. It offers capabilities for versioning, staging, and annotating models, making it easier to organize, track, and deploy models in production environments.
* projects - MLflow Projects is a component of MLflow that enables you to package data science code in a reusable and reproducible way. An MLflow project is a format for organizing and running data science code. It allows you to specify dependencies, parameters, and scripts, making it easy to share and run your code across different environments.

MLFlow tracks experiments runs and keeps track of 
* parameters - the parameters used for training the model, it can also track preprocessing steps used to prepare the data for training 
* metrics - any evaluation metric, such as accuracy, can track training, val, test metrics
* metadata - information related to the experiemnt, such as type of algorithm 
* artifacts - any files related to the model, including the data (though this won't scale well, and can result in data duplication)
* models - the model itself

mlflow demo 
- mlflow ui - launhces the mlflow tracking ui for local viewing of experiment runs 


installing mlflow
    pip install 
    launch mlflow ui with --backend-store-uri sqlite:///mlflow.db option 
add mlflow to jupyter notebook
    set_tracking_uri("sqlite:///mlflow.db")
    set_experiment("experiment-name")
    mlflow.start_run
        set_tag() - developer name
        log_param() - logs hyperparameters and any info you consider relevant to model's performance
        log_metric() - logs the metric used to assess the model
visualize in mlflow ui  

experiment tracking with more parameters 
    hyperopt xgboost 
        fmin - minimize output of function 
        tpe - algo that control training loging 
        hp - library containing methods to define search space
        status_ok - signal sent at the end of each run  
        trails - tracks info of each run 
    visualizations 
        parallel coordinates plot 
        scatter plot 
        contour plot
select best performing model: consider metric performance, size, time, complexity
autologging: simplifies the logging process for certain model types (xgboost, lightgbm, tensorflow, pytorch, and others)

model management: 
    experiment tracking, model versioning, model deployment

model registry: 
    deploying new model:
        - questions an ml eng might ask: what changed? new hyperparameters? any preprocessing? what is the env, dependencies, new versions?
        - tracking experiments with mlflow: as we track more models a time will come when we need to decide which ones are ready for production. for this, we can use mlflow's model registry. the data scientist is not responsible for deploying a model, they're only charged with deciding which ones are ready for production. it is the ml engineer responsibility to inspect the models in the registry and make a decision based on the model's performance, its hyperparameters, and its the size. after assessing the models in the registry, the ml eng can move the model from staging to production or archive