"""
organisateur de fichiers CSV par l'entremise d'un tableau lisible par humain. 
Par Antoine Desjardins-Chapleau
"""


# imports
from rich import print
import pandas as pd
import subprocess
import csv 
import os
from File_manager import file_mem, csv_files, output_dir_csv, output_dir_md
import time


# fonctions

def csv_to_xlsx(csv_file, xlsx_file):
    """
    cette fonction lit un fichier csv et le convertie en fichier xlsx.
    elle gere au passage les erreurs de lecture et d'ecriture avec des messages de status
    enrtées: les filepaths du csv d'entrée et du xlsx
    sortie: le fichier converti du csv d'entrée dans le fichier xlsx
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
    enrtées: les filepaths du xlsx et du csv de sortie
    sortie: le fichier converti du xlsx dans le fichier csv de sortie
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


def read_csv_as_list(filename):
    """
    cette fonction crée une liste contenant le contenue d'un fichier csv.
    enrtées: les filepaths du csv
    sortie: le fichier csv lu en liste de listes
    """
    try:
        rows = []
        with open(filename, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
        print(f"[italic blue]CSV file '[/]{os.path.basename(filename)}[italic blue]' read sucessfully.")
        return rows
    except OSError as e:
        print(f"[red]Error reading file:[/] {e}")


def write_markdown_file(csv_input_file, md_output_file):
    """
    cette fonction lit un fichier csv et le convertie en fichier markdown.
    enrtées: les filepaths du csv et du md
    sortie: le fichier md 
    """
    try:
        rows = read_csv_as_list(csv_input_file)
        if not rows:
            print(f"[italic blue]No rows found in CSV file '{os.path.basename(csv_input_file)}', skipping markdown conversion.")
            return
        max_len = max(len(row) for row in rows)
        with open(md_output_file, "w", encoding="utf-8") as file:
            file.write("|" * max_len + "|\n")
            file.write("|:-:" * max_len + "|\n")
            for row in rows:
                if not row:
                    continue
                written = " |".join(str(cell) for cell in row)
                file.write("| " + written + " |\n")
        print(f"[italic blue]Markdown file '[/]{os.path.basename(md_output_file)}[italic blue]' written sucessfully.")
    except OSError as e:
        print(f"[red]Error writing file:[/] {e}")


# couleurs pour input()

YELLOW = "\033[93m"
GREEN = "\033[92m"


# code

if csv_files:
    for file_path in csv_files:
        file_mem['csv_input'] = file_path
        read_current_file = input(f"\n{YELLOW}The file {GREEN}{os.path.basename(file_path)}{YELLOW} is about to be read, do you wish to read it? (y/n): ").lower()      # demande à l'utilisateur si il veut lire le fichier
        
        if read_current_file == "y":        #  si il veut lire le fichier
            if csv_to_xlsx(file_mem['csv_input'], file_mem['xlsx_file']) == "no error":     # si la conversion du fichier s'est bien faite
                subprocess.run(["start", "excel", file_mem['xlsx_file']], shell=True)       # ouvre excel pour que l'utilisateur puisse modifier le fichier
                
                go = input(f"\n{YELLOW}Press Enter when you are done editing the .xlsx file and are ready convert it back to .csv: ")       # attend que l'utilisateur ait fini de modifier le fichier
                subprocess.run(["taskkill", "/F", "/IM", "EXCEL.EXE"], shell=True, check=False)     # ferme excell pour éviter les conflits de fichiers
                file_mem['csv_output'] = os.path.join(output_dir_csv, os.path.basename(file_path).replace(".csv", "_organised.csv"))        # donne le fichier organisé dans le dossier cde sortie
                xlsx_to_csv(file_mem['xlsx_file'], file_mem['csv_output'])
                
                to_md = input(f"\n{YELLOW}Do you want to convert the organised .csv file to markdown format? (y/n): ").lower()      # demande si l'utilisateur veut aussi le résultat en format tableau md
                
                if to_md == "y":        # donne aussi une copie en tableau md
                    file_mem['md_output'] = os.path.join(output_dir_md, os.path.basename(file_path).replace(".csv", "_organised.md"))
                    write_markdown_file(file_mem['csv_output'], file_mem['md_output'])
                
                elif to_md == "n":      # ne le transforme pas en md
                    continue
                
                else:
                    print()
                time.sleep(3)       # donne le temps à excel de se fermer
            else:
                print()
        else:
            continue        # passe le fichier si l'utilisateur ne veut pas le modifier
else:
    print("[red]No .csv files found.")