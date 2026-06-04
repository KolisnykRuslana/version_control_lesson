import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
df = pd.DataFrame({'Name': ['Olga', 'Maks', 'Slava'], 'Aga': [22, 34, 45]})
df.head()
print(df.head())
sns.barplot(x='Name', y='Aga', data=df)
plt.show()
