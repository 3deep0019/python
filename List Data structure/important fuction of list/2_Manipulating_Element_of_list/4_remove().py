#4) remove() Function:
#   ------->We can use this function to remove specified item from the list.If the item present 
 #          multiple times then only first occurrence will be removed.
n=[10,20,10,30] 
n.remove(10) 
print(n) 
#D:\Python_classes>py test.py 
#[20, 10, 30]
#  
#   If the specified item not present in list then we will get ValueError


n=[10,20,10,30] 
n.remove(40) 
print(n) 
#ValueError: list.remove(x): x not in list 

# Note: Hence before using remove() method first we have to check specified element 
#       present in the list or not by using in operator.