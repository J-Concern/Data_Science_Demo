import pandas
from sklearn import linear_model

#call cleaned csv
df = pandas.read_csv(r"C:\Users\Caleb\Desktop\git\Data_Science_Demo\cleandata")

#drop NaNs
df_clean = df.dropna()

#declare dependent and independent values
x = df_clean[["Pclass","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]]
y = df_clean["Survived"]

# Run linear Regression
regr = linear_model.LinearRegression()
regr.fit(x,y)

# Get coefficients and intercept
coefficients = regr.coef_
intercept = regr.intercept_
feature_names = x.columns

# Build the regression equation
equation = f"y = {intercept:.4f}"
for coef, feature in zip(coefficients, feature_names):
    equation += f" + ({coef:.4f} * {feature})"


# a rudimentary survial prediction formula note that some of the data is statstically insignificant.
def surival_prediction(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked):
    y = (
        0.0423 
        + (-0.1476 * Pclass) 
        + (0.5119 * Sex) 
        + (-0.0027 * Age)
        + (-0.0374 * SibSp) 
        + (-0.0052 * Parch) 
        + (0.0004 * Fare) 
        + (0.0298 * Embarked)
        # the moral of this is basically we can cut the data down to 4 units.
    )
    return y