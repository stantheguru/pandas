import pandas as pd

selected_columns = ['value', 'shelfLife']

df = pd.read_csv('./Sample Data/Inventory.csv', usecols=selected_columns)

#Use corr() to show relations between columns
print(df)
print(df.corr())