"""
organisateur de fichiers CSV par l'entremise d'un tableau lisible par humain. 
"""
            #file.write("| test | test | test |\n")
            #file.write("|:---: |:----:|:---: |\n")
            #file.write("| test | test | test |\n")
            #file.write("| test | test | test |\n")
            #file.write("| test | test | test |\n")

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
        print(f"CSV file '{filename}' read sucessfully.")
        return rows
    except OSError as e:
        print(f"Error reading file: {e}")

def write_markdown_file(filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            max_len = 0
            for length in read_csv("test_read.csv"):
                if len(length) > max_len:
                    max_len = len(length)
                else:
                    continue
            file.write("| test " * max_len + "|\n")
            file.write("|:---: " * max_len + "|\n")
            for row in read_csv("test_read.csv"):
                if row == []:
                    continue
                else:
                    written = " | ".join(row)
                    file.write("| " + written + " |\n")
        print(f"Markdown file '{filename}' written sucessfully.")
    except OSError as e:
        print(f"Error writing file: {e}")


# lecture test
write_markdown_file("test_table.md")