import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

ordinal_encoder = OrdinalEncoder()
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)


def approach_1_drop_categorical_variables(X_train, X_valid):
    new_X_train = X_train.select_dtypes(exclude=['str'])
    new_X_valid = X_valid.select_dtypes(exclude=['str'])
    return new_X_train, new_X_valid


def approach_2_ordinal_encoding(X_train, X_valid, debug=True):
    object_cols = [cname for cname in X_train.columns if X_train[cname].dtype == 'str']

    good_label_cols = [col for col in object_cols if
                       set(X_valid[col]).issubset(set(X_train[col]))]
    good_label_cols.remove('Condition1')

    # Problematic columns that will be dropped from the dataset
    bad_label_cols = list(set(object_cols) - set(good_label_cols))

    if debug:
        print('Categorical columns that will be ordinal encoded:', good_label_cols)
        print('Categorical columns that will be dropped from the dataset:', bad_label_cols)

    # Drop categorical columns that will not be encoded
    label_X_train = X_train.drop(bad_label_cols, axis=1)
    label_X_valid = X_valid.drop(bad_label_cols, axis=1)

    # Apply ordinal encoder to each column with categorical data
    label_X_train[good_label_cols] = ordinal_encoder.fit_transform(label_X_train[good_label_cols])
    label_X_valid[good_label_cols] = ordinal_encoder.transform(label_X_valid[good_label_cols])

    return label_X_train, label_X_valid


def approach_3_one_hot_encoding(X_train, X_valid):
    object_cols = [cname for cname in X_train.columns if X_train[cname].dtype == 'str']

    # Apply one-hot encoder to each column with categorical data
    OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols]))
    OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[object_cols]))

    # One-hot encoding removed index; put it back
    OH_cols_train.index = X_train.index
    OH_cols_valid.index = X_valid.index

    # Remove categorical columns (will replace with one-hot encoding)
    num_X_train = X_train.drop(object_cols, axis=1)
    num_X_valid = X_valid.drop(object_cols, axis=1)

    # Add one-hot encoded columns to numerical features
    OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
    OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

    # Ensure all columns have string type
    OH_X_train.columns = OH_X_train.columns.astype(str)
    OH_X_valid.columns = OH_X_valid.columns.astype(str)

    return OH_X_train, OH_X_valid
