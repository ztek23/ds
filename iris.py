import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics #to calculate accuracy

iris = pd.read_csv("iris.csv")
print(iris.head()) #pre proccessing
iris["species"] = iris["species"].replace({"setosa":0,"versicolor":1,"virginica":2})
print(iris.head())
#Basic data-analysis

plt.subplot(221) #creates a subplot in a 2x2 grid (1st position)
plt.scatter(iris["sepal_length"],iris["species"],s=10,c="green",marker="o")
plt.xlabel("sepal length")
plt.ylabel("species")

plt.subplot(222)
plt.scatter(iris["sepal_width"],iris["species"],s=10,c="blue",marker="o")
plt.xlabel("sepal width")
plt.ylabel("species")

plt.subplot(223)
plt.scatter(iris["petal_length"],iris["species"],s=10,c="red",marker="o")
plt.xlabel("petal length")
plt.ylabel("species")

plt.subplot(224)
plt.scatter(iris["petal_width"],iris["species"],s=10,c="orange",marker="o")
plt.xlabel("petal width")
plt.ylabel("species")

plt.show()

Y = iris["species"]
X = iris.drop("species",axis=1)
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=1)
print(x_train.shape)
print(x_test.shape)

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
prediction = model.predict(x_test)
accuracy = metrics.accuracy_score(prediction, y_test)
print(accuracy)

