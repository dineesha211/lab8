import numpy as np
import matplotlib.pyplot as plt
def dft(x):
  f=[]
  N=len(x)
  for i in range(0,N):
    X=[]
    for k in range(0,N):
        a=x[k]*(np.exp((-1j*2*np.pi*k*i)/N))
        X.append(a)
    f.append(sum(X))
  return f
y=[1,2,3,4,5,6,7,8,9,10]
p=dft(y)
k=np.arange(0,len(y))
s=int(input("enter no of zeros to be added:"))
for i in range(0,s):
	y.append(0)
l=y
F=dft(l)
h=np.arange(0,len(l))
plt.subplot(1,2,1)
plt.stem(k,np.abs(p))
plt.subplot(1,2,2)
plt.stem(h,np.abs(F))
plt.show()
