"""
organisateur de fichiers CSV par l'entremise d'un tableau lisible par humain. 
"""

# imports
from rich import print
import pandas as pd
import subprocess 
import os
import glob

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# fonctions

def csv_to_xlsx(csv_file, xlsx_file):
    """
    cette fonction lit un fichier csv et le convertie en fichier xlsx.
    elle gere au passage les erreurs de lecture et d'ecriture avec des messages de status
    """
    try:
        csv_file = pd.read_csv(csv_file, on_bad_lines='skip')
        print("[green]\n CSV file read sucessfully")
        try:
            csv_file.to_excel(xlsx_file, index=False)
            print("[green] xlsx file written sucessfully")
            return "no error"
        except Exception as e:
            print(f"[red]xlsx write Error: {e}")
    except Exception as e:
        print(f"[red]CSV read Error: {e}")

def xlsx_to_csv(xlsx_file, csv_file):
    """
    cette fonction lit un fichier xlsx et le convertie en fichier csv.
    elle gere au passage les erreurs de lecture et d'ecriture avec des messages de status
    """
    try:
        xlsx_file = pd.read_excel(xlsx_file)
        print("[green] xlsx file read sucessfully")
        try:
            xlsx_file.to_csv(csv_file, index=False)
            print("[green] csv file written sucessfully\n")
        except Exception as e:
            print(f"[red]csv write Error: {e}")
    except Exception as e:
        print(f"[red]xlsx read Error: {e}")


# config

YELLOW = "\033[93m"
RED = "\033[91m"

file_mem = {
    'csv_input' : 'input_csv_file_here/*.csv' ,
    'xlsx_file' : os.path.join(script_dir, 'csv_file_organiser.xlsx') ,
    'csv_output' : 'output_organised_csv_here/*.csv' ,
}


# code

folder_path = os.path.join(script_dir, "input_csv_file_here")
output_dir = os.path.join(script_dir, "output_organised_csv_here")
os.makedirs(output_dir, exist_ok=True)
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))


if csv_files:
    for file_path in csv_files:
        file_mem['csv_input'] = file_path
        if csv_to_xlsx(file_mem['csv_input'], file_mem['xlsx_file']) == "no error":
            subprocess.run(["start", "excel", file_mem['xlsx_file']], shell=True)
            go = input(f"\n{YELLOW}Press Enter {RED}after closing Excel {YELLOW}when you are done editing the .xlsx file and are ready convert it back to .csv: \n")
            file_mem['csv_output'] = os.path.join(output_dir, os.path.basename(file_path).replace(".csv", "_organised.csv"))
            xlsx_to_csv(file_mem['xlsx_file'], file_mem['csv_output'])
            #subprocess.run(["start", "notepad", file_mem['csv_output']], shell=True)       # debug to see the thing actually works
        else:
            print()
else:
    print("No .csv files found.")