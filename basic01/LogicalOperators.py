#  ----  We can apply for all types.

# *** -->  For boolean Types Behaviour:
#             and --->  If both arguments are True then only result is True
#             or --->   If atleast one arugemnt is True then result is True
#             not --->  Complement

# -- Example
#     (1) True and False ---->False
#     (2) True or False -----> True
#     (3) not False ---> True


# **** For non-boolean Types Behaviour:
#       
#      --------> 0 means False
#      --------> non-zero means True
#      --------> empty string is always treated as False


#   (1)   x and y:
#      ------->If x is evaluates to false return x otherwise return y
#  Eg:
#     (1) 10 and 20
#     (2) 0 and 20
#                   If first argument is zero then result is zero otherwise result is y

#      (2)  x or y:
#       --------> If x evaluates to True then result is x otherwise result is y
#   Eg:
#     (1) 10 or 20  10
#     (@)  0 or 20  20
 

#     (3)  not x:
#        ---------->If x is evalutates to False then result is True otherwise False
#     Eg:
#        (1)  not 10  False
#        (2)  not 0  True

# 1) "durga" and "durgasoft" ==>durgasoft 
# 2) "" and "durga" ==>"" 
# 3) "durga" and "" ==>"" 
# 4) "" or "durga" ==>"durga" 
# 5) "durga" or ""==>"durga" 
# 6) not ""==>True 
# 7) not "durga" ==>False