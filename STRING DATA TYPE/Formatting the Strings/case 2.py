'''
Case-2: Formatting Numbers
d -> Decimal IntEger
f -> Fixed point number(float).The default precision is 6
b -> Binary format
o -> Octal Format
x -> Hexa Decimal Format (Lower case)
X -> Hexa Decimal Format (Upper case)
'''

# Eg-1:
print("The intEger number is: {}".format(123)) 
print("The intEger number is: {:d}".format(123)) 
print("The intEger number is: {:5d}".format(123)) 
print("The intEger number is: {:05d}".format(123)) 

# Eg-2:
print("The float number is: {}".format(123.4567)) 
print("The float number is: {:f}".format(123.4567)) 
print("The float number is: {:8.3f}".format(123.4567)) 
print("The float number is: {:08.3f}".format(123.4567)) 
print("The float number is: {:08.3f}".format(123.45)) 
print("The float number is: {:08.3f}".format(786786123.45))

'''
Note:
--> {:08.3f}
-- Total positions should be minimum 8.
-->After decimal point exactly 3 digits are allowed.If it is less then 0s will be placed in the 
   last positions
--> If total number is < 8 positions then 0 will be placed in MSBs
--> If total number is >8 positions then all intEgral digits will be considered.
--> The extra digits we can take only 0
Note: For numbers default alignment is Right Alignment (>)
'''


#Eg- 3 Print Decimal value in binary, octal and hexadecimal form

print("Binary Form:{0:b}".format(153)) 
print("Octal Form:{0:o}".format(153)) 
print("Hexa decimal Form:{0:x}".format(154)) 
print("Hexa decimal Form:{0:X}".format(154)) 

'''
Output:
Binary Form:10011001
Octal Form:231
Hexa decimal Form:9a
Hexa decimal Form:9A

Note: We can represent only int values in binary, octal and hexadecimal and it is not 
possible for float values
'''

'''
Note:
1) {:5d} It takes an intEger argument and assigns a minimum width of 5.
2) {:8.3f} It takes a float argument and assigns a minimum width of 8 including "." and 
after decimal point excatly 3 digits are allowed with round operation if required
3) {:05d} The blank places can be filled with 0. In this place only 0 allowed.

'''