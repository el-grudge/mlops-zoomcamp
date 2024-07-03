import os
import pandas as pd
from datetime import datetime

import batch

def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)


columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
data = [
    (None, None, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2), dt(1, 10)),
    (1, 2, dt(2, 2), dt(2, 3)),
    (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
    (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
]
df_input = pd.DataFrame(data, columns=columns)

input_file = batch.get_input_path(2022, 1)
output_file = batch.get_output_path(2022, 1)

S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL', 'http://localhost:4566')
options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL
    }
}

df_input.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)

os.system('python batch.py 2022 01')


df_actual = pd.read_parquet(output_file, storage_options=options)
print(df_actual['predicted_duration'].sum())