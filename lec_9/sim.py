def f(x):
	return 10-(3*x*x)
a=-1
b=3
def simpson13(a,b):
	h = (b - a) / 4
	integration = f(a) + f(b)
	for i in range(1,4):
		k = a + i*h
		if i%2 == 0:
			integration = integration + 2 * f(k)
		else:
			integration = integration + 4 * f(k)
	integration = integration * h/3
	return integration
result = simpson13(a, b)
print("Integration is: %0.6f" % (result) )
