import pandas as pd
from path import path

###
# 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S ###

## PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked ##

## 1) Passenger ID

## 2) Survived 0 = No, 1 = Yes

## 3) Pc Class = Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd

## 4) Name = Clean

## 5) Sex is Male and Female male = 0, female = 1

## 6) Age, INT

## 7) siblings and spouses INT

## 8) Number of parents and children 

## 9) Ticket Number In letter/number format (Convert letter to integer)

## 10) Fare INT

## 11) Cabin lots of missing data Consider wiping?

## 12) Embarked Location C = Cherbourg, Q = Queenstown, S = Southampton

# Calls csv from imported path and assigns unclean data to data frame.
unclean_data = pd.read_csv(path)
df = pd.DataFrame(unclean_data)

# Drops name from the data frame
df = df.drop('Name', axis =1)

#Fills all NaN with 0
df = df.fillna(0)

# Changes Sex to a numerical value
df['Sex'] = (
    df["Sex"]
        .map({"male": 1, "female": 2})
        .fillna(0)
        .astype(int)
)

# Changes embarked to a numerical value
df['Embarked'] = (
    df["Embarked"]
        .map({'S': 1, 'C': 2, 'Q': 3})
        .fillna(0)
        .astype(int)
)

#df['Cabin'] = df['Cabin'].astype(float)

print(df)

# Numericizes values into numpy array
df = df.to_numpy()

print(df)