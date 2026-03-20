"""
ce programme est utilisé par le programme principal pour gérer les chemins de fichiers
"""

import os
import glob

# adapte les chemins de fichiers 

script_dir = os.path.dirname(os.path.abspath(__file__))


# storage dews fichiers

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