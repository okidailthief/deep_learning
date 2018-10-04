import pandas as pd
import numpy as np

def readFile(_importColNums, _outputColNums):
    inputData = pd.read_csv("kc_house_data.csv",
                            sep=',',
                            usecols=_inputColNums,
                            header=0)
    outputData = pd.read_csv("kc_house_data.csv",
                            sep=',',
                            usecols=_inputColNums,
                            header=0)
    return np.array(inputData), np.array(outputData)
