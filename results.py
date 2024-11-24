"""
Code for the publication AI-Enhanced Distributionally Robust Chance
Constrained Optimization for Managing Uncertainty in Heat Pump Dominated 
Residential Energy Systemsby Marwan Mostafa 

Results File
"""
###############################################################################
## IMPORT PACKAGES & SCRIPTS ## 
###############################################################################
#### PACKAGES ####
import pickle as pkl

#### SCRIPTS ####
import parameters as par


###############################################################################
## FUNCTIONS ##
###############################################################################

def save_optim_results(results, filename):
    try:
        with open(filename, 'wb') as file:
            pkl.dump(results, file)
        print(f"Results successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the results: {e}")

def load_optim_results(filename):
    try:
        with open(filename, 'rb') as file:
            results = pkl.load(file)
        print(f"Results loaded successfully from {filename}.")
        return results
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except pkl.UnpicklingError:
        print(f"Error: Unable to load the file {filename}. It may not be a valid pickle file.")
        return None
    

def curtailment_calculation(results, load_profile):
    # Assuming the flexible load is at the first bus
    bus = 2
    curtailment_factor = []

    # Loop through each timestep to calculate curtailment
    for t in range(len(results['load'])):
        # Get the expected (input) load from the profile and actual load from the results
        expected_load = load_profile['P_HEATPUMP_smooth'].iloc[t] / par.hp_scaling
        actual_load = results['load'][t][bus]

        # Calculate the curtailment factor
        curtailment = (expected_load - actual_load) / expected_load if expected_load != 0 else 0
        curtailment_factor.append(curtailment)

    return curtailment_factor

# Check and convert string representations of lists back to actual lists if necessary
def convert_to_list_if_needed(cell):
    if isinstance(cell, str):
        return eval(cell)
    return cell

