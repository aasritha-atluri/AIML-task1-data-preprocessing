#install these using "pip install" if these are not present in your computer"
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

# Load dataset
df = pd.read_csv("titanic.csv")   # put dataset in repo

# Explore
print(df.head())
print(df.info())
print(df.isnull().sum())

# Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)  # too many nulls

# Encode categorical
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df['Embarked'] = le.fit_transform(df['Embarked'])

# Feature scaling
scaler = StandardScaler()
df[['Age','Fare']] = scaler.fit_transform(df[['Age','Fare']])

# Outlier detection (boxplot)
sns.boxplot(df['Fare'])
plt.show()

# Remove extreme outliers
q1 = df['Fare'].quantile(0.25)
q3 = df['Fare'].quantile(0.75)
iqr = q3 - q1
df = df[(df['Fare'] >= (q1 - 1.5*iqr)) & (df['Fare'] <= (q3 + 1.5*iqr))]

print("Final shape:", df.shape)

# Save cleaned data
df.to_csv("titanic_cleaned.csv", index=False)
