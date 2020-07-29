import numpy as np
import matplotlib.pyplot as plt
"""
x = np.linspace(0,10,100)
f = np.exp(-x/10)*np.sin(np.pi*x)
g = x*np.exp(-x/3)
fig = plt.figure()
plt.plot(x, f, label='f(x)')
plt.plot(x, g, label='g(x)')
fig.suptitle('f & g plot')
plt.xlabel('interval')
plt.ylabel('function result')
plt.legend()
plt.show()
"""


theta = np.linspace(0,2*np.pi,100)
cardioid = 1.0 + np.cos(theta)
limacon08 = 0.8 + np.cos(theta)
limacon12 = 1.2 + np.cos(theta)
x_cardioid = cardioid * np.cos(theta)
x_limacon08 = limacon08 * np.cos(theta)
x_limacon12 = limacon12 * np.cos(theta)
y_cardioid = cardioid * np.sin(theta)
y_limacon08 = limacon08 * np.sin(theta)
y_limacon12 = limacon12 * np.sin(theta)
fig = plt.figure()
plt.plot(x_cardioid, y_cardioid, label='cardioid')
plt.plot(x_limacon08, y_limacon08, label='limacon0.8')
plt.plot(x_limacon12, y_limacon12, label='limacon1.2')
fig.suptitle('cardioid and limacon plots')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

