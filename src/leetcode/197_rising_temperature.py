# https://leetcode.com/problems/rising-temperature/description/
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+

# +----+------------+-------------+
# | id | recordDate | temperature |
# +----+------------+-------------+
# | 1  | 2015-01-01 | 10          |
# | 2  | 2015-01-02 | 25          |
# | 3  | 2015-01-03 | 20          |
# | 4  | 2015-01-04 | 30          |
# +----+------------+-------------+

# Output:
# +----+
# | id |
# +----+
# | 2 |
# | 4 |
# +----+
import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.sort_values('recordDate').reset_index(drop=True)
    df['prev_day'] = df['recordDate'].shift(1)
    df['prev_temperature'] = df['temperature'].shift(1)
    # print(df)
    ds = df[
        (df['temperature'] > df['prev_temperature']) &
        (df['recordDate'] - df['prev_day'] == pd.Timedelta(days=1))
        ]['id']
    return pd.DataFrame({'Id': ds})


if __name__ == '__main__':
    data = {
        'id': [1, 2],
        'recordDate': ['2015-01-14', '2015-01-16'],
        'temperature': [3, 5]
    }

    df = pd.DataFrame(data)
    df['recordDate'] = pd.to_datetime(df['recordDate'])

    print(rising_temperature(df))
