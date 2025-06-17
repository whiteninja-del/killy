import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()

df=pd.read_csv("data.csv")
x=df[['CO2', 'Weight']]
scaledx=scale.fit_transform(x)
print(scaledx)

#The standardization method uses this formula:

#z = (x - u) / s 
#where z is the new value, x is the original value, u is the mean and s is the standard deviation


