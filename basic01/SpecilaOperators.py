# Python defines the following 2 special operators

# 1) Identity Operators
# 2) Membership operators


# 1)Identity Operators
# ---> We can use identity operators for address comparison.
# ---> There are 2 identity operators are available
#      1) is 
#      2) is not
# ********** r1 is r2 returns True if both r1 and r2 are pointing to the same object.
# ********** r1 is not r2 returns True if both r1 and r2 are not pointing to the same object.
# Eg:
a=10 
b=10 
print(a is b) 
x=True

a=10 
b=10 
print(a is  b) 
y=True



a="durga" 
b="durga" 
print(id(a)) 
print(id(b)) 
print(a is b) 
#Eg:
list1=["one","two","three"] 
list2=["one","two","three"] 
print(id(list1)) 
print(id(list2)) 
print(list1 is list2) 
print(list1 is not list2)  
print(list1 == list2)  
#Note: We can use is operator for address comparison where as == operator for content 
#      comparison.


#       2)Membership Operators:
#  ----->We can use Membership operators to check whether the given object present in the 
#        given collection. (It may be String, List, Set, Tuple OR Dict)

#   ******   In ---->  Returns True if the given object present in the specified Collection
#   ******   not in  ------> Retruns True if the given object not present in the specified Collection


# Ex 1 
x="hello learning Python is very easy!!!" 
print('h' in x) 
print('d' in x) 
print('d' not in x) 
print('Python' in x) 


#Eg: 2 
list1=["sunny","bunny","chinny","pinny"] 
print("sunny" in list1) 
print("tunny" in list1) 
print("tunny" not in list1) 