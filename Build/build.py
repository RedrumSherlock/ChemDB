'''
Created on Oct 25, 2017

@author: Mengliao Wang
'''

substraction = "H2O"

from Build.utils import *
import copy

def generate():
  
    # First load the compounds and the mass list  
    compound_list = load_compounds()
    compound_list2 = copy.deepcopy(compound_list)
      
    final_list = []
    final_list.append(['Code3', 'Code1', 'Formula', 'O/C', 'H/C', 'Mass'])
      
    for i in range(len(compound_list)):
        for j in range(len(compound_list2)):
            new_compound = compound_list[i].connect(compound_list2[j])
            final_list.append([new_compound.code3, new_compound.code1, new_compound.formula,
                               new_compound.get_OCratio(), new_compound.get_HCratio(), new_compound.get_mass()
                               ])
            new_compound = compound_list[i].connect(compound_list2[j], effect = 'HCl')
            final_list.append([new_compound.code3, new_compound.code1, new_compound.formula,
                               new_compound.get_OCratio(), new_compound.get_HCratio(), new_compound.get_mass()
                               ])
          
    save_csv(final_list)
          
  
if __name__ == "__main__":
    generate()