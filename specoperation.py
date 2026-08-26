import numpy as np
arr=np.array([1,2,33,44,55,3])
print(arr[arr>20])
b=arr.reshape(3,2)
print(b)
""" .ravel=modifies original only if u modifies this 
.flatten=returns copy"""
c=b.flatten()
d=b.ravel()
c[0]=100
print(b)
d[0]=100
print(b)