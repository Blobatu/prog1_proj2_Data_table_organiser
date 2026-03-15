"""
organisateur de fichiers CSV par l'entremise d'un tableau lisible par humain. 
"""

# imports
from rich import print
import pandas as pd

# code
try:
    df = pd.read_csv('test_read.csv', on_bad_lines='skip')
    df.to_excel('test_write.xlsx', index=False)
except Exception as e:
    print(f"Error: {e}")