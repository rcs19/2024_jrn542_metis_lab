"""
Iterates through data files in a specified folder and stores specified variables into a pandas dataframe.
Assumes filenaming convention follows "P{}_B{}_I{}_N{}.mat"
1. Specify directory in `directory`
2. Specify variables to record in list.
3. Run
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
for filename in os.listdir(directory)[:3]:
    try:
        file_string = os.path.join(directory, filename).replace('\\','/')   # example string: 'data/P1_B1_Idefault_Ndefault.mat'
        dataset = scipy.io.loadmat(file_string)
    except:
        print(f"Error: {file_string} is probably corrupted or you have incorrectly entered directory.")

    pnbi_input = float(filename.split('_')[0][1:])                          # PNBI input assuming file-naming convection 

    # Calculate average and standard deviation between index 50 and 100 for each variable specified
    row = [pnbi_input, ]
    for var in variables:   
        var_avg, var_std = get_average(50, 100, index=var, dataset=dataset)
        row.extend([var_avg, var_std])
    rows.append(row)
    ti0err = np.sqrt((row[4]/row[5])**2 + (row[6]/row[7])**2)
    print(ti0err)

df = pd.concat([df, pd.DataFrame(rows, columns=columns)], ignore_index=True)
    
# Calculate ti0, tripleproduct, and their standard deviations #
df['ti0'] = df['te0'] * df['tite']
df['ti0_std'] = np.linalg.norm([df['te0']/df['te0_std'], df['tite']/df['tite_std']], axis=0)

df['tripleprod'] = df['ni0'] * df['ti0']*df['taue']
df['tripleprod_std'] = np.linalg.norm([df['ni0']/df['ni0_std'], df['ti0']/df['tite_std'], df['taue']/df['taue_std']], axis=0)

print(df)
