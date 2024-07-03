import pandas as pd
from datetime import datetime

from batch import prepare_data


def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)


def test_prepare_data():
    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2), dt(1, 10)),
        (1, 2, dt(2, 2), dt(2, 3)),
        (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)

    # Define the expected output and use the assert to make sure that the actual dataframe matches the expected one
    categorical = ['PULocationID', 'DOLocationID']
    df_actual = prepare_data(df, categorical)

    data_expected = [
            ('-1', '-1', dt(1, 2), dt(1, 10), 8.0),
            ('1',  '-1', dt(1, 2), dt(1, 10), 8.0),
            ('1', '2', dt(2, 2), dt(2, 3), 1.0),
        ]

    df_expected = pd.DataFrame(data_expected, columns=columns+['duration'])

    assert df_actual.equals(df_expected)