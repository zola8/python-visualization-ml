import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 29],
    'City': ['New York', 'London', 'Tokyo', 'New York', 'London'],
    'Salary': [50000, 60000, 75000, 65000, 55000]
}

df = pd.DataFrame(data)

# Tasks:
# Display the first 3 rows of the DataFrame.
# Select only the Name and Salary columns.
# Filter the DataFrame to show only people who live in 'London'.
# Find the maximum salary in the dataset.
print("", "\n")

if __name__ == '__main__':
    # Display the first 3 rows of the DataFrame.
    print(df.head(3), "\n")

    # Select only the Name and Salary columns.
    print(df[['Name', 'Salary']], "\n")

    # Filter the DataFrame to show only people who live in 'London'.
    print(df[df['City'] == 'London'], "\n")

    # Find the maximum salary in the dataset.
    print(df['Salary'].max(), "\n")
