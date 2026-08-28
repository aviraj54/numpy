"""
hstack()--horizontal stacking (rowwise)
vstack()--vertical stacking (colwise)
"""
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
r_1=np.hstack((arr1,arr2))
r_2=np.vstack((arr1,arr2))
print(r_1,r_2)
arr3=np.split(r_2,2)
print(arr3)
arr4=np.vsplit(r_2,2)##only can do split for inside matrix [2,3]cant be splited from 2 and 3
print(arr4)
arr5=np.hsplit(r_2,3)#split rows in 3 parts like 1 array
print(arr5)
