#    eval():
#       --->  eval Function take a String and evaluate the Result.

x = eval('10+20+30')
print(x)



# eval() can evaluate the Input to list, tuple, set, etc based the provided Input.
# Eg: Write a Program to accept list from the keynboard on the display
l = eval(input('Enter List')) 
print (type(l)) 
print(l)