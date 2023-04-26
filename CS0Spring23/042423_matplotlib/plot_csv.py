import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')
df.plot()

plt.show()

#use a list of indexes:
print(df.loc[[0, 1]])