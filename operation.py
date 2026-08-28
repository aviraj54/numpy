import numpy as np
arr=np.array([1,2,3])
print(arr+2,arr)
#insert function
n_arr=np.insert(arr,2,4,None)##insert value in that position and will pull other position sideways
print(n_arr)#cant save modifications in array__must create new array for it
#axis =0 means rows and 1 means column
arr2=np.array([[1,2,3],[4,5,6]])
n_arr2=np.insert(arr2,2,4,0)
n_arr3=np.insert(arr2,3,7,1)
print("final::")
print(n_arr2,n_arr3)