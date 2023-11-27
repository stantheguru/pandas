import pandas as pd 

a = [1,7,2]

myvar = pd.Series(a)


#print first value of the series
print(myvar[0])

y = [10,20,30]

#create labels
myVarLabelled = pd.Series(y, index=['x','y','z'])
#Access value by label
print(myVarLabelled['y'])

#Key/Value objects as series
calories = {"day1":100,"day2":200, "day3":400}

calSeries = pd.Series(calories)
print(calSeries)