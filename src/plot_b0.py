"""
Create a stacked plot of chosen variables against PNBI (neutral beam injeciton power).  
"""
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('b0_averages.csv')  # Dataset generated by main.py
# df = df[df['pnbi_input']<40]                        # Filter
xdata = df['input']                             # x-data in mega-watts MW  
ydatas = ['betan','ni0','ti0','taue','tripleprod']          # list of y-variables to include in stacked plot.

# Create stacked plot with shared x-axis ('pnbi')
fig, ax = plt.subplots(len(ydatas), sharex=True)    

# Iterate through chosen y-variables and plot on a separate axis each
for i, var in enumerate(ydatas):
    ydata = df[var]
    yerr = df[f'{var}_std']
    ax[i].plot(xdata,ydata,label='Average')

    # Plot error as shaded region 
    ax[i].fill_between(xdata,ydata-yerr,ydata+yerr, alpha=0.2, label='Standard Deviation') 
    ax[i].set_ylabel(var)
    
ax[0].set_title('Parameters vs B0')
ax[-1].set_xlabel('B0 (T)')
plt.legend()
plt.subplots_adjust(hspace=0)
plt.show()