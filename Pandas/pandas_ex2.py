import pandas as pd

df = pd.read_csv("data.csv")
df['Age'].to_csv("output.csv", index=False)
