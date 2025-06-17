#normal data distribution
import numpy
import matplotlib.pyplot as plt

x=numpy.random.normal(5.0, 1.0, 100000)
#mean value is 5 and standard deviation is 1.0
# values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.

plt.hist(x, 100)
plt.show()
