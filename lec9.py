def f(x):
	return 10-(x*x)
def trapezoidal(x0,xn,n):
	h = (xn - x0)/n
	integration = f(x0) + f(xn)
	i=1
	while i<n:
		integration+=2*f(x0+i*h)
		i+=1
	integration = integration*h/2
	return integration
lower_limit=-2
upper_limit=2
sub_interval=8
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (result) )
                                                                   
