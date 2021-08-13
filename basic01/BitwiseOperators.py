# **** We can apply these operators bitwise.
# ----->  These operators are applicable only for int and boolean types.
# ---------->By mistake if we are trying to apply for any other type then we will get Error.

#  &, |, ^, ~, <<, >>


#  print(4&5)  Valid
#  print(10.5 & 5.6) 
#  TypeError: unsupported operand type(s) for &: 'float' and 'float'


#  print(True & True)  Valid


#  &  If both bits are 1 then only result is 1 otherwise result is 0
#  | If atleast one bit is 1 then result is 1 otherwise result is 0
#  ^  If bits are different then only result is 1 otherwise result is 0
#  ~  bitwise complement operator
#  1 --> 0 & 0 ---> 1
#  <<  Bitwise Left Shift
# >>  Bitwise Right Shift
a = (4&5)
print(a)


a = (4|5)
print(a)

a = (4^5)
print(a)


