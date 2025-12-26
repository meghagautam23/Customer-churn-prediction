import pandas as pd

# Load dataset
df = pd.read_csv("data/churn.csv")

# View first 5 rows
print(df.head())

# Dataset info
print(df.info())

# Check missing values
print(df.isnull().sum())
