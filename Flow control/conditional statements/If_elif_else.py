# 3) if-elif-else:

#  if condition1:
#  Action-1
#  elif condition2:
#  Action-2
#  elif condition3:
#  Action-3
#  elif condition4:
#  Action-4
#  ...
#  else:
#  Default Action


# Based condition the corresponding action will be executed

from typing import runtime_checkable


brand=input("Enter Your Favourite Brand:") 
if brand=="RC" : 
   print("It is childrens brand") 
elif brand=="KF": 
   print("It is not that much kick") 
elif brand=="FO": 
   print("Buy one get Free One") 
else : 
   print("Other Brands are not recommended")


#    Note:
# 1) else part is always optional. Hence the following are various possible syntaxes.
# 1) If
# 2) if – else
# 3) if-elif-else
# 4) if-elif
# 2) There is no switch statement in Python



