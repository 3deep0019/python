#     Syntax: x = firstValue if condition else secondValue

#    If condition is True then firstValue will be considered else secondValue will be considered.

# Eg 1:

# 1) a,b=10,20 
# 2) x=30 if a<b else 40 
# 3) print(x) #30 

# Eg 2: Read two numbers from the keyboard and print minimum value

# 1) a=int(input("Enter First Number:")) 
# 2) b=int(input("Enter Second Number:")) 
# 3) min=a if a<b else b 
# 4) print("Minimum Value:",min) 

# Output:
# Enter First Number:10
# Enter Second Number:30
# Minimum Value: 10
# Note: Nesting of Ternary Operator is Possible.

#Q) Program for Minimum of 3 Numbers
#  d=int(input("Enter First Number:")) 
#  b=int(input("Enter Second Number:")) 
#  c=int(input("Enter Third Number:")) 
#  min=d if d<b and d<c else b if b<c else c 
#  print("Minimum Value:",min) 

# # Q) Program for Maximum of 3 Numbers
# a=int(input("Enter First Number:")) 
# b=int(input("Enter Second Number:")) 
# c=int(input("Enter Third Number:")) 
# max=a if a>b and a>c else b if b>c else c 
# print("Maximum Value:",max) 


a=int(input("Enter First Number:")) 
b=int(input("Enter Second Number:")) 
print("Both numbers are equal" if a==b else "First Number is Less than Second Number" if a<b else "First Number Greater than Second Number") 
