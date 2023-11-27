import pandas as pd 

df = pd.read_csv("./Sample Data/Catalog.csv")
df_tostring = df.to_string() #Use to_string() to return te entire dataframe
print(df) #If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

#max_rows
pd.options.display.max_rows = 9999 #Use this to adjust max rows
print(df)



