# Task 1 - Data Cleaning & Preprocessing (ML Internship)

This repository contains my solution for **Task 1** of the ML Internship.  
The goal of this task is to clean and preprocess raw data so it is ready for Machine Learning.

## Requirements
Install all dependencies before running:

```bash
pip install -r requirements.txt
```

## Steps Done
- Imported Titanic dataset
- Checked null values and data types
- Handled missing values (median/mode imputation, dropped columns with many nulls)
- Encoded categorical variables (Sex, Embarked)
- Standardized numerical features (Age, Fare)
- Detected and removed outliers (IQR method)
- Saved cleaned dataset

## Tools & Libraries
- Python  
- Pandas, NumPy  
- Seaborn, Matplotlib  
- Scikit-learn  

## How to Run
1. Clone this repository or download the files.
2. Make sure you have installed Python 3.x and all the dependencies (see Requirements).
3. Place the raw dataset (`titanic.csv`) in the same folder as `task1code.py`.
4. Run the script:

```bash
python task1code.py
```
5. A boxplot window will appear for outlier visualization.
👉 Close the boxplot window to let the script continue.

6. After execution, the cleaned dataset will be saved as `titanic_cleaned.csv`.


