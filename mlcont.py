#histogram
import numpy 
import matplotlib.pyplot as plt

#big data distributions
#10000 random numbers and disply them in 100 bars
x=numpy.random.uniform(0.0, 2.0, 10000)

plt.hist(x, 100)
plt.show()

