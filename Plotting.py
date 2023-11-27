import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("./Sample Data/Inventory.csv")

#Scatter Plot
df.plot(kind='scatter', x='value', y='shelfLife')

#Histogram

plt.show()