import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

housing = pd.read_csv("C:/Users/zacha/Desktop/tchdove2/Data science/BostonHousing.csv")
print(housing.head())

#linear regression

X = housing[["lstat","rm"]]
Y = housing["medv"]

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=5)

linear_model = LinearRegression()
linear_model.fit(x_train,y_train)

ytestpredict = linear_model.predict(x_test)
rootmeansquareerror = (np.sqrt(mean_squared_error(y_test,ytestpredict)))
print(rootmeansquareerror)


#polynomial regression

polytfeature = PolynomialFeatures(degree=2)
xtrainpoly = polytfeature.fit_transform(x_train)
polymodel = LinearRegression()
polymodel.fit(xtrainpoly,y_train)
xtestpoly = polytfeature.fit_transform(x_test)
ytestpredictpoly = polymodel.predict(xtestpoly)
rootmeansquareerrorpolymodel = (np.sqrt(mean_squared_error(y_test,ytestpredictpoly)))
print(rootmeansquareerrorpolymodel)

#graphical part
lstat = housing['lstat']
medv = housing['medv']
rm = housing['rm']

plt.subplot(221)
plt.scatter(x=lstat,y=medv,color='blue',marker='o')
plt.title("Boston housing (polynomial regression)")
plt.xlabel("LSTAT")
plt.ylabel("MEDV")


plt.subplot(222)
plt.scatter(x=rm,y=medv,color='red',marker='o')
plt.title("Boston housing (polynomial regression)")
plt.xlabel("RM")
plt.ylabel("MEDV")
plt.show()