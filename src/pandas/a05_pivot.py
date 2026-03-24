# Exercise 5: Time Series & Pivot Tables (Hard)
# Goal: Work with dates, resampling, and pivot tables.
import numpy as np
import pandas as pd

# Generate 100 days of data
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
data = {
    'Date': dates,
    'Store': ['North', 'South'] * 50,  # Alternating stores
    'Revenue': np.random.randint(1000, 5000, size=100)  # Random revenue
}
df = pd.DataFrame(data)

# Tasks:
# Set the Date column as the Index of the DataFrame.
# Resample the data to calculate the total Revenue per Month ('M').
# Create a Pivot Table showing Revenue summed by Store (columns) and Month (index). Hint: You may need to extract the Month from the Date index first.
# Find the rolling average (window=3) of the total monthly revenue.

if __name__ == '__main__':
    # Set the Date column as the Index of the DataFrame.
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure it's datetime object
    df = df.set_index('Date')
    print(df, "\n")

    # Resample the data to calculate the total Revenue per Month ('M').
    monthly_revenue = df['Revenue'].resample('ME').sum()
    print("Monthly Revenue:\n", monthly_revenue, "\n")

    # Create a Pivot Table showing Revenue summed by Store (columns) and Month (index).
    df['Month'] = df.index.to_period('M')
    pivot = pd.pivot_table(df, values='Revenue', index='Month', columns='Store', aggfunc='sum')
    print("Pivot Table:\n", pivot, "\n")

    # Find the rolling average (window=3) of the total monthly revenue.
    rolling_avg = monthly_revenue.rolling(window=3).mean()
    print("Rolling Average (3 Months):\n", rolling_avg, "\n")
