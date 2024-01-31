import pandas as pd

a=[1,None,3]

data = pd.DataFrame(a, columns=['values'])

data['values'].fillna(0, inplace=True)

print(data)

print(pd.concat([data,data]))

print(data.pivot(columns=['values']))

data.melt()