#np.isinf(array)checks wheather there is infinity or not in array
import numpy as np
arr=np.array([1,2,np.inf,-np.inf])
print(np.isinf(arr))
arr2=np.nan_to_num(arr,posinf=6,neginf=3)#replacement of infinity
print(arr2)