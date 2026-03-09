# https://www.w3resource.com/python-exercises/pandas/groupby/python-pandas-groupby-exercise-8.php
import pandas as pd

orders_data = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10',
                 '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})


def print_sorted():
    print("Sorted orders:")
    print(orders_data.sort_values('ord_no'), "\n")


def print_grouped():
    print("Grouped orders: \n")
    grouped_df = orders_data.groupby('customer_id')
    for key, item in grouped_df:
        print(item, "\n")


def print_grouped_sum():
    print("Grouped orders + sum: \n")
    grouped_df = orders_data.groupby('customer_id')
    for key, item in grouped_df:
        print(f"Customer id: {key}, Total orders: {item['purch_amt'].sum()}")
    df = grouped_df["purch_amt"].sum().reset_index()
    print(df, "\n")
    

def print_cheapest_amount_per_customer():
    print("Cheapest order per customer: \n")
    grouped_df = orders_data.groupby('customer_id')
    df = grouped_df["purch_amt"].min().reset_index()
    print(df, "\n")


if __name__ == '__main__':
    # print_sorted()
    # print_grouped()
    print_grouped_sum()
    # print_cheapest_amount_per_customer()
