import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from global_categorical_variables import approach_1_drop_categorical_variables, approach_2_ordinal_encoding, approach_3_one_hot_encoding
from global_handle_missing_values import drop_columns_with_missing_values, imputation_mean, imputation_median
from global_print_statistics import print_model_statistics

if __name__ == '__main__':
    # Load data
    X_full = pd.read_csv('../input/train.csv', index_col='Id')
    X_test_full = pd.read_csv('../input/test.csv', index_col='Id')

    # Select target
    print('Select target: SalePrice')
    y = X_full.SalePrice

    # Select features: Remove rows with missing target, separate target from predictors
    print('Select features: Remove rows where missing values are in SalePrice. \n')
    X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
    X_full.drop(['SalePrice'], axis=1, inplace=True)

    # print_column_statistics(X_full)

    X_train, X_valid, y_train, y_valid = train_test_split(X_full, y, train_size=0.8, test_size=0.2, random_state=0)

    #########################################################

    # model_1 = ('model_1', DecisionTreeRegressor(max_depth=5, random_state=1))
    # model_2 = ('model_2', DecisionTreeRegressor(max_leaf_nodes=100, random_state=1))
    model_3 = ('model_3', RandomForestRegressor(random_state=1))
    model_4 = ('model_4', RandomForestRegressor(n_estimators=50, random_state=0))
    model_5 = ('model_5', RandomForestRegressor(n_estimators=100, random_state=0))
    # model_6 = ('model_6', RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0))
    # model_7 = ('model_7', RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0))
    # model_8 = ('model_8', RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0))
    mae_results = {}

    # models = []
    models = [model_3, model_4, model_5]
    # model_1, model_2, model_6, model_7, model_8,, model_5

    print('Model training ... started')

    for model_name, model in models:
        # Approach 1 (Drop Categorical Variables) = numerical only
        new_X_train, new_X_valid = approach_1_drop_categorical_variables(X_train, X_valid)

        mae1 = drop_columns_with_missing_values(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae2 = imputation_mean(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae3 = imputation_median(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae_results[(model_name, 'Drop column where missing value', 'Drop Categorical Variables')] = mae1
        mae_results[(model_name, 'Imputation with Mean', 'Drop Categorical Variables')] = mae2
        mae_results[(model_name, 'Imputation with Median', 'Drop Categorical Variables')] = mae3

        # Approach 2 (Ordinal Encoding)
        new_X_train, new_X_valid = approach_2_ordinal_encoding(X_train, X_valid, debug=False)

        mae1 = drop_columns_with_missing_values(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae2 = imputation_mean(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae3 = imputation_median(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae_results[(model_name, 'Drop column where missing value', 'Ordinal Encoding')] = mae1
        mae_results[(model_name, 'Imputation with Mean', 'Ordinal Encoding')] = mae2
        mae_results[(model_name, 'Imputation with Median', 'Ordinal Encoding')] = mae3

        # Approach 3 (One-Hot Encoding)
        new_X_train, new_X_valid = approach_3_one_hot_encoding(X_train, X_valid)

        mae1 = drop_columns_with_missing_values(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae2 = imputation_mean(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae3 = imputation_median(model, new_X_train, new_X_valid, y_train, y_valid, debug=False)
        mae_results[(model_name, 'Drop column where missing value', 'One-Hot Encoding')] = mae1
        mae_results[(model_name, 'Imputation with Mean', 'One-Hot Encoding')] = mae2
        mae_results[(model_name, 'Imputation with Median', 'One-Hot Encoding')] = mae3

        print('Model:', model_name, '... completed')

    print()
    print_model_statistics(mae_results)

    #########################################################

    # Generate test predictions
    # print('\n--- Generate test predictions \n')
    #
    # final_X_test = pd.DataFrame(median_imputer.transform(X_test))
    # final_X_test.columns = X_test.columns
    #
    # preds_test = model.predict(final_X_test)

    # Save test predictions to file
    # output = pd.DataFrame({'Id': X_test.index, 'SalePrice': preds_test})
    # output.to_csv('submission.csv', index=False)

    # print('submission.csv saved')
