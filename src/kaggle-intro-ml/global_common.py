from sklearn.metrics import mean_absolute_error


def score_dataset(model, X_train, X_valid, y_train, y_valid):
    model.fit(X_train, y_train)
    predictions = model.predict(X_valid)
    return mean_absolute_error(y_valid, predictions)
