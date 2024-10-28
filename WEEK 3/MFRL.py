import numpy as np
from functools import reduce

np.num=[2,3,6,9,10]
np.num1=[[1,3,5],[7,9],[11,13,15]]

cubed=list(map(lambda cube:(cube **3),np.num))
print("using map function",cubed)

even =list(filter(lambda x:(x% 2== 0),np.num))
print ("using filter function",even)

re=reduce(lambda x, y: x+y,np.num)
print ("using reduce fuction",re)
