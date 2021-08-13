# Splitting of Strings:
#         ----------------->We can split the given string according to specified seperator by using split() method
#         ----------------->l = s.split(seperator)
#         ---------------->The default seperator is space. The return type of split() method is List.


s="durga software solutions" 
l=s.split() 
for x in l: 
 print(x)

 # 2 

s="22-02-2018" 
l=s.split('-') 
for x in l: 
 print(x)