import numpy as np
import pandas as pd

data = {
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red'],
    'Size': ['Small', 'Large', 'Medium', 'Small', 'Large']
}

if __name__ == '__main__':
    df = pd.DataFrame(data)
    print('Original DataFrame')
    print(df)

    # Perform one-hot encoding
    df_encoded = pd.get_dummies(df)
    print('\n DataFrame after performing One-hot Encoding')
    print(df_encoded)

    # Series with days of the week
    days = pd.Series(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday'])
    print(pd.get_dummies(days, dtype='int'))

    # List with color categories and NaN
    colors = ['Red', 'Blue', 'Green', np.nan, 'Red', 'Blue']
    print(pd.get_dummies(colors, dummy_na=True, dtype='int'))
