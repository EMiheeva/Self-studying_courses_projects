#We create a pandas Series with some numbers and use it to create our chart:

import matplotlib.pyplot as plt
import pandas as pd

series = pd.Series([18, 42, 9, 32, 81, 64, 3])
series.plot(kind='bar')
plt.savefig('plot.png')
