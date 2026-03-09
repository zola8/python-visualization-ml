import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    grouped_df = activity.groupby(["player_id"])

    for key, item in grouped_df:
        print(item, "\n")

    df = grouped_df["event_date"].min().reset_index()
    df.rename(columns={"event_date": "first_login"}, inplace=True)
    return df


if __name__ == '__main__':
    activity_data = {
        'player_id': [1, 1, 2, 3, 3],
        'device_id': [2, 2, 3, 1, 4],
        'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
        'games_played': [5, 6, 1, 0, 5]
    }

    activity_df = pd.DataFrame(activity_data)

    res = game_analysis(activity_df)
    print(res)
