# To Check Type of Characters Present in a String:
#  ---------------------------->Python contains the following methods for this purpose.
# 1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )

# 2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)

# 3) isdigit(): Returns True if all characters are digits only( 0 to 9)

# 4) islower(): Returns True if all characters are lower case alphabet symbols

# 5) isupper(): Returns True if all characters are upper case aplhabet symbols

# 6) istitle(): Returns True if string is in title case

# 7) isspace(): Returns True if string contains only spaces

# Eg:
# 1) print('Durga786'.isalnum())  True
# 2) print('durga786'.isalpha())  False
# 3) print('durga'.isalpha())  True
# 4) print('durga'.isdigit())  False
# 5) print('786786'.isdigit())  True
# 6) print('abc'.islower())  True
# 7) print('Abc'.islower())  False
# 8) print('abc123'.islower())  True
# 9) print('ABC'.isupper())  True
# 10) print('Learning python is Easy'.istitle())  False
# 11) print('Learning Python Is Easy'.istitle())  True
# 12) print(' '.isspace())  True


#Example


s=input("Enter any character:") 
if s.isalnum(): 
   print("Alpha Numeric Character") 
   if s.isalpha(): 
      print("Alphabet character") 
      if s.islower(): 
         print("Lower case alphabet character") 
      else: 
         print("Upper case alphabet character") 
   else: 
    print("it is a digit") 
elif s.isspace(): 
   print("It is space character") 
else: 
     print("Non Space Special Character")
