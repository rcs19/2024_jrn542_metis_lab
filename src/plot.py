"""
Create a stacked plot of chosen variables against PNBI (neutral beam injeciton power).  
"""
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('averages_with1to10integers.csv')  # Dataset generated by main.py
df = df[df['pnbi_input']<11]                        # Filter
xdata = df['pnbi']*1e-6                             # x-data in mega-watts MW  
ydatas = ['ni0','ti0','taue','tripleprod']          # list of y-variables to include in stacked plot.

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
    
ax[0].set_title('Parameters vs (Measured) NBI Power')
ax[-1].set_xlabel('PNBI (MW)')
plt.legend()
plt.subplots_adjust(hspace=0)
plt.show()


plt.plot(df['pnbi_input'],df['pnbi']*1e-6)
plt.xlabel("Input Parameter (MW)")
plt.ylabel("Measured Parameter (MW)")
plt.title("Input vs Measured PNBI")
plt.show()