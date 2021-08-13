# 2)input():

# input() function can be used to read data directly in our required format.We are not 
# required to perform type casting.

# x = input("Enter Value)
# type(x)

# 10  int
# "durga" str
# 10.5  float
# True  bool

# ***Note: 
# -------> But in Python 3 we have only input() method and raw_input() method is not available. 
# ----->Python3 input() function behaviour exactly same as raw_input() method of Python2. 
# Example
#          every input value is treated as str type only.
# ---------> raw_input() function of Python 2 is renamed as input() function in Python 3.


# type(input("Enter value:")) 
# Enter value:10 
# <class 'str'> 
# Enter value:10.5
# <class 'str'> 


#Q) Write a program to read 2 numbers from the keyboard and print sum
# x=input("Enter First Number:") 
# y=input("Enter Second Number:") 
# i = int(x) 
# j = int(y) 
# print("The Sum:",i+j)

# Q)    Write a Program to read Employee Data from the Keyboard and 
#       print that Data

# eno=int(input("Enter Employee No:")) 
# ename=input("Enter Employee Name:") 
# esal=float(input("Enter Employee Salary:")) 
# eaddr=input("Enter Employee Address:") 
# married=bool(input("Employee Married ?[True|False]:")) 
# print("Please Confirm Information") 
# print("Employee No :",eno) 
# print("Employee Name :",ename) 
# print("Employee Salary :",esal) 
# print("Employee Address :",eaddr) 
# print("Employee Married ? :",married)





#    Write a Program to read Employee Data from the Keyboard and 
#    print that Data

# eno=int(input("Enter Employee No:")) 
# ename=input("Enter Employee Name:") 
# esal=float(input("Enter Employee Salary:")) 
# eaddr=input("Enter Employee Address:") 
# married=bool(input("Employee Married ?[True|False]:")) 
# print("Please Confirm Information") 
# print("Employee No :",eno) 
# print("Employee Name :",ename) 
# print("Employee Salary :",esal) 
# print("Employee Address :",eaddr) 
# print("Employee Married ? :",married)



# How to read multiple values from the keyboard in a 
# single line:


a,b= [int(x) for x in input("Enter 2 numbers :").split()] 
print("Product is :", a*b) 

#  Note: split() function can take space as seperator by default .But we can pass 
#        anything as seperator.



#   Q)   Write a program to read 3 float numbers from the keyboard 
 #       with, seperator and print their sum

a,b,c= [float(x) for x in input("Enter 3 float numbers :").split(',')] 
print("The Sum is :", a+b+c)
