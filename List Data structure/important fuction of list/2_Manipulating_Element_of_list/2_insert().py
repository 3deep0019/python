# 2) insert() Function:
 #  ----> To insert item at specified index position
n=[1,2,3,4,5] 
n.insert(1,888) 
print(n) 

#D:\Python_classes>py test.py 
n=[1, 888, 2, 3, 4, 5] 
n=[1,2,3,4,5] 
n.insert(10,777) 
n.insert(-10,)
print(n)


''' Note: If the specified index is greater than max index then element will be inserted at last 
          position. If the specified index is smaller than min index then element will be inserted at 
          first position


Differences between append() and insert()

    append() 
        ---------> In List when we add any element it will 
                come in last i.e. it will be last element.

    insert()
       --------->  In List we can insert any element in 
                   particular index number


'''