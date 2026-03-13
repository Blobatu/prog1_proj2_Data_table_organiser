"""
organisateur de fichiers CSV par l'entremise d'un tableau lisible par humain. 
"""

# imports
import csv

# fonctions

def read_csv(filename):
    try:
        rows = []
        with open(filename, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
        print(f"CSV file '{filename}' written sucessfully.")
        return rows
    except OSError as e:
        print(f"Error reading file: {e}")

def write_markdown_file(filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("| test | test | test |\n")
            file.write("|:---: |:----:|:---: |\n")
            file.write("| test | test | test |\n")
            file.write("| test | test | test |\n")
            file.write("| test | test | test |\n")
        print(f"Markdown file '{filename}' written sucessfully.")
    except OSError as e:
        print(f"Error writing file: {e}")


# lecture test
read_csv("test_read.csv")
write_markdown_file("test_table.md")