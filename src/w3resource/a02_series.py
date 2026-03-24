import pandas as pd

if __name__ == '__main__':
    ds1 = pd.Series([2, 4, 6, 8, 10])
    ds2 = pd.Series([1, 3, 5, 7, 10])

    ds = ds1 + ds2
    print("Add two Series:")
    print(ds, "\n")

    print("Subtract two Series:")
    ds = ds1 - ds2
    print(ds, "\n")

    print("Multiply two Series:")
    ds = ds1 * ds2
    print(ds, "\n")

    print("Divide Series1 by Series2:")
    ds = ds1 / ds2
    print(ds, "\n")

    print("Compare the elements of the said Series:")
    print("Equals:")
    print(ds1 == ds2, "\n")

    print("Greater than:")
    print(ds1 > ds2, "\n")

    print("Less than:")
    print(ds1 < ds2, "\n")
