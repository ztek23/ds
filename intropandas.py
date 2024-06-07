import pandas as pd

df = pd.DataFrame({
    "Item": ["Desktop","Laptop","MacBook"],
    "Cpu": ["i5","i7","M2"],
    "Graphics": ["RTX 4060","iris Xe","M2"],
    "Ghz": [5.1,2.4,3.5]
})
"""
print(df.head())
print(df.shape)
print(df.info())
print(df["Item"])
print(df["Ghz"].max())
print(type(df["Graphics"]))
print(df["Cpu"].shape)
print(df.describe())
"""
csv = pd.read_csv("C:/Users/zacha/Desktop/tchdove/Data science/titanic.csv")

print(csv.head(5))
print(csv.shape)
print(csv.info())
print(csv.describe())
nameandage = csv[["Name","Age"]]
print(nameandage)

above35 = csv[csv["Age"]>35]
print(above35)

class1and2 = csv[(csv["Pclass"]==1) | (csv["Pclass"]==2)]
print(class1and2)
print(class1and2[["Name","Pclass"]])