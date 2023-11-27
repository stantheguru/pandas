import pandas as pd 


df = pd.read_csv("./Sample Data/Catalog.csv")

df_10 = df.head(10) #Get first 10 rows
df_5 = df.head() #Get first 5 rows

#Last 5 rows
df_tail = df.tail()

#Info about the data
info = df.info()
