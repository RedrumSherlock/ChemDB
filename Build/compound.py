'''
Created on Oct 25, 2017

@author: Mengliao Wang
'''

import warnings
from collections import OrderedDict

class Compound(object):
    
    def __init__(self, name, formula, code3, code1,  mass_list = None, elements = None):
        self.name = name
        self.formula = formula
        self.code3 = code3
        self.code1 = code1
        self.mass_list = mass_list
        self.elements = elements
        
        if self.elements is None and self.mass_list is not None:
             self.load_elements()
    
    def load_elements(self):
        self.elements = []
        length = len(self.formula)
        idx = 0
        while idx < length:
            if idx < length - 1 and self.formula[idx:idx+2] in self.mass_list:
                next = 2
            elif self.formula[idx] in self.mass_list:
                next = 1
            else:
                raise ValueError("Element {} or {} not found in the mass list".format(self.formula[idx], self.formula[idx:idx+1]))
            
            # Now we need to count the elements. 
            element = self.formula[idx:idx+next]
            idx = idx + next
            if idx == length or not self.formula[idx].isdigit():
                # Only one element
                self.elements.append(element)
            else:
                old_idx = idx
                while idx < length and self.formula[idx].isdigit():
                    idx = idx + 1
                counts = int(self.formula[old_idx:idx])
                for _ in range(counts):
                    self.elements.append(element)
                
    def elements2formula(self, elements):
        ele_dict = OrderedDict()
        for element_name in elements:
            if element_name in ele_dict:
                ele_dict[element_name] = ele_dict[element_name] + 1
            else:
                ele_dict[element_name] = 1
        
        new_forumla = ""
        for names, counts in ele_dict.items():
            new_forumla = new_forumla + names + (str(counts) if counts > 1 else "")
            
        return new_forumla 
            
                
    def connect(self, comp, effect = ""):
        new_name = self.name + comp.name
        new_code_3 = self.code3 + "-" + comp.code3
        new_code_1 = self.code1 + comp.code1
        new_elements = self.elements + comp.elements
        
        new_elements.remove('H')
        new_elements.remove('H')
        new_elements.remove('O')
        
        if effect == 'HCl':
            new_elements.remove('H')
            new_elements.append('Cl')
            new_code_3 = 'Cl-' + new_code_3
        
        new_formula = self.elements2formula(new_elements)
        
        return Compound(
            name = new_name,
            formula = new_formula,
            code3 = new_code_3,
            code1 = new_code_1,
            elements = new_elements,
            mass_list = self.mass_list)
    
    
    def get_mass(self):
        mass = 0.0
        for element_name in self.elements:
            mass = mass + self.mass_list[element_name]
        return mass
            
    def get_OCratio(self):
        count_O = 0.0
        count_C = 0.0
        for element_name in self.elements:
            if element_name == 'O':
                count_O = count_O + 1
            if element_name == 'C':
                count_C = count_C + 1
        if count_C > 0:
            return float( count_O * self.mass_list['O']/ (count_C * self.mass_list['C']) )
        else:
            return -1
        
    def get_HCratio(self):
        count_H = 0
        count_C = 0
        for element_name in self.elements:
            if element_name == 'H':
                count_H = count_H + 1
            if element_name == 'C':
                count_C = count_C + 1
        if count_C > 0:
            return float( count_H * self.mass_list['H']/ (count_C * self.mass_list['C']) )
        else:
            return -1
                