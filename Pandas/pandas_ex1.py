import pandas as pd

data = {
    'Name': ['Ajith', 'Bob', 'Charlie'],
    'Age': [25, 30 ,35],
    'City': ['New York', 'London', 'Mumbai']
    }

df = pd.DataFrame(data)
print(df.dtypes)
print(df)
