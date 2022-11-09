import math as m
import matplotlib.pyplot as p
def f(x):
    return x*x-9
def df(x):
    return 2*x
x=5
e=0.00001
a=[]
for i in range(0,100):
    if abs(f(x))>e:
     x=x-(f(x)/df(x))
     a.append(x)
    else:
     print('The no of iterations:',i)
     break    
print(x)
p.plot(a)
p.show()
def g(x):
    return m.tanh(x)
def dg(x):
    return (1/(m.cosh(x))**2)
x=1
for i in range(0,100):
    x=x-(g(x)/dg(x))
print(x)
