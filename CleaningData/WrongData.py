import pandas as pd 

df = pd.read_csv("../Sample Data/Inventory.csv")

#Replacing values
df.loc[7, "value"] = 10000

#Replacing with loop
for i in df.index:
    if df.loc[i,'value']>10000:
        df.loc[i,'value'] = 10000


#Removing rows
#Drop rows where value is above 10000
for i in df.index:
    if df.loc[i,'value'] >10000:
        df.drop(i,inplace=True)

print(df.to_string())