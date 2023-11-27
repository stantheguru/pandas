import pandas as pd 

df = pd.read_csv("../Sample Data/Inventory.csv")

#Replace Non integer values with integer
df['value'] = pd.to_numeric(df['value'])


#Remove rows with wrong format
df.dropna(subset=['value'], inplace=True)
print(df)