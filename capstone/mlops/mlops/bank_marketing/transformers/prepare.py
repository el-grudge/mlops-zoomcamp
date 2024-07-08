from mlops.utilities.data_preparation.prepare_data import prepare_data
from mlops.utilities.data_preparation.transform_data import transform_data


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(data, *args, **kwargs):
    X_train, X_val, y_train, y_val = prepare_data(data)
    # transform data 
    X_train, X_val = transform_data(X_train), transform_data(X_val)
    
    return X_train, X_val, y_train, y_val