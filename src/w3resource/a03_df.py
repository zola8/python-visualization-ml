import numpy as np
import pandas as pd

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

if __name__ == '__main__':
    df = pd.DataFrame(exam_data, index=labels)
    print(df, "\n")

    print("First three rows of the data frame:")
    print(df.iloc[:3], "\n")

    print("Selecting 'name' and 'score' Columns")
    print(df[['name', 'score']], "\n")

    print("Selecting 'a' and 'b' rows")
    print(df.iloc[[0, 1],], "\n")

    print("Selecting 'b' row and 'qualify' column")
    print(df.iloc[[1], [3]], "\n")

    print("Selecting Rows Where Attempts > 2")
    print(df[df['attempts'] > 2], "\n")

    print("qualify: yes")
    print(df[df['qualify'] == "yes"], "\n")

    print("Counting Rows and Columns")
    total_rows = len(df.axes[0])
    total_cols = len(df.axes[1])
    print("Number of Rows: " + str(total_rows))
    print("Number of Columns: " + str(total_cols), "\n")

    print("Rows where score is missing:")
    print(df[df['score'].isnull()], "\n")

    print("Selecting Rows with Attempts < 2 and Score > 15")
    print(df[(df['attempts'] < 2) & (df['score'] > 15)], "\n")

    print("Summing Examination Attempts")
    print(df['attempts'].sum(), "\n")

    print("Append a new row:")
    df.loc['k'] = ['Suresh', 15.5, 1, 'yes']
    print(df, "\n")

    print("Delete a row:")
    df.drop('k', inplace=True)
    print(df, "\n")

    print("Insert a column:")
    color = ['Red', 'Blue', 'Orange', 'Red', 'White', 'White', 'Blue', 'Green', 'Green', 'Red']
    df['color'] = color
    print(df, "\n")

    print("Delete a column:")
    df.drop('color', axis=1, inplace=True)
    print(df, "\n")
