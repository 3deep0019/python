'''
Formatting the Strings:
֍ We can format the strings with variable values by using replacement operator {} and 
format() method.
֍ The main objective of format() method to format string into meaningful output form.
'''
#Case- 1: Basic formatting for default, positional and keyword arguments

name = 'durga' 
salary = 10000 
age = 48 
print("{} 's salary is {} and his age is {}".format(name,salary,age)) 
print("{0} 's salary is {1} and his age is {2}".format(name,salary,age)) 
print("{x} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name))