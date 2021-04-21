import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
import csv
import json
"""
Simple LCA creation
"""

"""
#Get component properties from Fusion 360; probably not our focus
    mat_type = Get material type from Fusion 360 # “grade 5 carbon steel”
    mat_density = Get material density from Fusion 360 “8000kg/m3”
    process_type = from manufacturing process (probably input as part of ASI interface), get the type as it relates to additive/subtractive; can store additive = 1, subtractive = -1
    #process_type = -1
    mass_comp = Get material mass (or volume * density) from Fusion 360 #5g
    box_size = Get dimension in x, y, z directions #Want to figure out the size of a box the component would fit in; use array/list/whatever the name of this data type is

"""
class Fusion_LCA:
    def __init__(self, product_name, mat_type, mat_density, process_type,
                 box_size, mass_comp, mat_footprint, mat_cost, energy_footprint,energy_cost,
                 specific_energy, is_recycled, disposal_impact):

        #Data from Fusion 360
        self.product_name = product_name
        self.mat_type = mat_type
        self.mat_density = mat_density
        self.process_type = process_type
        self.mass_comp = mass_comp
        self.box_size = box_size
        self.mat_footprint = mat_footprint
        self.mat_cost = mat_cost
        self.energy_footprint = energy_footprint
        self.energy_cost = energy_cost
        self.specific_energy = specific_energy
        self.is_recycled = is_recycled
        self.disposal_impact = disposal_impact
        return

    def manufacturing(self):
        """
        Calculates the manufacturing impact of the product.
        """
        
        #additive manufacturing 
        if self.process_type == 1:
            mass_processed = self.mass_comp
            mass_input = self.mass_comp #feed the final amount of mass into manufacturing process

        #subtractive manufacturing
        elif self.process_type == -1:
            mass_processed = (self.mat_density * self.box_size) - self.mass_comp
            mass_input = self.mat_density * self.box_size

        #calculate gate CO2 and cost 
        gate_CO2 = (mass_input * self.mat_footprint) + (self.specific_energy * mass_processed * self.energy_cost)
        gate_cost = (mass_input * self.mat_cost) + (self.specific_energy * mass_processed * self.energy_cost)

        return gate_CO2, gate_cost

    def assembly(self): 
        """
        Calculates the assembly impact of the product.
        """
        return 0 # non-zero for production

    def disposal(self):
        """
        Calculates the disposal impact of the product.
        """
        if self.is_recycled == 1:
            return 0
        else: 
            return self.disposal_impact*self.mass_comp

def main():
    #Data from Fusion 360
    product_name = "Carbon Black Steel Bolt"
    mat_type = ["Grade 5 Carbon Steel"]
    mat_density = 8000 #material density in kg/m^3
    process_type = -1 # 1 is additive, -1 is subtractive manufacturing
    mass_comp = 0.001 #mass of component (kg)
    box_size = 0.006*0.006*0.01 # size of a box the component would fit in (m^3)
    
    #Data from EcoInvent, GABI, OpenLCA
    mat_footprint = 3 #material footprint (kg CO2eq/kg)
    mat_cost = 1.53 #cost of material ($/kg)
    energy_footprint = 1e-7 #footprint of energy used in manufacturing (kgCO2/J)
    energy_cost = 2.8e-8 #cost of energy in manufacturing ($/joule)
    specific_energy = 1000 #energy used per unit of mass processed (J/kg)
    is_recycled = -1 #1 is recycled, -1 is not-recycled
    disposal_impact = 10**-2 # disposal impact of material (kgCO2eq/kg of mat_type) 
    
    my_LCA = Fusion_LCA(product_name, mat_type, mat_density, process_type,
                 box_size, mass_comp, mat_footprint, mat_cost, energy_footprint,energy_cost,
                 specific_energy, is_recycled, disposal_impact)
    
    co2, cost = my_LCA.manufacturing()
    co2 += my_LCA.disposal()
    print("A", product_name, "costs $",cost,"and outputs", co2, "kg of CO2 equivalent.")

if __name__ == "__main__":
    main()