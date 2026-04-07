"""
organisateur de fichiers CSV par l'entremise d'un tableau lisible par humain. 
Par Antoine Desjardins-Chapleau
"""

# imports

import os
import glob

# adapte les chemins de fichiers 

script_dir = os.path.dirname(os.path.abspath(__file__))


# storage dews fichiers

file_mem = {
    'csv_input' : 'input_csv_file_here/*.csv' ,
    'xlsx_file' : os.path.join(script_dir, 'csv_file_organiser.xlsx') ,
    'csv_output' : 'output_organised_csv_here/*.csv' ,
    'md_output' : 'output_organised_markdown_here/*.csv' ,
}


# code

input_folder_path = os.path.join(script_dir, "input_csv_file_here")
output_dir_csv = os.path.join(script_dir, "output_organised_csv_here")
output_dir_md = os.path.join(script_dir, "output_organised_markdown_here")
os.makedirs(output_dir_csv, exist_ok=True)
csv_files = glob.glob(os.path.join(input_folder_path, "*.csv"))
os.makedirs(output_dir_md, exist_ok=True)
md_files = glob.glob(os.path.join(output_dir_md, "*.md"))