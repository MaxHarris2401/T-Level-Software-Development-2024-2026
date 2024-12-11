import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
file_path = Path(__file__).parent
csv_path = (file_path /"student_lifestyle_dataset.csv")

df = pd.read_csv(csv_path)
def q1():
    df_sorted = df.head(25)
    df_sorted = df_sorted.sort_values(by='Study_Hours_Per_Day')
    df_sorted.plot(x='Study_Hours_Per_Day', y='GPA', kind='bar')

    plt.title('GPA: Study Hours Per Day', fontsize=16)
    plt.xlabel('Study Hours per Day', fontsize=14)
    plt.ylabel('GPA', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

def q2():
    df_sorted = df.head(25)
    df_sorted = df_sorted.sort_values(by='Stress_Level')
    df_sorted.plot(x='Stress_Level', y='GPA', kind='bar')

    plt.title('GPA: Stress Levels', fontsize=16)
    plt.xlabel('Stress_Level', fontsize=14)
    plt.ylabel('GPA', fontsize=14)
    plt.xticks(rotation=45, fontsize = 8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()
def q3():
    low_stress_df = df[df['Stress_Level'] == 'Low']

    top_5_df = low_stress_df.nlargest(5, 'GPA')

    top_5_df.plot(x='Student_ID', y='GPA', kind='bar')

    plt.title('GPA: Top 5 with low stress', fontsize=16)
    plt.xlabel('Student ID', fontsize=14)
    plt.ylabel('GPA', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()


q1()
q2()
q3()
