import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def readFile(_importColNums, _outputColNums):
    inputData = pd.read_csv("kc_house_data.csv",
                            sep=',',
                            usecols=_importColNums,
                            header=0)
    outputData = pd.read_csv("kc_house_data.csv",
                            sep=',',
                            usecols=_outputColNums,
                            header=0)
    return np.array(inputData), np.array(outputData)
