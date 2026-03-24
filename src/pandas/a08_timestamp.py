import pandas as pd

if __name__ == '__main__':
    date1 = pd.Timestamp('2019-01-01', tz='Europe/Berlin')
    print(date1)
    print(date1.tz_localize(None))
