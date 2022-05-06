# Import Libraries

import pandas as pd

import os

from collections import Counter

# Change to directory where the files are stored

os.chdir('C:/Users/sadik/OneDrive/Desktop/Null-Innovation')

# Extract (Reader)

fname = 'personal.txt'

# Transformation

with open(fname, 'r') as f:
    for line in f:
        l = line.upper()
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

