'''
2)By using Slice Operator:

Syntax: list2 = list1[start:stop:step]

Start --> It indicates the Index where slice has to Start
          Default Value is 0

Stop --> It indicates the Index where slice has to End
         Default Value is max allowed Index of List ie Length of the List

Step --> increment value
         Default Value is 1
         
         '''
n=[1,2,3,4,5,6,7,8,9,10] 
print(n[2:7:2]) 
print(n[4::2]) 
print(n[3:7]) 
print(n[8:2:-2]) 
print(n[4:100])