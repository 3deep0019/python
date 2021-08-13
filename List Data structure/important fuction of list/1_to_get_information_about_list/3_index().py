# 3) index():
 #   --------> Returns the index of first occurrence of the specified item.
n = [1, 2, 2, 2, 2, 3, 3] 
print(n.index(1)) #  0 
print(n.index(2)) #  1 
print(n.index(3)) # 5 
#print(n.index(4)) # ValueError: 4 is not in list

'''
Note: If the specified element not present in the list then we will get ValueError.Hence 
      before index() method we have to check whether item present in the list or not by using in 
    operator.

print( 4 in n)  False

'''
