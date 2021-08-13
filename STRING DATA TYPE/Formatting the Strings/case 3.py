'''
Case-3: Number formatting for signed numbers
---> While displaying positive numbers,if we want to include + then we have to write
      {:+d} and {:+f}
----> Using plus for -ve numbers there is no use and for -ve numbers - sign will come 
automatically.
'''
print("int value with sign:{:+d}".format(123)) 
print("int value with sign:{:+d}".format(-123)) 
print("float value with sign:{:+f}".format(123.456)) 
print("float value with sign:{:+f}".format(-123.456)) 

'''
Output:
int value with sign:+123
int value with sign:-123
float value with sign:+123.456000
float value with sign:-123.456000
'''