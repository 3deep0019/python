# Replacing a String with another String
#          --------------------->>>>>>>>>>  s.replace(oldstring, newstring)
#                                           inside s, every occurrence of old String will be replaced with new String.

# Eg 1:

s = "Learning Python is very difficult"
s1 = s.replace("difficult","easy")
print(s1)

# Eg 2: All occurrences will be replaced

s = "ababababababab"
s1 = s.replace("a","b")
print(s1)

# Q) String Objects are Immutable then how we can change the 
#    Content by using replace() Method
# ANS -----> Once we creates string object, we cannot change the content.This non changeable 
#             behaviour is nothing but immutability. If we are trying to change the content by using 
#             any method, then with those changes a new object will be created and changes won't 
#             be happend in existing object.

# *** Hence with replace() method also a new object got created but existing object won't 
#     be changed.

# Eg:
s = "abab"
s1 = s.replace("a","b")
print(s,"is available at :",id(s))
print(s1,"is available at :",id(s1))


# In the above example, original object is available and we can see new object which was 
# created because of replace() method.