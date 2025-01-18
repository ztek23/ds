import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data = pd.read_csv('iris.csv')
print(data.head())
print(data.info())

data['species'] = data['species'].replace({'setosa':0,'versicolor':1,'virginica':2})
'''
plt.subplot(221)
plt.scatter(data['petal_length'],data['species'],s=10,c='green',marker='o')

plt.subplot(222)
plt.scatter(data['petal_width'],data['species'],s=10,c='red',marker='o')

plt.subplot(223)
plt.scatter(data['sepal_length'],data['species'],s=10,c='blue',marker='o')

plt.subplot(224)
plt.scatter(data['sepal_width'],data['species'],s=10,c='orange',marker='o')

plt.show()
'''
Y = data['species']
X = data.drop('species',axis=1)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=1)
print(X_train.shape)
print(X_test.shape)

model = DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(X_train,Y_train)
predictions = model.predict(X_test)
print('accuracy',metrics.accuracy_score(predictions,Y_test))
