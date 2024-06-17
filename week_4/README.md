In week 4️⃣ of the MLOps Zoomcamp we learned about

📦🚀 Deployment

There are two ways a machine learning model can be deployed:
- 🕒 Batch / Offline: When regular runs at separate time intevals are sufficient. A normal use case would look something like this: 
    1- Get some data from a database
    2- Apply the model to it
    3- Write the predictions to another database
    4- Another application uses those predictions

    Ex. A churn model predicts when a user might stop using a service, and a marketing model uses that prediction to make an offer to retain user. 

- 🌐 Online: When a model needs to be up at all times. This can be done with a webservice or a streaming service.
    - A webservice deployment would look something like this: user uses app ➡️ app talks to backend ➡️ calls webservice ➡️ gets prediction
      Ex. A user of a ride hailing app gets a prediction on the trip trip duration.

    - A streaming deployment would involve producer(s) and consumer(s). It would look something like this: producer pushes some events ➡️ consumer listens to stream ➡️ consumer gets event ➡️ does something with it

Here's a guide of how to deploy a model as a webservice:  
    1- Create a virtual environment to install dependencies. Use `pip freeze` to get the package versions there were used when training the model, and install them in the virtual environment.   
    2- Wrap the predict function in an api (use either fastapi or flask).  
    3- Containarize the environment and the artifacts with docker. Make sure to use a production ready webservice (ex. gunicorn) when deploying the webservice in production. Some useful docker commands:  
    
```shell
# to build a docker image. 
docker build -t image_name:v001 -f image.dockerfile .
```

```shell 
# to run in interactive mode and access the image's bash. Useful for debugging
docker run -it image_name:v001 /bin/bash
```

```shell 
# use the -p option to bind the image to a port to access the webservice
docker run -it --rm -p 9696:9696 image_name:v001
```

🛠️ Web-services: Getting the models from an MLflow model registry
    - MLflow can be used to track the model run and to save artifacts (ex. model binary, data preparation function). Alternatively, a scikit-learn pipeline can be used to deal with less artifacts.
    - To avoid relying on the MLFlow tracking service and possibly creating a bottleneck consider connecting MLflow to a cloud bucket and use the model from that bucket instead.

🚀 Deploying a model
In the weekly project we built an I created a flask app for my duration prediction model and built a docker container around it so it can be deployed as a webservice. You can view the code [here](https://github.com/el-grudge/mlops-zoomcamp/tree/main/week_4).

#mlops_zoomcamp #ochestration #deployment #flask #machine_learning #docker #learning_in_public
