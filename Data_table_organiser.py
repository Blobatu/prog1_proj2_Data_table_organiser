"""
organisateur de fichiers CSV par l'entremise d'un tableau lisible par humain. 
"""

# imports
import csv

# fonctions

def read_csv(file_path):
    rows = []
    with open(file_path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows

# lecture test
data = read_csv("test_read.csv")
print(data)