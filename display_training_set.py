import sys
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 

np.random.seed(2)

#12 number of customers
x=np.random.normal(4,5,12)
y=np.random.normal(20000,5000,12) / x 
#amount of money spent before making a purchase

#training
train_x=x[:80]
train_y=y[:80]
#testing
test_x=x[80:]
test_y=y[80:]

plt.scatter(train_x,train_y)
plt.show()

#make the compiler able to draw
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()