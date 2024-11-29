import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('example_averages.csv')

xdata = df['pnbi']
ydatas = ['ni0','ti0','taue','tripleprod']

fig, ax = plt.subplots(len(ydatas), sharex=True)

for i, var in enumerate(ydatas):
    ydata = df[var]
    yerr = df[f'{var}_std']
    ax[i].plot(xdata,ydata,label='Average')
    ax[i].fill_between(xdata,ydata-yerr,ydata+yerr, alpha=0.2, label='Standard Deviation')
    ax[i].set_ylabel(var)
    
ax[0].set_title('Parameters vs (Measured) NBI Power')
ax[-1].set_xlabel('PNBI (W)')
plt.legend()
plt.subplots_adjust(hspace=0)
plt.show()


plt.plot(df['pnbi_input'],df['pnbi']*1e-6)
plt.show()