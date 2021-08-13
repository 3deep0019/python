# del Statement:
#          -------> del is a keyword in Python.

#          ------> After using a variable, it is highly recommended to delete that variable if it is no longer 
#                 required,so that the corresponding object is eligible for Garbage Collection.

#         ----> We can delete variable by using del keyword.
x = 10 
print(x) 
del x


# After deleting a variable we cannot access that variable otherwise we will get NameError.
x = 10 
del x 
print(x) 

# NameError: name 'x' is not defined.

# Note: We can delete variables which are pointing to immutable objects.But we cannot 
# delete the elements present inside immutable object.

# s = "durga" 
# print(s) 
# del s  ---> valid  
# 4) del s[0]  TypeError: 'str' object doesn't support item deletion




# Difference between del and None:
#             -------->In the case del, the variable will be removed and we cannot access that variable(unbind 
#                      operation)
# 1) s = "durga" 
# 2) del s 
# 3) print(s)  NameError: name 's' is not defined. 

# But in the case of None assignment the variable won't be removed but the corresponding 
# object is eligible for Garbage Collection (re bind operation). Hence after assigning with 
# None value, we can access that variable.

# 1) s = "durga" 
# 2) s = None 
# 3) print(s)  Non