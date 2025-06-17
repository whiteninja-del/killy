#speed of a ten year old car
import matplotlib.pyplot as plt
from scipy import stats
x=[1,2,3,4,5,6,7,8,9,11,12]
y=[240,220,210,200,190,185,182,180,176,156,150]

slope, intercept, r, p, std_err=stats.linregress(x,y)
def myfunc(x):
    return slope *x + intercept
speed=myfunc(10)

mymodel=list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()
print(speed)
