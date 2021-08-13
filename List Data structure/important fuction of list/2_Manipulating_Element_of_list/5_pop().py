'''
5) pop() Function:
---> It removes and returns the last element of the list.
--> This is only function which manipulates list and returns some element.

'''
n=[10,20,30,40] 
print(n.pop()) 
print(n.pop()) 
print(n) 
'''
D:\Python_classes>py test.py 
40 
30 
[10, 20]

If the list is empty then pop() function raises IndexError

'''

n = [] 
print(n.pop()) #   IndexError: pop from empty list 
'''

Note:
1) pop() is the only function which manipulates the list and returns some value

2) In general we can use append() and pop() functions to implement stack datastructure 
   by using list,which follows LIFO(Last In First Out) order.
   In general we can use pop() function to remove last element of the list. But we can use to 
remove elements based on index.

--->*** n.pop(index)  To remove and return element present at specified index.
--->*** n.pop()  To remove and return last element of the list

'''
n = [10,20,30,40,50,60] 
print(n.pop()) #  60 
print(n.pop(1)) #  20 
print(n.pop(10)) #  IndexError: pop index out of range 



'''
Differences between remove() and pop()

remove() 
 1) We can use to remove special element
    from the List.

2) It returned removed element.

3) If special element not available then we
   get VALUE ERROR.

pop()
1) We can use to remove last element
  from the List.

2) It can’t return any value.

3) If List is empty then we get Error.


'''