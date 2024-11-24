"""
Code for the publication AI-Enhanced Distributionally Robust Chance
Constrained Optimization for Managing Uncertainty in Heat Pump Dominated 
Residential Energy Systemsby Marwan Mostafa 

Debug File
"""
###############################################################################
## IMPORT PACKAGES & SCRIPTS ## 
###############################################################################
#### SCRIPTS ####
import data as dt
import griddata as gd 
import results as rs
import plot as pl
import opf as opf
import drcc as drcc
import montecarlo as mc

#violations_df_opf = rs.load_optim_results("mc_results_opf.pkl")
#violations_df_drcc = rs.load_optim_results("mc_results_drcc.pkl")
#opf_results = rs.load_optim_results("opf_results.pkl")
#drcc_results = rs.load_optim_results("drcc_opf_results.pkl") 

#pl.plot_opf_results_plotly(opf_results)
#pl.plot_opf_results_plotly(drcc_results)



violations_df_drcc = rs.load_optim_results("violations_df_drcc.pkl")
drcc_mc_line_results_df = rs.load_optim_results("drcc_mc_line_results.pkl")

violations_df_opf = rs.load_optim_results("mc_results_opf.pkl")
opf_mc_line_results_df = rs.load_optim_results("opf_mc_line_results.pkl")

pl.compare_heatmap(violations_df_opf, violations_df_drcc, threshold=0.05)

#pl.box_line_loading_two_subplots_percentile(opf_mc_line_results_df, drcc_mc_line_results_df)

#pl.box_line_loading_two_subplots(opf_mc_line_results_df, drcc_mc_line_results_df)
