"""
as arr+2 addup to every element similarly in multidimensional array
[[],[]] each []acts
as element.
"""
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1+[10,20,30])
#broadcasting is only possible if size of to be add array is 
#size of one element
"""for eg:
if a=[[1,2],[3,4]] then to be add =[1,2,3] then error if its
only [1,2] then program will run fluently
"""
a=np.array([1,2,3])
print(a+[10,20,30])##gets added and this also is possible
#but without array it could be:
a1=[1,2,3]
r=[x+y for x,y in zip(a1,[10,20,30])]
print(r)