'''
Case-5: String formatting with format()

Similar to numbers, we can format String values also with format() method.
s.format(string)
'''

print("{:5d}".format(12)) 
print("{:5}".format("rat")) 
print("{:>5}".format("rat")) 
print("{:<5}".format("rat")) 
print("{:^5}".format("rat")) 
print("{:*^5}".format("rat"))
 # Instead of * we can use any character(like +,$,a etc)
 # Note: For numbers default alignment is right where as for strings default alignment is left