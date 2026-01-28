# https://www.youtube.com/watch?v=rLVCSmtoA7U
# https://seaborn.pydata.org/installing.html

import seaborn as sns
import matplotlib.pyplot as plt


def visualization_scatterplot():
    sns.scatterplot(x=[1,2,3], y=[1,2,3])
    plt.show()


if __name__ == '__main__':
    # visualization_scatterplot()
    sns.set_theme(style="darkgrid")
    # visualization_scatterplot()

    tips = sns.load_dataset("tips")
    print(tips)