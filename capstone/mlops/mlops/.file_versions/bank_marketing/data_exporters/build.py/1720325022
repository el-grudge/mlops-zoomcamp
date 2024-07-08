from typing import Tuple
from pandas import DataFrame, Series

from mlops.utilities.data_preparation.encoders import vectorize_features

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_exporter
def export(data: Tuple[DataFrame, DataFrame, Series, Series], *args, **kwargs):
    X_train, X_val, y_train, y_val = data
    
    X_train, X_val, dv = vectorize_features(X_train, X_val)
    
    return X_train, X_val, y_train, y_val, dv