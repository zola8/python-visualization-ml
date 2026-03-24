# Merging & Cleaning (Medium-Hard)
import pandas as pd
import numpy as np

# Customers Table
customers = {
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Country': ['USA', 'UK', 'USA', 'Germany']
}
df_customers = pd.DataFrame(customers)

# Orders Table (Note: CustomerID 5 does not exist in customers, and CustomerID 3 has no orders)
orders = {
    'OrderID': [101, 102, 103, 104],
    'CustomerID': [1, 2, 5, 1],
    'Amount': [200, 500, 100, 300]
}
df_orders = pd.DataFrame(orders)


# Tasks:
# Merge the two DataFrames on CustomerID. Use a left join (keep all customers, even if they have no orders).
# Fill any missing Amount values (NaN) with 0.
# Create a new column Status: If Amount > 0, set to 'Active', otherwise 'Inactive'.
# Drop the CustomerID column from the final result (keep it only for merging).

if __name__ == '__main__':
    print("", "\n")

    # Merge the two DataFrames on CustomerID. Use a left join (keep all customers, even if they have no orders).
    merged = pd.merge(df_customers, df_orders, on='CustomerID', how='left')
    print(merged, "\n")

    # Fill any missing Amount values (NaN) with 0.
    merged['Amount'] = merged['Amount'].fillna(0)
    print(merged, "\n")

    # Create a new column Status: If Amount > 0, set to 'Active', otherwise 'Inactive'.
    merged['Status'] = np.where(merged['Amount'] > 0, 'Active', 'Inactive')
    print(merged, "\n")

    # merged.drop('CustomerID', axis=1, inplace=True)
    merged = merged.drop(columns='CustomerID')
    print(merged, "\n")
