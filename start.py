# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Exploratory Data Analysis of the Titanic Dataset

# %% [markdown]
# **Goal:** To explore the Titanic dataset and identify factors that influenced passenger survival.
#
# **Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ## Loading the Data

# %%
titanic_data = pd.read_csv("titanic.csv") # Make sure titanic.csv is in the same directory

# %% [markdown]
# ## Initial Data Inspection

# %%
print("First 5 rows:")
print(titanic_data.head())
print("\nData Info:")
print(titanic_data.info())
print("\nData Description:")
print(titanic_data.describe())

# %% [markdown]
# ## Data Cleaning (Handling Missing Values)

# %%
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)
titanic_data.drop('Cabin', axis=1, inplace=True)

# %% [markdown]
# ## Exploratory Data Analysis and Visualization

# %%
plt.figure(figsize=(8, 6))  # Adjust figure size for better visualization
sns.countplot(x='Survived', data=titanic_data)
plt.title('Survival Count')
plt.xlabel('Survived (0: No, 1: Yes)')
plt.ylabel('Count')
plt.show()

# %%
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', hue='Survived', data=titanic_data)
plt.title('Survival by Passenger Class')
plt.xlabel('Passenger Class (1: 1st, 2: 2nd, 3: 3rd)')
plt.ylabel('Count')
plt.show()

# %%
plt.figure(figsize=(8, 6))
sns.boxplot(x='Pclass', y='Age', data=titanic_data)
plt.title('Age Distribution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()

# %%
plt.figure(figsize=(8, 6))
sns.histplot(titanic_data['Age'], kde=True) #added kde for better visualization
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# %%
#Select numerical columns for pairplot to avoid errors
numerical_cols = titanic_data.select_dtypes(include=np.number).columns
sns.pairplot(titanic_data[numerical_cols], hue="Survived")
plt.show()

# %% [markdown]
# ## Further Analysis (Example: Survival Rate by Sex)

# %%
print("Survival Rate by Sex:")
print(titanic_data.groupby('Sex')['Survived'].mean())

# %%
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', hue='Survived', data=titanic_data)
plt.title('Survival by Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

# %% [markdown]
# ## Conclusions
#
# Based on the analysis, we can observe:
#
# *   A higher proportion of females survived.
# *   Passengers in higher classes had a higher survival rate.
# *   The age distribution shows a concentration of younger passengers.
# *   There appears to be a relationship between age, class, and survival. Further analysis could investigate this relationship more closely.

# %%
