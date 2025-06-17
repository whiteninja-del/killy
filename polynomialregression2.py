import numpy
import matplotlib.pyplot as plt
from scipy import stats

cars=["BMW","Merc","Audi","Mustang","RAM","Evo","Mark-X","911"]
speed=[400,380,350,280,329,270,300,290]

x=cars
y=speed

polymodel=numpy.poly1d(numpy.polyfit(x,y,3))
line=numpy.linspace(250,450,100)

plt.scatter(x,y)
plt.plot(line,polymodel(line))
plt.show()