#import matplotlib.pyplot as plt
#import numpy as np


def readFile():

    myFile = open("kc_house_data.csv")
    allX1 = []
    allX2 = []
    allY = []

    # x1 = house size
    # x2 = year built
    # y = price

    for line in myFile.readlines()[1:]:
        try:
            currLine = line.split(",")
            allX1.append(int(currLine[5]))
            allX2.append(int(currLine[15]))
            allY.append(int(currLine[2]))

        except Exception as e:
            allX1.pop()  # why do we pop if there's an error?
            pass

    return allX1, allX2, allY


def getYHat(w1, w2, x1, x2, b):
    yHat = 0
    yHat = ((w1 * x1) + (w2 * x2) + b)

    return yHat


def calcError(w1, w2, allX1, allX2, allY, b):
    totalError = 0
    for num, el in enumerate(allX1):
        totalError = totalError + (getYHat(w1, w2, allX1[num], allX2[num], b) - allY[num]) ** 2
    return totalError / len(allX1)


def derive(allY, allX1, allX2, b, w1, w2):
    der_resp_w1, der_resp_w2, der_resp_b = 0, 0, 0

    for num, el in enumerate(allX1):
        der_resp_w1 = der_resp_w1 + (allY[num] - getYHat(w1, w2, allX1[num], allX2[num], b)) * -1 * allX1[num]
        der_resp_w2 = der_resp_w2 + (allY[num] - getYHat(w1, w2, allX1[num], allX2[num], b)) * -1 * allX2[num]
        der_resp_b = der_resp_b + (w1 * allX1[num] + w2 * allX2[num] + b)

    final_der_w1 = der_resp_w1 * (2 / len(allX1))
    final_der_w2 = der_resp_w2 * (2 / len(allX2))
    final_der_b = der_resp_b * (2 / len(allX2))
    return final_der_w1, final_der_w2, final_der_b


"""
der_respect_to_m = 0
        for num, el in enumerate(all_x):
            #this formula differs from my notes
            der_respect_to_m = der_respect_to_m + (all_y[num] - (initialM * all_x[num] + initialB)) * -1 * all_x[num]

        der_respect_to_m = der_respect_to_m / 50 # same as multiplying by 2/sample size

        initialM = initialM - learning_rate * der_respect_to_m
        """

def main():


    allX1, allX2, allY = readFile()

    w1 = 10
    w2 = 10
    b = 10
    learning_rate = .00000001
    for el in range(5000):
        error = calcError(w1, w2, allX1, allX2, allY, b)
        print("Error: ", error)

        derivatives_wrt = derive(allY, allX1, allX2, b, w1, w2)
        print("derivative WRT w1/w1/b: ", derivatives_wrt)
        w1 = w1 - learning_rate * derivatives_wrt[0]
        w2 = w2 - learning_rate * derivatives_wrt[1]
        b = b - learning_rate * derivatives_wrt[2]

main()
