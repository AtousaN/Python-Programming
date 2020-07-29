import numpy as np
import matplotlib.pyplot as plt
x = 5
y = pow(x,2)
z = pow(x,3)
theta = 90
sin = np.sin(theta)
cos = np.cos(theta)
print(sin,cos)
#angles used in radian
meshPoints = np.linspace(-1,1,500)
print (meshPoints[54])
plt.plot(meshPoints,np.sin(2*np.pi*meshPoints))
plt.show()
