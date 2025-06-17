import matplotlib.pyplot as plt
from scipy import stats
#linear regression-find the relationship between variables
age=[2,3,4,5,6,7,8,9,1,10]
speed=[56,76,89,98,87,75,64,42,77,88]

slope, intercept, r,p, std_err=stats.linregress(age,speed)

def myfunc(age):
    return slope *age + intercept
mymodel=list(map(myfunc, age))
plt.scatter(age,speed)
plt.plot(age, mymodel)
plt.show()
