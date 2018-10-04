import numpy as np


def readFile():
    myFile = open("kc_house_data.csv")
    all_x = []
    all_y = []

    # x1 = house size
    # x2 = year built
    # y = price

    for line in myFile.readlines()[1:]:
        try:
            currLine = line.split(",")
            all_x.append([int(currLine[5]), int(currLine[15])])
            all_y.append(int(currLine[2]))

        except Exception as e:
            all_x.pop()  # why do we pop if there's an error?
            pass
    x_np = np.array(all_x).reshape([len(all_x), 2])
    y_np = np.array(all_y).reshape([len(all_y), 1])
    return x_np, y_np


def get_y_hat(w_np, x1_np, x2_np, b):

    all_y_hat = np.sum(np.matmul(x1_np, w_np), np.matmul(x2_np, w_np))
    all_y_hat = all_y_hat + b
    return all_y_hat


def calc_error(y_np, y_hat):

    y_hat_minus_y = y_hat - y_np
    error = np.average(y_hat_minus_y ** 2)
    return error


def derive(y_np, x_np, b, w_np):

    der_resp_w1, der_resp_w2, der_resp_b = 0, 0, 0
    all_x1_np = x_np[:, 0].reshape([20121, 1])
    all_x2_np = x_np[:, 1].reshape([20121, 1])
    print(w_np.shape)
    #w1_np = w_np[:, 0].reshape([20121])
    #w2_np = w_np[:, 1].reshape([20121])
    #for num in enumerate(all_x1_np):
    der_resp_w1 = np.average((np.sum(np.matmul(w_np[0], all_x1_np + b) * -1 * all_x1_np)) * 2)
    der_resp_w2 = np.average((np.sum(np.matmul(w_np[1], all_x2_np + b) * -1 * all_x2_np)) * 2)
    der_resp_b = np.average((np.sum(np.matmul(w_np[0], all_x1_np) + np.matmul(w_np[1], all_x2_np) + b) - y_np) * 2)

    return der_resp_w1, der_resp_w2, der_resp_b
"""
def derive(allY, allX1, allX2, b, w1, w2):
    der_resp_w1, der_resp_w2, der_resp_b = 0, 0, 0

    for num, el in enumerate(allX1):
        der_resp_w1 = der_resp_w1 + (allY[num] - (w1 * allX1[num] + b)) * -1 * allX1[num]
        der_resp_w2 = der_resp_w2 + (allY[num] - (w2 * allX2[num] + b)) * -1 * allX2[num]
        der_resp_b = der_resp_b + (w1 * allX1[num] + w2 * allX2[num] + b) - allY[num]

    final_der_w1 = der_resp_w1 * (2 / len(allX1))
    final_der_w2 = der_resp_w2 * (2 / len(allX2))
    final_der_b = der_resp_b * (2 / len(allX2))
    return final_der_w1, final_der_w2, final_der_b
    """




def main():

    x_np, y_np = readFile()

    all_w = [10.0, 10.0]
    b = 10.0
    w_np = np.array(all_w)
    w_np.reshape([2, 1])
    print(w_np)

    all_x1_np = x_np[:, 0].reshape([20121, 1])
    all_x2_np = x_np[:, 1].reshape([20121, 1])
    y_hat = get_y_hat(w_np, all_x1_np, all_x2_np, b)

    error = calc_error(y_np, y_hat)
    print(error)

    #print(derive(y_np, x_np, b, w_np))

main()






