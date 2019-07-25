#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Input File Description:  Barrier doped AlGaAs/GaAs heterostructure.
# -------------------------------------------------------------------
# ----------------
# GENERAL SETTINGS
# ----------------

# TEMPERATURE
T = 300.0 #Kelvin

# COMPUTATIONAL SCHEME
# 0: Schrodinger
# 1: Schrodinger + nonparabolicity
# 2: Schrodinger-Poisson
# 3: Schrodinger-Poisson with nonparabolicity
# 4: Schrodinger-Exchange interaction
# 5: Schrodinger-Poisson + Exchange interaction
# 6: Schrodinger-Poisson + Exchange interaction with nonparabolicity
# 7: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson then  poisson and DD)
# 8: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson and DD)
computation_scheme = 2

# QUANTUM
# Total subband number to be calculated for electrons
subnumber_h = 4
subnumber_e = 1
# APPLIED ELECTRIC FIELD
Fapplied = 0.00#/50e-9 # (V/m)

# --------------------------------
# REGIONAL SETTINGS FOR SIMULATION
# --------------------------------

# GRID
# For 1D, z-axis is choosen
gridfactor = 0.5 #nm
maxgridpoints = 200000 #for controlling the size
mat_type='Wurtzite'
# REGIONS
# Region input is a two-dimensional list input.
# An example:
# Si p-n diode. Firstly lets picturize the regional input.
#         | Thickness (nm) | Material | Alloy fraction x|Alloy fraction y| Doping(cm^-3) | n or p type |
# Layer 0 |      250.0     |   Si     |      0         |      0         |      1e16      |     n       |
# Layer 1 |      250.0     |   Si     |      0         |      0         |      1e16      |     p       |
#
# To input this list in Gallium, we use lists as:
material =[[ 100., 'GaN', 0.0, 0.0, 5e17, 'p','b'],
            [ 2.0, 'AlGaInN', 0.46, 0.38, 5e17, 'p','b'],
            [ 5.0, 'AlGaInN', 0.48, 0.23, 5e17, 'p','b'],
            [ 2.0, 'InGaN', 0.23, 0.0, 0.0, 'p','w'],
            [ 2.0, 'AlGaInN', 0.48, 0.23, 0.0, 'p','b'],
            [ 2.0, 'InGaN', 0.23, 0.0, 0.0, 'p','w'],
            [ 5.0, 'AlGaInN', 0.48, 0.23, 5e17, 'n','b'],
            [ 100., 'GaN', 0.0, 0.0, 5e17, 'n','b']]
 
#This is accourding to interpolated Vegard’s law for quaternary ABxCyD1-x-y=NGaxAlyIn1-x-y
import numpy as np
x_max = sum([layer[0] for layer in material])
def round2int(x):
    return int(x+0.5)
n_max=round2int(x_max/gridfactor)
dop_profile=np.zeros(n_max)  
surface=np.zeros(2)  
if __name__ == "__main__": #this code allows you to run the input file directly
    input_obj = vars()
    import aestimo_eh as aestimo
    aestimo.run_aestimo(input_obj)
