import numpy as np
from pand import *

allX, allY = readFile([5,14], [2])

def calcYHat(w, x, b):
    ans = np.sum(w * x.transpose()) + b


def calcError(_w, _x, _b, _y):
    for index, el, in enumerate(_x):
        myResult = myResult + (_y[index] - calcYHat(_w, _x, _b)) ** 2
    return myResult/len(_x)

def main():
    learningRate = .000001
    w = np.array([[0.0], [0.0]]) # 2x1 matrix
    b = 0
    for el in range(1000):
        der_resp_w1 = 0
        for index, currElement in enumerate(allX):
            der_resp_w1 = allY[index] - calcYHat(w, currElement, b) - allY[index]

            der_resp_w1 = der_resp_w1 * 2 / len(allX)

            w[0][0] = w[0][0] - learningRate * der_resp_w1

            print("w[0][0]: ", str(w[0][0]))
            print("total error is: ", str(calcError(w, allX, b, allY)))