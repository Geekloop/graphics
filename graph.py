from pylab import *
import matplotlib.pyplot as plt
import numpy as np

x = linspace(-4, 5, 5)
y = x ** 2
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('Python')
show()