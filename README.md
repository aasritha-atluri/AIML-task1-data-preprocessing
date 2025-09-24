# Task 1 - Data Cleaning & Preprocessing (ML Internship)

This repository contains my solution for **Task 1** of the ML Internship.  
The goal of this task is to clean and preprocess raw data so it is ready for Machine Learning.

## Requirements
Install all dependencies before running:

```bash
pip install -r requirements.txt

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

## Files in this Repository
- `task1code.py` → Code for preprocessing
- `titanic.csv` → Raw dataset
- `titanic_cleaned.csv` → Cleaned dataset

