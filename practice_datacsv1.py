import pandas as pd

import matplotlib.pyplot as plt
from sklearn import linear_model

from sklearn.preprocessing import StandardScaler

scale=StandardScaler()

df=pd.read_csv("data.csv")
X=df[['Volume', 'CO2']]
y=df['Weight']

scaledX=scale.fit_transform(X)

#predicting car weight
regr=linear_model.LinearRegression()
regr.fit(scaledX, y)
scaled=scale.transform([[3000,200]]) #Numeric Values
#predcted car weight
predicted_car_weight=regr.predict([scaled[0]])
print("Predicted Car weight:", predicted_car_weight) #predicted car weight of volume 3000
#And CO2 emission of 200cm3
plt.hist(y)
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.title('Histogram of car weights')
plt.show()