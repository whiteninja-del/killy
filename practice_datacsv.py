import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()

df=pd.read_csv("data.csv")
X=df[['Volume', 'CO2']]
y=df['Weight']
scaledX=scale.fit_transform(X)

regr=linear_model.LinearRegression()
regr.fit(scaledX,y)
#predicted weight
scaled=scale.transform([[2000,100]])
predicted_weight=regr.predict([scaled[0]])
print("Predicted Car Weight of 2000 volume and 100 co2 emission:", predicted_weight)