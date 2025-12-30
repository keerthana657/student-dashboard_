import pandas as pd
import requests
import streamlit as st
from io import StringIO

print("📥 Downloading REAL student data from websites...")

# Option 1: Kaggle (if file exists)
try:
    df = pd.read_csv('StudentsPerformance.csv')
    print("✅ Kaggle data loaded!")
except:
    # Option 2: Public GitHub dataset
    print("🌐 Fetching from GitHub...")
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/students.csv"
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text))
    print("✅ GitHub data loaded!")

# Clean + Magic calculations
if 'math score' in df.columns.str.lower():
    df.columns = df.columns.str.lower()
df['Total Score'] = df.select_dtypes(include='number').sum(axis=1)
df['Average'] = df['Total Score'] / df.select_dtypes(include='number').shape[1]
df['Grade'] = pd.cut(df['Average'], bins=[0,60,70,80,90,100], 
                     labels=['F','D','C','B','A'])

# Save for dashboard
df.to_csv('student_data.csv', index=False)
print(f"✅ {len(df)} students ready in student_data.csv!")
print("\nFirst 5 students:")
print(df.head())
