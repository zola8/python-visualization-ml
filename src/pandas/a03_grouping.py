# Exercise 3: GroupBy & Aggregation (Medium)
import pandas as pd

data = {
    'Store': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Apple'],
    'Sales': [100, 150, 200, 100, 120, 130, 110, 210]
}

df = pd.DataFrame(data)

# print(df, "\n")


# Tasks:
# Group the data by Store and calculate the sum of Sales for each store.
# Group the data by Product and calculate the mean (average) Sales.
# Group by both Store and Product to see total sales per product per store.
# Reset the index of the result from Task 1 so Store becomes a column again.
if __name__ == '__main__':
    # Group the data by Store and calculate the sum of Sales for each store.
    print(df.groupby(by='Store')['Sales'].sum(), "\n")

    # Group the data by Product and calculate the mean (average) Sales.
    print(df.groupby('Product')['Sales'].mean(), "\n")

    # Group by multiple columns
    print(df.groupby(['Store', 'Product']).sum(), "\n")
    print(df.groupby(['Store', 'Product'])['Sales'].sum(), "\n")

    # Reset the index of the result from Task 1 so Store becomes a column again.
    df = df.groupby(by='Store')['Sales'].sum().reset_index()
    print(df, "\n")
