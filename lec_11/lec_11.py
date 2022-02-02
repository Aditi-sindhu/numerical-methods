import numpy as np
from scipy.interpolate import CubicSpline
x=np.array([0,1,2])
y=np.array([1,2,4])
f = CubicSpline(x, y)
print("value is",f(1.5))
def g(x):
	return 2**x
print("original value is",g(1.5))
