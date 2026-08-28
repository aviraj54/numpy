import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([[1,2],[3,4]])
res_1=np.delete(arr1,2,0)
res_2=np.delete(arr2,1,1)
print(res_1,res_2)