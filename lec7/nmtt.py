def f(x):
    return x**2-10
def g(x):
    return 2*x

def newtonrhapson(x0,N):

    step=1
    flag=1
    x1=x0-f(x0)/g(x0)
    print('Iteration-%d, x1=%0.6f and f(x1)=%0.6f' %(step,x1,f(x1)))
    x0=x1
    step=step+1

    if step>N:
       flag=0
       break

    if flag==1:
       print('Root is: %0.8f' %(x1))

x0=0
N=100
newtonrhapson(x0,N)
