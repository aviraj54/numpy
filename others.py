##np.isnan(array) replace by true in only those place in which value is nan
import numpy as np
arr=np.array([1,2,3,np.nan])
print(np.isnan(arr))
#nan value is not comparatable
print(np.nan==np.nan)#so returns false we cant compare it

#replacing nan value
#we use np.nan_to_num(array,value)here default value is 0 for value
arr1=np.nan_to_num(arr)
print(arr1)##replaces by0
arr2=np.nan_to_num(arr,nan=5)
print(arr2)