import pandas as pd

file_name= "iris.data"

data = pd.read_csv(file_name)

print(data)

rows = data.head()

print(rows)

statistics = data.describe()

print(statistics)