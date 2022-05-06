import sqlite3

import pyodbc

import pandas as pd

from collections import Counter

# Extract

con = pyodbc.connect(driver='{SQL Server}', server='yourserverurl', database='countries')

df=pd.read_sql_query("SELECT name FROM countries", con)

df = pd.DataFrame(df)

df.to_txt('data.txt',sep=' ')

# Transformation

fname='data.txt'

with open(fname, 'r') as f:
    for line in f:
        l=line.upper()
        print(l)

# Load (Writer)
with open('C:/Users/sadik/OneDrive/Documents/file.txt', 'w') as output_file:
    output_file.write(l)

# Second Part

with open(fname, 'r') as f:
    for line in f:
        l = line
        line.lower()
        print(Counter(line.split()))









