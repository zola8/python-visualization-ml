import pandas as pd


def get_last_business_days(year):
    """
    Create a Pandas time series with the last working days (weekdays) of each month
    for a specific year using 'BM' frequency (business month end).
    """
    # Generate the time series directly
    dates = pd.date_range(start=f'{year}-01-01', periods=12, freq='BME')
    return pd.Series(dates, name='Last Business Day')


if __name__ == '__main__':
    dates = pd.Series(pd.date_range('2020-12-01',periods=31, freq='D'))
    print("Month of December 2020:")
    print(dates)

    dates = pd.Series(pd.date_range('2020-12-01',periods=31, freq='D'))
    print("\nMaximum date: ", dates.max())
    print("Minimum date: ", dates.min())
    print("Maximum index: ", dates.idxmax())
    print("Minimum index: ", dates.idxmin())

    print("\nLast working days of each month:\n", get_last_business_days('2026'))
