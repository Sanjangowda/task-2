import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("BMW sales data (2010-2024) (1).csv")


summary = df.describe().T
print(summary) #prints the statistics such as: mean, mode, median, count and etc...

numeric_col = df.select_dtypes(include=['int64', 'float64']).columns

#Histograms
for col in numeric_col:
    plt.figure(figsize=(6,4))
    plt.hist(df[col].dropna(), bins=30)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()
    
#boxplots
for col in numeric_col:
    plt.figure(figsize=(6,4))
    plt.boxplot(df[col].dropna())
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.ylabel("Value")
    plt.show() 

#pairplots
sns.pairplot(df.select_dtypes(include=['int64', 'float64']))
plt.show()

#coorelation matrix computation
corr = df.corr
