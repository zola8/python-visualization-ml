from datetime import datetime
import pandas as pd
import numpy as np


if __name__ == '__main__':
    today = datetime.today()
    print("today:     ", today)
    print("tomorrow:  ", today + pd.Timedelta(days=1))

    szuletett = datetime(2019,2,16)
    print("difference between 2 dates: ", today - szuletett)

    dates = ['2014-08-01','2014-08-02','2014-08-03','2014-08-04']
    time_series = pd.Series(np.random.randn(4), dates)
    print(time_series)
