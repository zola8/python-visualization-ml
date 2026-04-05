import pandas as pd
from sklearn.impute import SimpleImputer

from global_common import score_dataset


def drop_columns_with_missing_values(model, X_train, X_valid, y_train, y_valid, debug=True):
    if debug:
        print('--- Drop columns with missing values \n')

    # Number of missing values in each column of training data
    missing_val_count_by_column = (X_train.isnull().sum())

    if debug:
        print("Missing values by columns:")
        print(missing_val_count_by_column[missing_val_count_by_column > 0], "\n")

    # get names of columns with missing values
    cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]

    # Fill in the lines below: drop columns in training and validation data
    reduced_X_train = X_train.drop(cols_with_missing, axis=1)
    reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

    mae = score_dataset(model, reduced_X_train, reduced_X_valid, y_train, y_valid)
    if debug:
        print("MAE (Drop columns with missing values):", mae)
    return mae


def imputation_mean(model, X_train, X_valid, y_train, y_valid, debug=True):
    if debug:
        print('\n--- Imputation (mean) \n')

    # imputation
    mean_imputer = SimpleImputer(strategy="mean")
    imputed_X_train = pd.DataFrame(mean_imputer.fit_transform(X_train))
    imputed_X_valid = pd.DataFrame(mean_imputer.transform(X_valid))

    # imputation removed column names; put them back
    imputed_X_train.columns = X_train.columns
    imputed_X_valid.columns = X_valid.columns

    mae = score_dataset(model, imputed_X_train, imputed_X_valid, y_train, y_valid)
    if debug:
        print("MAE (Imputation):", mae)
    return mae


def imputation_median(model, X_train, X_valid, y_train, y_valid, debug=True):
    if debug:
        print('\n--- Imputation (median) \n')

    # Imputation
    median_imputer = SimpleImputer(strategy='median')
    final_X_train = pd.DataFrame(median_imputer.fit_transform(X_train))
    final_X_valid = pd.DataFrame(median_imputer.transform(X_valid))

    # Imputation removed column names; put them back
    final_X_train.columns = X_train.columns
    final_X_valid.columns = X_valid.columns

    mae = score_dataset(model, final_X_train, final_X_valid, y_train, y_valid)
    if debug:
        print("MAE (median approach):", mae)
    return mae
