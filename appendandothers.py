import numpy as np
arr=np.array([10,20,30])
arr2=np.append(arr,[40,50,60])
print(arr2)
"""np.concatenate(arr1,arr2,axis)
if axis is 0 arranges rowwise and if axis is 1 arranges columwise"""
arr3=np.concatenate((arr,arr2),0)
print(arr3)