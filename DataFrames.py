import pandas as pd 


data = {
    "calories":[100,500,780],
    "duration":[20,56,45]
}

df = pd.DataFrame(data)

#Locate row
row1 = df.loc[0]

#Return a Panda Series
series = df.loc[[0,1]]

#Named Indexes
df_named = pd.DataFrame(data, index=["day1", "day2", "day3"])

#Locate named indexes
day2 = df_named.loc['day2']
print(day2)