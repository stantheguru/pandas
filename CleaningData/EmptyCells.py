import pandas as pd

df = pd.read_csv("../Sample Data/Inventory.csv")

#Remove rows that contain empty cells
#Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()

#To change the original dataframe use inplace = True
df.dropna(inplace=True)

#Replacing empty values
df.fillna(130, inplace=True) #Replace all empty values with 130

#Replace values for specific columns
df['value'].fillna(130, inplace=True)

#Replace Using Mean, Median, or Mode
#Mean
x = df['value'].mean()
df['value'].fillna(x,inplace=True)

#Median
median = df['value'].median()
df['value'].fillna(median,inplace=True)

#Mode
mode = df['value'].mode()
df['value'].fillna(mode,inplace=True)






