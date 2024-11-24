"""
Code for the publication AI-Enhanced Distributionally Robust Chance
Constrained Optimization for Managing Uncertainty in Heat Pump Dominated 
Residential Energy Systemsby Marwan Mostafa 

Parameters File
"""

###############################################################################
## IMPORT PACKAGES & SCRIPTS ## 
###############################################################################
#### PACKAGES ####
import gurobipy as gp
import numpy as np

###############################################################################
## GUROBI PARAMETERS ## 
###############################################################################
# gp.setParam("NonConvex",-1) # enable non convex constraints, enable = 2
#gp.setParam("OutputFlag",0) # solver output, enable = 1
# gp.setParam("DualReductions", 0) # check if feasible or unbounded: enable = 0
# gp.setParam("MIPGap",2e-4) # MIP gap, default = 1e-4


###############################################################################
## GENERAL ## 
###############################################################################
### NETWORK ###
hp_scaling = 1.4 # heat pump scaling factor
hh_scaling = 1.7 # household scaling factor

hp_max_power = 1 # heat pump max power in MW
ts_size_mwh = 84*4 # thermal storage size in MWh
ts_sof_init = 0.5 # initial state of fill of thermal storage
ts_eff = 0.95 # thermal storage efficiency
ts_out_max = 100 # thermal storage max output in MWth
ts_in_max = 100 # thermal storage max input in MWth
COP = 4 # heat pump COP

### Optimization Costs ###
import_cost = 80  # €/MW for importing power from the external grid
export_cost = 80  # €/MW for exporting power to the external grid
curtailment_cost = 150  # €/MW for curtailing PV (set higher than import/export costs)
flexibility_cost = 200  # €/MW for reducing load at bus 1

   
### CONVERGENCE CRITERIA ###



### FORECAST ###
N_MC = 10 # number of samples for monte-carlo simulation
