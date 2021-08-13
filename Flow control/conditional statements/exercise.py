# Q) Write a Program to find Biggest of given 2 Numbers from the 
#  Commad Prompt?
n1=int(input("Enter First Number:")) 
n2=int(input("Enter Second Number:")) 
if n1>n2: 
 print("Biggest Number is:",n1) 
else : 
 print("Biggest Number is:",n2)



#  Q) Write a Program to find Biggest of given 3 Numbers from the 
#  Commad Prompt?
n1=int(input("Enter First Number:")) 
n2=int(input("Enter Second Number:")) 
n3=int(input("Enter Third Number:")) 
if n1>n2 and n1>n3: 
  print("Biggest Number is:",n1) 
elif n2>n3: 
  print("Biggest Number is:",n2) 
else : 
  print("Biggest Number is:",n3)


#   Q) Write a Program to Check whether the given Number is in 
#  between 1 and 100?
n=int(input("Enter Number:")) 
if n>=1 and n<=10 : 
 print("The number",n,"is in between 1 to 10") 
else: 
 print("The number",n,"is not in between 1 to 10")



#  Q) Write a Program to take a Single Digit Number from the Key 
#  Board and Print is Value in English Word?
# 1) 0  ZERO 
# 2) 1  ONE 
 
n=int(input("Enter a digit from o to 9:")) 
if n==0 : 
   print("ZERO") 
elif n==1: 
 print("ONE") 
elif n==2: 
 print("TWO") 
elif n==3: 
 print("THREE") 
elif n==4: 
 print("FOUR") 
elif n==5: 
 print("FIVE") 
elif n==6: 
 print("SIX") 
elif n==7: 
 print("SEVEN") 
elif n==8: 
 print("EIGHT") 
elif n==9: 
 print("NINE") 
else: 
 print("PLEASE ENTER A DIGIT FROM 0 TO 9")