from mlops.utilities.logging import track_experiment
from mlops.utilities.models.model_training import load_class, train_model

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def training(
    training_set,
    model_class_name,
    *args,
    **kwargs,
):
    # Specify your transformation logic here
    mlmodel_class = load_class(model_class_name)
    X_train, X_val, y_train, y_val, dv = training_set['build']

    model, metrics, y_pred = train_model(
        mlmodel_class(),
        X_train,
        y_train,
        X_val,
        y_val,
        callback=lambda **opts: track_experiment(**{**opts, **kwargs}),
        random_state=42,
    )

    return model, metrics, y_pred, dv
