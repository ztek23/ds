from cProfile import label
import numpy as np
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as mp

x = [0,4,0.8,9,45,5]
y = [7,25,46,89,91,0.1]

def findmean(a):
    n = len(a)
    print(sum(a))
    return sum(a)/n

meanx = findmean(x)
meany = findmean(y)

numerator = 0
denominator = 0

for i in range(len(x)):
    numerator = numerator + ((x[i]-meanx) * (y[i]-meany))
    denominator = denominator + pow((x[i]-meanx),2)

print("The numerator is", numerator)
print("The denominator is", denominator)

slope = numerator/denominator
intercept = round(meany - meanx * slope,1)
print("The slope is", slope)
print("The intercept is", intercept)

X = np.array([[0],[4],[0.8],[9],[45],[5]])

Y = np.array([[7],[25],[46],[89],[91],[0.1]])

regression = lr().fit(X,Y)
print("The slope is", regression.coef_)
print("The intercept is", regression.intercept_)

mp.scatter(X,Y,color='blue',marker='o',label="datapoints")
mp.plot(X,regression.predict(X),color='red',label="prediction")
mp.xlabel("x")
mp.ylabel("y")
mp.title("Linear regression prediction and manual input")
mp.legend()
mp.show()