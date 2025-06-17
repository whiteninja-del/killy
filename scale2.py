import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()
df=pd.read_csv("data.csv")
X=df[['Volume', 'CO2']]
y=df['Weight']

regr=linear_model.LinearRegression()
scaledX=scale.fit_transform(X)
regr.fit(X,y)
print(scaledX)
