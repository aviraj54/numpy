##identity matrix
import numpy as np
a=np.eye(3)
print(a)

##array properties
a_2d=np.array([[1,2,3],
               [2,4.0,4],
               [3,4,5]])
print(a_2d.shape,a_2d.size)

#dimension
print(a_2d.ndim)

##for 3d array
a_3d=np.array([[[1,2],[3,2]]])
print(a_3d.ndim)

##datatype dtype of elements of data
print(a_2d.dtype)#if one also becomes float it returns matching


