In week 5️⃣ of the MLOps Zoomcamp we learned about

🔍🤖 Monitoring ML Models in Production 

* ⏳🛠️ Performance of ML models in production degrades with time, and the right monitoring will allow us to intervene in time.
* First, monitor service health with metrics like:
    - ⏱️ uptime
    - 🧠 memory usage 
    - 🕒 latency
* Second, monitor model health with metrics like: 
    - 📊✔️ model accuracy (choice of metric depends on the problem, whether it's a ranking (ex. Normalized Discounted Cumulative Gain), classification (ex. Log Loss), or regression (ex. mean absolute error))
    - ⚖️🏥💰 model bias, especially in highly critical domains such health care or finance
    - 📉 underperforming segments 
    - 📈⚠️ outliers, especially when the cost of each individual error is high
    - 🗣️🔍 explainability
* Third, monitor data health with metrics like: 
    - 🏷️📉 data quality and integriy (ex. categorical values proportions, missing / null values)
    - 🚧🚫 broken pipelines / data outages, 
    - 📋🔄 schema change, 
    - 🔄📊 data drift (the statistical properties of the input data change over time) , 
    - 🔄📉 concept drift (the statistical properties of the target variable, or the relationship between the input features and the target variable change over time)

* How to monitor?
    - 🛠️📈 if you already have some monitoring architecture for service health, you can leverage those to monitor your ml model (ex. Prometheus / Grafana)
    - 📊🖥️ use a bi tool to create a dashboard to monitor your model (ex. tableau / looker)

* 🌊🗂️ Monitoring non-batch models (ex. a streaming / online model) can be more complicated, especially when calculating things like data drift and concept drift. The best way to tackle this issue is to use a window function (ex. moving window with / without moving reference) to break up the data into batches and compare those windows.

Emeli Dral showed us how to setup a monitoring service using evidently.ai and Grafana. Here's a simple guide:
1- 🖥️ Created a virtual environvment
2- 🐍📦 Install python libraries
3- 🐳⚙️ Create a docker compose yml to run the services that will be needed for the monitoring application (postgres, adminer, grafana)
4- 📊🔧 Use evidently.ai metrics to monitor column drift, dataset drift, dataset missing values, column quantiles, dataset correlations, and much more (you can learn more about the available metrics [here](https://docs.evidentlyai.com/reference/all-metrics#data-quality))

📝🔍 Monitoring a production model
In the weekly project we built a monitoring dashboard using evidently and Grafana and looked at multiple metrics from our trip duration model, including the fare amount 50th quantile. You can view the code [here](https://github.com/el-grudge/mlops-zoomcamp/tree/main/week_5).

#mlops_zoomcamp #monitoring #evidently #grafana #machine_learning #docker #learning_in_public
