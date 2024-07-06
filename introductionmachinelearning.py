import numpy as np
import pandas as pd
import matplotlib as mp
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("C:/Users/zacha/Desktop/tchdove/Data science/Data.csv")
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values
print(x)
print()
print(y)
 
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
print(x)
ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder='passthrough')
x = np.array(ct.fit_transform(x))
print(x)

le = LabelEncoder()
y = le.fit_transform(y)
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

sc = StandardScaler()
x_train[:,3:] = sc.fit_transform(x_train[:,3:])
x_test[:,3:] = sc.transform(x_test[:,3:])
print(x_train)
print(x_test)