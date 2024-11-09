# importing libraries


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("student-mat.csv")
data.head()

data.describe()
data.info()

label_encoder = LabelEncoder()
columns = ["school", "sex", "famsize", "Pstatus", "Mjob", "Fjob", "reason", "guardian", "schoolsup", "famsup", "paid", "activities", 
           "nursery", "higher", "internet", "romantic"]
data[columns] = data[columns].apply(label_encoder.fit_transform)

data.drop("G1", axis = 1, inplace = True)
data.drop("G2", axis = 1, inplace = True)

X = data[["school", "sex", "age", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian", "traveltime", "studytime", "failures", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences"]]

Y = data["G3"]

X.dtypes

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 5)

classifier = RandomForestClassifier(n_estimators = 100)
classifier.fit(X_train, Y_train)

y_pred = classifier.predict(X_test)
print(y_pred)

matrix = confusion_matrix(Y_test, y_pred)
sns.heatmap(matrix, annot = True, fmt = "d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

print(classification_report(Y_test, y_pred))