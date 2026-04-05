def print_column_statistics(X):
    print('--- Column statistics --- \n')
    numerical_cols = [col for col in X.columns if X[col].dtype in ['int64', 'float64']]
    print(f"numerical cols: {len(numerical_cols)}:", numerical_cols)
    obj_cols = [cname for cname in X.columns if X[cname].dtype == 'object']
    print(f"object cols: {len(obj_cols)}:", obj_cols)

    # print('\nColumn data types and nr. of values:')
    # for col in X.columns:
    #     print(f"Col: {col}, data type: {X[col].dtype}, unique elements: {X[col].nunique()}")

    cols_with_missing = [col for col in X.columns if X[col].isnull().any()]
    print('\nMissing values from these columns:', cols_with_missing)

    print("\n")


def print_model_statistics(mae_results):
    print('--- Model statistics --- \n')
    model_stats = sorted(mae_results.items(), key=lambda x: x[1], reverse=False)

    # Define column widths
    col_width_model = 10
    col_width_strategy = 35
    col_width_variables = 35
    col_width_score = 15

    # Print Header
    print(
        f"{'Rank':<5} {'Model':<{col_width_model}} {'Missing Value Strategy':<{col_width_strategy}} {'Categorical variable handling':<{col_width_variables}} {'MAE Score':>{col_width_score}}")
    print("-" * (5 + col_width_model + col_width_score + col_width_strategy + col_width_variables + 5))

    # Print Rows
    for rank, ((current_model, strategy, variables), score) in enumerate(model_stats, 1):
        print(
            f"{rank:<5} {current_model:<{col_width_model}} {strategy:<{col_width_strategy}} {variables:<{col_width_variables}} {score:>{col_width_score}.2f}")
