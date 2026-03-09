# https://leetcode.com/problems/duplicate-emails/description/


import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = person['email'].value_counts()
    duplicate_emails_list = email_counts[email_counts > 1].index.tolist()
    return pd.DataFrame(duplicate_emails_list, columns=['Email'])


if __name__ == '__main__':
    data = {
        'id': [1, 2, 3],
        'email': ['a@b.com', 'b@b.com', 'a@b.com'],
    }

    df = pd.DataFrame(data)
    # print(df)

    res = duplicate_emails(df)
    print(res)