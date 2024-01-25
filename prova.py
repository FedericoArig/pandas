import pandas as pd

file_name = "wine.csv"

data = pd.read_csv(file_name)
#fa .describe tutto: count, means std min 25% 50 % 75% e max
statistics = data.describe()

print(statistics)

