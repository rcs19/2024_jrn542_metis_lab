import scipy.io
import numpy as np
from matplotlib import pyplot as plt

full_dataset = scipy.io.loadmat("data/P20_B1_Idefault_Ndefault.mat")    

def list_subsections():
    print("subsections (I'm using zerod by default):")
    print(full_dataset['post'].dtype)


def list_indexes(subsection='zerod'):
    print("indexes in subsection " + subsection + ":")
    print(full_dataset['post']['zerod'][0][0].dtype)


def get_variable(index, subsection='zerod'):
    a = full_dataset['post'][subsection][0][0][index][0][0]
    a = [float(x[0]) for x in a]
    return a

def get_average(start, end, index, subsection='zerod'):
    a = get_variable(index, subsection=subsection)
    return (np.mean(a[start:end]), np.std(a[start:end]))

if __name__ == "__main__":
    list_subsections()
    list_indexes()
    print("(Mean,Std) =",get_average(50, 100, 'taue'))
    plt.plot(get_variable('taue'))
    plt.show()
