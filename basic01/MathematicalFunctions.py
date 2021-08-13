# ***** A Module is collection of functions, variables and classes etc.

# ***** math is a module that contains several functions to perform mathematical operations.

# ***** If we want to use any module in Python, first we have to import that module.
#       import math

# Once we import a module then we can call any function of the module.
import math 
print(math.sqrt(16)) 
print(math.pi)

# ****** We can create alias name by using as keyword. import math as m

# ****** Once we create alias name, by using that we can access functions and variables of that 
#        module.


import math as m 
print(m.sqrt(16)) 
print(m.pi) 

# ***  We can import a particular member of a module explicitly as follows
# from math import sqrt
# from math import sqrt,pi
#  ***  If we import a member explicitly then it is not required to use module name while 
#       accessing.


from math import sqrt,pi 
print(sqrt(16)) 
print(pi) 

# Important Functions of math Module:

# 1) ceil(x)
# 2) floor(x)
# 3) pow(x,y)
# 4) factorial(x)
# 5) trunc(x)
# 6) gcd(x,y)
# 7) sin(x)
# 8) cos(x)
# 9) tan(x)
# 10) ....


# Important Variables of math Module:

# pi3.14
# e  2.71
# inf  infinity
# nan  not a number


# Q) Write a Python Program to find Area of Circle pi*r**2
from math import pi 
r = 16 
print("Area of Circle is :",pi*r**2)

