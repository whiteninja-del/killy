import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()
df=pd.read_csv("iris.csv")
X=df[['sepal_length','petal_width']]
y=df['petal_length']
scaledX=scale.fit_transform(X)
#predicting petal length

regr=linear_model.LinearRegression
regr.fit(scaledX, y)
scaled=scale.transform([[5.0, 3.6]])
predicted_petal_length=regr.predict([scaled[0]])
print(predicted_petal_length)
print(scaledX)