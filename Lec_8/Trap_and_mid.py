import numpy as np
n=10000
a=0
x=0
b=2*np.pi
def f(x):
    return np.sin(x)
delx=(b-a)/n
A=0
A1=delx*((f(a)+f(b))/2)
for i in range(1,n):
    x=x+delx
    A=A+delx*f(x)
B=A+A1
print(B,'Trapezoidal rule')
#mid point rule
C=0
xi=a
for i in range(1,n+1):
    xi=xi+(i-0.5)*delx
    C=C+delx*f(xi)
print(C,'Mid point rule')
