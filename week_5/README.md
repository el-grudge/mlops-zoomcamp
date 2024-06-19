monitoring ml models in production
emeli dral 

performance of models in prod degrades with time 
monitor service health with metrics such as
    uptime, 
    memory usage, 
    latency
monitor model health with metrics such as 
    model accuracy (choice of metric depends on the problem, whether it's a ranking (ex. Normalized Discounted Cumulative Gain), classification (ex. Log Loss), or regression (ex. mean absolute error))
    model bias, especially in highly critical domains such health care or finance
    underperforming segments 
    outliers, especially when the cost of each individual error is high
    explainability
monitor data health with metrics such as 
    data quality and integriy (ex. categorical values proportions, missing / null values)
    broken pipelines / data outages, 
    schema change, 
    data drift (the statistical properties of the input data change over time) , 
    concept drift (the statistical properties of the target variable, or the relationship between the input features and the target variable change over time)

how to monitor?
    if you already have some monitoring architecture for service health, you can leverage those to monitor your ml model (ex. Prometheus / Grafana)
    use a bi tool to create a dashboard to monitor your model (ex. tableau / looker)


monitoring non-batch models (ex. a streaming / online model) can be more complicated, especially when calculating things like data drift and concept drift. 

the best way to tackle this issue is to use a window function (ex. moving window with / without moving reference) to break up the data into batches and compare those windows.




we created our environvment
requirements file and python libraries
docker compose image including services for monitoring application (postgres, adminer, grafana)
evidently metrics

DatasetCorrelationsMetric()