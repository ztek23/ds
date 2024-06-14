import pandas as pd

titaniccsv = pd.read_csv("C:/Users/zacha/Desktop/tchdove/Data science/titanic.csv")

adultnames = titaniccsv.loc[titaniccsv["Age"]>18,"Name"]
print(adultnames)

print(titaniccsv.iloc[9:25,2:5])

titaniccsv.loc[0:2,"Name"] = "Zacharia Geevarghese"
print(titaniccsv["Name"].head())

titaniccsv.to_csv("C:/Users/zacha/Desktop/tchdove/Data science/titanic1.csv")

titaniccsv["test"] = titaniccsv["Fare"]+2
print(titaniccsv["test"])

titaniccsvrename = titaniccsv.rename(columns={"Pclass":"Class","Sex":"Gender"})
print(titaniccsvrename.info())

print(titaniccsv["Age"].mean())
print(titaniccsv[["Age","Fare"]].mean())
print(titaniccsv.agg({"Age":["min","max","median"],"Fare":["min","max","median"]}))

print(titaniccsv[["Sex","Age"]].groupby("Sex").mean())
print(titaniccsv["Pclass"].value_counts())
print(titaniccsv["Pclass"].count())

agesort = titaniccsv.sort_values(by="Age")
print(agesort.head())
classandagesort = titaniccsv.sort_values(by=["Pclass","Age"],ascending=False)
print(classandagesort.head())

titaniccsv["name"] = titaniccsv["Name"].str.lower()
print(titaniccsv["name"].head())

titaniccsv["Gender"] = titaniccsv["Sex"].replace({"male":"m","female":"f"})
print(titaniccsv["Gender"].head())
