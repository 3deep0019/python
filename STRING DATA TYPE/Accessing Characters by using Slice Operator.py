# 2)Accessing Characters by using Slice Operator:

#  Syntax: s[bEginindex:endindex:step]

#  Begin Index: From where we have to consider slice (substring)
#  End Index: We have to terminate the slice (substring) at endindex-1 
#  Step: Incremented Value.

# Note:
#  If we are not specifying bEgin index then it will consider from bEginning of the string.
#  If we are not specifying end index then it will consider up to end of the string.
#  The default value for step is 1.

# 1) >>> s="Learning Python is very very easy!!!" 
# 2) >>> s[1:7:1] 
# 3) 'earnin' 
# 4) >>> s[1:7] 
# 5) 'earnin' 
# 6) >>> s[1:7:2] 
# 7) 'eri' 
# 8) >>> s[:7] 
# 9) 'Learnin' 
# 10) >>> s[7:] 
# 11) 'g Python is very very easy!!!' 
# 12) >>> s[::] 
# 13) 'Learning Python is very very easy!!!' 
# 14) >>> s[:] 
# 15) 'Learning Python is very very easy!!!' 
# 16) >>> s[::-1] 
# 17) '!!!ysae yrev yrev si nohtyP gninraeL'



# Behaviour of Slice Operator:
# 1) s[bEgin:end:step]

# 2) Step value can be either +ve or –ve

# 3) If +ve then it should be forward direction(left to right) and we have to consider bEgin 
#    to end-1

# 4) If -ve then it should be backward direction (right to left) and we have to consider bEgin 
#    to end+1.

# ***Note:
#  In the backward direction if end value is -1 then result is always empty.
#  In the forward direction if end value is 0 then result is always empty.


# In Forward Direction:

# default value for bEgin: 0
# default value for end: length of string
# default value for step: +1

# In Backward Direction:
# default value for bEgin: -1
# default value for end: -(length of string+1)

# Note: Either forward or backward direction, we can take both +ve and -ve values for 
#       bEgin and end index.

# Slice Operator Case Study:
# 1) S = 'abcdefghij'
# 2) s[1:6:2]  'bdf'
# 3) s[::1]  'abcdefghij'
# 4) s[::-1]  'jihgfedcba'
# 5) s[3:7:-1]  ''
# 6) s[7:4:-1]  'hgf'
# 7) s[0:10000:1]  'abcdefghij'
# 8) s[-4:1:-1]  'gfedc'
# 9) s[-4:1:-2]  'gec'
# 10)s[5:0:1]  ''
# 11)s[9:0:0]  ValueError: slice step cannot be zero
# 12)s[0:-10:-1]  ''
# 13)s[0:-11:-1]  'a'
# 14)s[0:0:1]  ''
# 15)s[0:-9:-2]  ''
# 16)s[-5:-9:-2]  'fd'
# 17)s[10:-1:-1]  ''
# 18)s[10000:2:-1]  'jihgfed'
# Note: Slice operator never raises IndexError
 
# Mathematical Operators for String:

# We can apply the following mathematical operators for Strings.
#       1) + operator for concatenation
#       2) * operator for repetition 
print("durga"+"soft") 
print("durga"*2) 


# Note: 
# 1) To use + operator for Strings, compulsory both arguments should be str type.
# 2) To use * operator for Strings, compulsory one argument should be str and other
#    argument should be int.