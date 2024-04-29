"""
Let's start with the most basic one -- a line chart.
We will use the COVID-19 data from the previous module to create our charts.
Let's show the number of cases in the month of December.
To create a line chart we simply need to call the plot() function on our DataFrame, which contains the corresponding data:
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

df[df['month']==12]['cases'].plot()
plt.savefig('plot.png')
