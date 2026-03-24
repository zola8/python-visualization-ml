# https://www.w3resource.com/python-exercises/pandas/python-pandas-data-frame-exercise-21.php
# https://www.w3resource.com/python-exercises/pandas/index-dataframe.php

import pandas as pd


if __name__ == '__main__':
    exam_data = [{'name': 'Anastasia', 'score': 12.5}, {'name': 'Dima', 'score': 9}, {'name': 'Katherine', 'score': 16.5}]
    df = pd.DataFrame(exam_data)

    # Iterate over rows in a DataFrame
    for index, row in df.iterrows():
        print(row['name'], row['score'])
    print("\n")

    # Selecting Rows Based on Column Values
    d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
    df = pd.DataFrame(data=d)

    print('Rows for colum1 value == 4')
    print(df.loc[df['col1'] == 4])
