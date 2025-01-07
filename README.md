# COSC-2409-Spring-Project-3-Data-Science

You are a junior developer at a data science firm.  Your task is to take these notes from a senior member of your team and stand up the start of a data science notebook.

(Note:  Please see the assignment page for notes on getting started with Google Colab if you'd like to use that for your notebook enviornment.  It is a free, online tool that requires no setup up front.)

**Subject: Data Analysis Project - Titanic Dataset Exploration**

**To:** Junior Data Analyst Team

**From:** Data Science Department

**Date:** October 26, 2023

**Project: Titanic Dataset Exploration and Cleaning**

**Introduction:**

As part of our ongoing data analysis initiatives, we're tasking you with an introductory project using the "Titanic: Machine Learning from Disaster" dataset. This dataset is a classic in the field and provides a good starting point for practicing data manipulation, cleaning, and basic exploratory data analysis. Your work will directly support our data science team's efforts.

**Dataset:**

The dataset is available on Kaggle: [https://www.kaggle.com/competitions/titanic/data](https://www.kaggle.com/competitions/titanic/data). Please download the `train.csv` file.

**Tools:**

You will be using Python with the Pandas, Matplotlib, and Seaborn libraries within a Jupyter Notebook environment (local installation, Google Colab, or similar).

**Tasks:**

Please complete the following tasks within a Jupyter Notebook, ensuring your code is well-commented and that you use Markdown cells to explain your steps and findings.

**Phase 1: Data Acquisition and Setup**

1.  **Task 1: Install Required Libraries:**

      * Instructions: In a notebook cell, use pip to install the necessary libraries: `!pip install pandas matplotlib seaborn`.
      * Documentation:
          * Pandas installation: [https://pandas.pydata.org/pandas-docs/stable/getting\_started/install.html](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
          * Matplotlib installation: [https://matplotlib.org/stable/users/installing.html](https://matplotlib.org/stable/users/installing.html)
          * Seaborn installation: [https://seaborn.pydata.org/installing.html](https://seaborn.pydata.org/installing.html)

2.  **Task 2: Import Libraries and Load Data:**

      * Instructions: Import the libraries (`import pandas as pd`, `import matplotlib.pyplot as plt`, `import seaborn as sns`). Load the `train.csv` file into a Pandas DataFrame using `pd.read_csv()`.
      * Documentation:
          * `pandas.read_csv()`: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read\_csv.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

3.  **Task 3: Initial Data Inspection:**

      * Instructions: Use `.info()` to display the data types and non-null value counts for each column. Use `.describe()` to obtain summary statistics for numerical columns.
      * Documentation:
          * `pandas.DataFrame.info()`: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html)
          * `pandas.DataFrame.describe()`: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)

**Phase 2: Data Cleaning**

4.  **Task 4: Handle Missing "Age" Values:**

      * Instructions: Fill missing values in the "Age" column with the median age. Use `.fillna()` and `.median()`.
      * Documentation:
          * `pandas.DataFrame.fillna()`: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)
          * `pandas.Series.median()`: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.median.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.median.html)

5.  **Task 5: Handle Missing "Embarked" Values:**

      * Instructions: Fill missing values in the "Embarked" column with the most frequent value (mode). Use `.fillna()` and `.mode()`.
      * Documentation:
          * `pandas.Series.mode()`: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mode.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mode.html)

6.  **Task 6: Convert "Sex" to Numerical:**

      * Instructions: Convert the "Sex" column to numerical data: "male" to 0 and "female" to 1. Use `.replace()` or `.map()`.
      * Documentation:
          * `pandas.DataFrame.replace()`: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html)
          * `pandas.Series.map()`: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html)

**Phase 3: Exploratory Data Analysis and Visualization**

7.  **Task 7: Overall Survival Rate Visualization:**

      * Instructions: Calculate the overall survival rate. Create a count plot showing the number of survivors and non-survivors. Use `seaborn.countplot()`.
      * Documentation:
          * `seaborn.countplot()`: [https://seaborn.pydata.org/generated/seaborn.countplot.html](https://seaborn.pydata.org/generated/seaborn.countplot.html)

8.  **Task 8: Survival Rate by Sex Visualization:**

      * Instructions: Calculate the survival rate for each sex. Create a bar plot visualizing these rates. Use `seaborn.barplot()`.
      * Documentation:
          * `seaborn.barplot()`: [https://seaborn.pydata.org/generated/seaborn.barplot.html](https://seaborn.pydata.org/generated/seaborn.barplot.html)

9.  **Task 9: Age Distribution Visualization:**

      * Instructions: Create a histogram of the 'Age' column to visualize its distribution. Use `seaborn.histplot()` or `matplotlib.pyplot.hist()`. Include a kernel density estimate if using `seaborn.histplot`.
      * Documentation:
          * `seaborn.histplot()`: [https://seaborn.pydata.org/generated/seaborn.histplot.html](https://seaborn.pydata.org/generated/seaborn.histplot.html)
          * `matplotlib.pyplot.hist()`: [https://matplotlib.org/stable/api/\_as\_gen/matplotlib.pyplot.hist.html](https://www.google.com/url?sa=E&source=gmail&q=https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)

**Deliverables:**

  * A Jupyter Notebook (.ipynb file) containing all code, outputs, visualizations, and explanations in Markdown cells.
  * A concise summary of your findings and insights within the notebook.



We expect clear, well-documented code and a thorough analysis of the data. Please reach out to the Data Science team (your instructor) if you have any questions.


