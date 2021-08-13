
'''
Accessing Elements of List:
We can access elements of the list either by using index or by using slice operator(:)

1)By using Index:
* List follows zero based index. ie index of first element is zero.
* List supports both +ve and -ve indexes.
* +ve index meant for Left to Right
* -ve index meant for Right to Left

'''
list = [10, 20, 30, 40] 
print(list[0]) # 10
print(list[-1]) # 40
print(list[10])#  IndexError: list index out of range

