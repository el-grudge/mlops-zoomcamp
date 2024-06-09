In week 3️⃣ of the MLOps Zoomcamp we learned about

💇‍♀️ Orchestration and ML Pipelines with Mage  

Mage is an open source data orchestration tool. It provides a notebook-like interface that makes it easy to build, run, and debug ML pipelines. Below are some of the features that make Mage a useful tool when building ML pipelines:

* 📂 Projects: It is now easy to create and manage multiple projects within Mage  
* 🌐 GDP: When building an ML pipeline in Mage, storing the training data set as a global data product can make it easy to experiment with multiple models without having to prepare the data for each one.
* 🔀 Dynamic blocks: Dynamic blocks create multiple downstream blocks. This is useful when training multiple models, that way the models can be trained concurrently.
* 📊 Charts: Use charts and dashboards to monitor pipeline performance. Also, creating custom charts makes it easy to monitor model performances and compare performances across different models.
* 🔔 Alerts: Setup alerts in the project's metdata to receive email alerts on failed, delayed, and successful runs.

🪄 Orchestration + MLFlow
In the homework we built an ML pipeline in Mage. The pipeline trained a simple linear regression model and logged its performance in MLFlow. You can view the code [here](https://github.com/el-grudge/mlops-zoomcamp/tree/main/week_3).

#mlops_zoomcamp #ochestration #ml_pipelines #mlops #machine_learning #mage #learning_in_public