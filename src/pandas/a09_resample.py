import pandas as pd
import numpy as np

if __name__ == '__main__':
    date_rng = pd.date_range(start='2023-01-01', end='2023-01-05', freq='H')
    ts = pd.Series(np.random.randn(len(date_rng)), index=date_rng)

    ts_daily = ts.resample('D').mean()

    print(ts_daily)
