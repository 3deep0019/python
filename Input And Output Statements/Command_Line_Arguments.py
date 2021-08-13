# ------> argv is not Array it is a List. It is available sys Module.
# -----> The Argument which are passing at the time of execution are called Command Line 
#         Arguments.

# Note: ---------->argv[0] represents Name of Program. But not first Command Line Argument.
#                 argv[1] represent First Command Line Argument.

#Program: To check type of argv from sys

# import argv
# print(type(argv))

# q Write a Program to display Command Line Arguments

#   ------ Ans

# from sys import argv 
# print('The Number of Command Line Arguments:', len(argv)) 
# print('The List of Command Line Arguments:', argv) 
# print('Command Line Arguments one by one:') 
# for x in argv: 
#     print(x)


# from sys import argv 
# sum=0 
# args=argv[1:] 
# for x in args : 
#   n=int(x) 
#   sum=sum+n 
# print("The Sum:",sum)   


from sys import argv
print(argv[1]+argv[1])
print(int(argv[1]+int(argv[2])))