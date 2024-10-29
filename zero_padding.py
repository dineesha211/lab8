import numpy as np
import matplotlib.pyplot as plt
x=[6,9,2,5,2,8,6,5,0,3]
N1=len(x)
f=[]
omega=np.arange(0,2*np.pi,(2*np.pi/len(x)))
for i in range(0,N1):
    X=[]
    for k in range(0,N1):
        a=x[k]*(np.exp((-1j*2*np.pi*k*i)/N1))
        X.append(a)
    f.append(sum(X))
print(f)
plt.subplot(1,2,1)
plt.plot(omega,f)
y=[6,9,2,5,2,8,6,5,0,3,0,0,0,0,0,]
N2=len(y)
omega1=np.arange(0,2*np.pi,(2*np.pi/len(y)))
g=[]
for i in range(0,N2):
   Y=[]
   for k in range(0,N2):
      b=y[k]*np.exp(-1j*(2*np.pi*k*i)/N2)
      Y.append(b)
   g.append(sum(Y))
print(g)
plt.subplot(1,2,2)
plt.plot(omega1,g)
plt.show()

