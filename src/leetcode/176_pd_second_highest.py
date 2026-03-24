import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if N <= 0:
        n_highest = None
    elif len(unique_salaries) >= N:
        n_highest = unique_salaries.iloc[N-1]
    else:
        n_highest = None

    return pd.DataFrame({f'getNthHighestSalary({N})': [n_highest]})


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(unique_salaries) >= 2:
        second_highest = unique_salaries.iloc[1]
    else:
        second_highest = None

    return pd.DataFrame({'SecondHighestSalary': [second_highest]})


# https://leetcode.com/problems/second-highest-salary/description/
if __name__ == '__main__':
    employee_data = {
        'id': [1, 2, 3],
        'salary': [100, 200, 300],
    }
    employee_df = pd.DataFrame(employee_data)

    print(nth_highest_salary(employee_df, 0))
