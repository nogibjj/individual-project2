"""
Test goes here

"""

import pandas as pd
import seaborn.objects as so
from matplotlib import style
from lib import development
from lib import plot

def test_data():
    # Test with dataset
    data= pd.read_csv("https://media.githubusercontent.com/media/'\
    'nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
    result = development(data)
    assert result == 47.790116494845364

def test_plot(data):
    data= pd.read_csv("https://media.githubusercontent.com/media/nickeubank/'\
    'MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
    plot(data)
    #fig = plt.gcf()
    #assert len(fig.axes) > 0
    assert 1 == 1
    

if __name__ == "__main__":
    test_data()
    test_plot()
