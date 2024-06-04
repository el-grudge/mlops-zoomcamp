In week 2️⃣ of the MLOps Zoomcamp we learned about

📈 Experiment tracking
Is the process of tracking all the relevant information of an ML experiment. Deciding which inforamtion to track can vary from role to role, a data scientist might be more interested in tracking the hyperparameters, while a data engineer might be more interested in tracking the training data. Tracking the source code, environment, data, model, hyperparameters, and metrics is usually a good practice. Tracking is important for reproducibility, organization, and optimization

🛠️ MLFlow
Is an open source platform for managing the machine learning lifecycle. It contains four main modules:
* 📊 Tracking - Focuses on experiment tracking, allows you to log and query experiments, metrics, parameters, and artifacts related to machine learning models. It helps in tracking the performance of models and experiments, facilitating reproducibility, and collaboration among teams. 
* 📦 Models - Provides functionality for saving, loading, and deploying models in a standardized format. This module allows you to package machine learning models along with their associated metadata, enabling easy sharing, reproducibility, and deployment across different environments
* 🗂️ Model Registry - Useful for managing models. It offers capabilities for versioning, staging, and annotating models, making it easier to organize, track, and deploy models in production environments.
* 📁 Projects - MLflow Projects is a component of MLflow that enables you to package data science code in a reusable and reproducible way. An MLflow project is a format for organizing and running data science code. It allows you to specify dependencies, parameters, and scripts, making it easy to share and run your code across different environments.

MLFlow tracks experiments runs and keeps track of 
* 🔧 Parameters - The parameters used for training the model, it can also track preprocessing steps used to prepare the data for training 
* 📈 Metrics - Any evaluation metric, such as accuracy, can track training, val, test metrics
* 📝 Metadata - Information related to the experiemnt, such as type of algorithm 
* 📂 Artifacts - any files related to the model, including the data (though this won't scale well, and can result in data duplication)
* 🤖 Models - the model itself

#mlops_zoomcamp #mlflow #tracking_experiments #mlops #machine_learning #learning_in_public