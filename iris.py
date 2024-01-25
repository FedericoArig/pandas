import pandas as pd

file_name = "iris.data"

data = pd.read_csv(file_name,names = ["sepal.length","sepal.width","petal.length","petal.width","class"])

rows = data.head()

print(rows)

columns_names = data.columns
print(columns_names)