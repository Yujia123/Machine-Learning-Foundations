import numpy as np


# Question 4
# N=10000
N=5
dvc=50
delta=0.05

def mH(N):
    return float(N**dvc)


v1=np.sqrt(8.0/N*np.log(4.0*mH(2*N)/delta))
v2=np.sqrt(2.0*np.log(2.0*N*mH(N))/N)+np.sqrt(2.0/N*np.log(1.0/delta))+1.0/N
v3=np.sqrt(1.0/N*(2*0.05+np.log(6.0*mH(2*N)/delta)))
# v4=np.sqrt(1.0/(2.0*N)*(4.0*0.05*1.05+np.log(4.0*mH(N**2)/delta)))
# v5=np.sqrt(16.0/N*np.log(2.0*mH(N)/np.sqrt(delta)))

# print(v1,v2,v3,v4,v5)
