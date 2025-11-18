import pandas as pd

df = pd.read_csv("BMW sales data (2010-2024) (1).csv")


summary = df.describe().T
print(summary) #prints the statistics such as: mean, mode, median, count and etc..

