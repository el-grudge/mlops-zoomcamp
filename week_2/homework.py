import subprocess
import mlflow
import mlflow.sklearn

# Question 1
# pip install mlflow
result = subprocess.run(['mlflow', '--version'], capture_output=True, text=True, check=True)
# Print the output
print("MLflow version:", result.stdout.strip())

# Question 2
# Download the data
url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2023-'
subprocess.run(['wget', f'{url}01.parquet', '-O', 'data'], check=True)
subprocess.run(['wget', f'{url}02.parquet', '-O', 'data'], check=True)
subprocess.run(['wget', f'{url}03.parquet', '-O', 'data'], check=True)
# Run the preprocessing script
command = ['python', 'preprocess_data.py', '--raw_data_path', './data', '--dest_path', './output']
subprocess.run(command, check=True)

# Count files in output 
command = 'ls output | wc -l'
result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
print(int(result.stdout.strip()))

# Question 3
# Set the MLflow tracking URI if needed (replace with your own URI if it's not the default local one)
# mlflow.set_tracking_uri("http://your_tracking_server")
command = ['python', 'train.py']
subprocess.run(command, check=True)

# Replace 'your_run_id' with the actual run ID of your model
run_id = '78749850cfe7408a8b0babc9d9c02a33'

# Load the model from MLflow
MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
model_uri = f"runs:/{run_id}/model"
model = mlflow.sklearn.load_model(model_uri)

# Retrieve the min_samples_split parameter value
min_samples_split_value = model.get_params()['min_samples_split']
print(f"The value of min_samples_split is: {min_samples_split_value}")

# Question 4
command = ['mlflow','ui','--backend-store-uri','sqlite:///mlflow.db','--default-artifact-root','./mlruns']
process = subprocess.Popen(command)

# Question 5
command = ['python','hpo.py']
subprocess.run(command, check=True)
# Using the mlflow dashboard, the answer to the question is: 5.335

# Question 6
command = ['python','register_model.py']
subprocess.run(command, check=True)
# Using the mlflow dashboard, the answer to the question is: 5.567