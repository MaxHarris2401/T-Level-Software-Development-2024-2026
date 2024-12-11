import pandas as pd
import matplotlib.pyplot as plt
import random

from pathlib import Path
file_path = Path(__file__).parent
csv_path = (file_path /"ytData.csv")

def q1():
    df = pd.read_csv(csv_path)
    country_column = df[['Country', 'video views']]
    #country_column['video views'] = country_column['video views'].apply(lambda x: f"{x:,}")
    country_column = country_column.groupby("Country").max().reset_index()
    print(country_column)
    country_column.plot(kind="bar",x='Country',y='video views')
    
    plt.show()
    
q1()

def q2():
    df = pd.read_csv(csv_path)
    subscriber_column = df[['Country', 'subscribers']]
    subscriber_column = subscriber_column.groupby("Country").max().reset_index()
    print(subscriber_column)
    subscriber_column.plot(kind="bar",x='Country',y='subscribers')
    
    plt.show()

q2()

def q3():
    df = pd.read_csv(csv_path)
    df = df.head(50)

    youtuber_column = df[['Youtuber',  'video views']].copy()
    youtuber_column["Youtuber"] = youtuber_column["Youtuber"].astype(str)
    youtuber_column["video views"] = pd.to_numeric(youtuber_column["video views"], errors='coerce')
    youtuber_column["video views (in billions)"] = youtuber_column["video views"] / 1e9
    
    plt.figure(figsize=[18, 6])
    plt.scatter(youtuber_column["Youtuber"], youtuber_column["video views (in billions)"], color='skyblue')
    plt.xlabel('Youtuber', fontsize = 5)
    plt.ylabel("video views (in billions)", fontsize = 5)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
q3()

def q4():
    df = pd.read_csv(csv_path)
    df.plot(x='Name', y='Minutes Per Year', kind='bar')