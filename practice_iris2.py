import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()
df=pd.read_csv("iris.csv")
X=df[['sepal_width', 'petal_width']]
y=df['sepal_length']
scaledX=scale.fit_transform(X)

regr=linear_model.LinearRegression()
regr.fit(scaledX, y)
#predicted sepal length
scaled=scale.transform([[3.6, 0.5]])
predcited_sepal_length=regr.predict([scaled[0]])
print(predcited_sepal_length)