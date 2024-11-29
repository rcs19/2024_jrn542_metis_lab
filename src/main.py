"""
Script which iterates through data files in a specified folder and stores specified variables into a pandas dataframe. The ion density `ni0` and triple product `triplepro` is calculated from the averages. This dataframe is exported as a `.csv`.
Assumes filenaming convention follows "P{}_B{}_I{}_N{}.mat"
"""
import scipy.io
import pandas as pd
import numpy as np
import os
 
from processing import get_average

# Parameters #
directory = 'data/'                           # Filepath
variables = ['pnbi','ni0','te0','tite','taue']  # Variables to record (must be valid variables names in the data)

# Create list of columns for DataFrame
columns = ['pnbi_input']
for var in (variables):
    columns.append(var)           # Original variable
    columns.append(f"{var}_std")  # Corresponding standard deviation column e.g. `pnbi_std`
                                                          
# Create our DataFrame (table of data) 
df = pd.DataFrame(columns=columns)

# Iterate through files in specified directory #
rows = []
for filename in os.listdir(directory):
    try:
        file_string = os.path.join(directory, filename).replace('\\','/')   # example string: 'data/P1_B1_Idefault_Ndefault.mat'
        dataset = scipy.io.loadmat(file_string)
    except:
        print(f"Error: {file_string} is probably corrupted or you have incorrectly entered directory.")

    pnbi_input = float(filename.split('_')[0][1:])                          # PNBI input assuming file-naming convection 

    # Calculate average and standard deviation between index 50 and 100 for each variable specified
    row = [pnbi_input]
    for var in variables:   
        var_avg, var_std = get_average(50, 100, index=var, dataset=dataset)
        row.extend([var_avg, var_std])
    rows.append(row)

df = pd.concat([df, pd.DataFrame(rows, columns=columns)], ignore_index=True)
df = df.sort_values(by='pnbi_input').reset_index(drop=True)

# Calculate ti0, tripleproduct, and their standard deviations #
df['ti0'] = df['te0'] * df['tite']
df['ti0_std'] = df['ti0'] * np.linalg.norm([df['te0_std']/df['te0'], df['tite_std']/df['tite']], axis=0)

df['tripleprod'] = df['ni0'] * df['ti0']*df['taue']
df['tripleprod_std'] = df['tripleprod'] * np.linalg.norm([df['ni0_std']/df['ni0'], df['tite_std']/df['tite'], df['taue_std']/df['taue']], axis=0)

print(df)
df.to_csv("averages.csv", index=False)  