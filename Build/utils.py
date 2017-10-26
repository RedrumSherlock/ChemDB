'''
Created on Oct 25, 2017

@author: Mengliao Wang
'''


import os
import csv
from Build.compound import Compound

# the default path and file names
DEFAULT_PATH = "../Data"
DEFAULT_COMPOUND_FILE = "compounds.csv"
DEFAULT_MASS_FILE = "mass_list.csv"
DEFAULT_FINAL_FILE = "results.csv"

def load_compounds(path = DEFAULT_PATH, compound_file = DEFAULT_COMPOUND_FILE, mass_file = DEFAULT_MASS_FILE):
    with open(os.path.join(path,mass_file), 'rb') as file:
        masses = csv.DictReader(file)
        mass_list = {name: 0.0 for name in masses.fieldnames}
        for row in masses:
            for name in masses.fieldnames:
                mass_list[name] = float(row[name])
            
    compound_list = []
    with open(os.path.join(path,compound_file), 'rb') as file:
        compounds = csv.DictReader(file)
        for row in compounds:
            compound_list.append( Compound(
                name = row['name'],
                formula = row['formula'],
                code3 = row['code3'],
                code1 = row['code1'],
                mass_list = mass_list
                ) )   
    return compound_list  
    

def save_csv(list, file_path = DEFAULT_PATH, file_name = DEFAULT_FINAL_FILE):
    # list is expected to be a list of lists. The first list is the header.
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    path = os.path.join(file_path, file_name)
    with open(path, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(list)
        