"""
Minor edit to original processing.py by adding `dataset` as an 
argument to all functions so that it can be called from main.py.
"""

import scipy.io
import numpy as np
from matplotlib import pyplot as plt


def list_subsections(dataset):
    print("subsections (I'm using zerod by default):")
    print(dataset['post'].dtype)


def list_indexes(dataset, subsection='zerod'):
    print("indexes in subsection " + subsection + ":")
    print(dataset['post']['zerod'][0][0].dtype)


def get_variable(index, dataset, subsection='zerod'):
    a = dataset['post'][subsection][0][0][index][0][0]
    a = [float(x[0]) for x in a]
    return a

def get_average(start, end, index, dataset, subsection='zerod'):
    """Get the average of the specified variable over specified range. Example usage:
    `get_average(50, 100, 'taue')` finds the average of taue between indices 50 and 100"""
    a = get_variable(index, dataset, subsection=subsection)
    return (np.mean(a[start:end]), np.std(a[start:end]))

# Code to execute if this file is run
if __name__ == "__main__":
    dataset = scipy.io.loadmat("data/P1.5_B1_Idefault_Ndefault.mat")    
    list_subsections()
    list_indexes()
    print("(Mean,Std) =",get_average(50, 100, 'taue'))
    plt.plot(get_variable('taue'))
    plt.show()
