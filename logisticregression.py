import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

titanic = pd.read_csv("C:/Users/zacha/Desktop/tchdove2/Data science/titanic.csv")

print(titanic.isnull().sum())

print("The median of age column is: ",titanic["Age"].median(skipna=True))
print("Percent of missing records in cabin",titanic["Cabin"].isnull().sum()/titanic.shape[0]*100)
print("Most common boarding point", titanic["Embarked"].value_counts().idxmax())

titanic["Age"].fillna(titanic["Age"].median(skipna=True),inplace=True)
titanic["Embarked"].fillna(titanic["Embarked"].value_counts().idxmax(),inplace=True)
titanic.drop("Cabin",axis=1,inplace=True)

print(titanic.isnull().sum())

lrmodel = LogisticRegression()
titanic.drop("PassengerId",axis=1,inplace=True)
titanic.drop("Name",axis=1,inplace=True)
titanic.drop("Ticket",axis=1,inplace=True)
titanic.drop("SibSp",axis=1,inplace=True)
titanic.drop("Parch",axis=1,inplace=True)

label_encoder = preprocessing.LabelEncoder()
titanic["Sex"] = label_encoder.fit_transform(titanic["Sex"])
titanic["Embarked"] = label_encoder.fit_transform(titanic["Embarked"])

X = titanic[["Pclass","Sex","Age","Fare","Embarked"]]
Y = titanic["Survived"]

xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.2,random_state=2)

lrmodel.fit(xtrain,ytrain)

ypred = lrmodel.predict(xtest)
print(classification_report(ytest,ypred))

matrix = confusion_matrix(ytest,ypred)
sns.heatmap(matrix,annot=True,fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()