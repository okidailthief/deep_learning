from pand import *
from sklearn import *

allX, allY = readFile([5],[2]) # size, price

print(allX.shape)
print(allY.shape)

myModel = linear_model.LinearRegression()
myModel.fit(allX, allY)

print(myModel.coef_)
print(myModel.intercept_)

x1 = 0
y1 = x1 * myModel.coef_[0][0] + myModel.intercept_[0]

x2 = 12000
y2 = x2 * myModel.coef_[0][0] + myModel.intercept_[0]

plt.scatter(allX, allY)
plt.plot([x1,x2], [y1, y2]) # array of x's array of y's
plt.show()