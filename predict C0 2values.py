import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

df=pd.read_csv("data.csv")
X=df[['Weight', 'Volume']]
y=df['CO2']
scaledX=scale.fit_transform(X)
regr=linear_model.LinearRegression()
regr.fit(scaledX,y)

scaled=scale.transform([[2300, 1.3]])

predicted_car=regr.predict([scaled[0]])
print(predicted_car)
