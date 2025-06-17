import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()
df=pd.read_csv("iris.csv")
X=df[['sepal_length', 'petal_width']]
y=df['petal_length']
scaledX=scale.fit_transform(X)

regr=linear_model.LinearRegression()
regr.fit(scaledX, y)

#predicted petal length
scaled=scale.transform([[5.2, 0.2]])
predicted_petallength=regr.predict([scaled[0]])
print(predicted_petallength)