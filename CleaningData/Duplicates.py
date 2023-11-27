import pandas as pd 

df = pd.read_csv('../Sample Data/Inventory.csv')


#Remove duplicates
df.drop_duplicates(inplace=True)
duplicates = df.duplicated()
print(duplicates)