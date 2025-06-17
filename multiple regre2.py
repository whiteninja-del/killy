import pandas as pd
from sklearn import linear_model

df=pd.read_csv("data.csv")
X=df[['Weight', 'Volume']]
y=df['CO2']

regr=linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)