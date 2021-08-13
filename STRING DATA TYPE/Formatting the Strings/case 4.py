'''
Case-4: Number formatting with alignment

(1)  <, >, ^ and = are used for alignment
(2)  < -> Left Alignment to the remaining space
(3)  ^ -> Center alignment to the remaining space
(4)  > -> Right alignment to the remaining space
(5)  = -> Forces the signed(+) (-) to the left most position

Note: Default Alignment for numbers is Right Alignment.

'''
print("{:5d}".format(12)) 
print("{:<5d}".format(12)) 
print("{:<05d}".format(12)) 
print("{:>5d}".format(12)) 
print("{:>05d}".format(12)) 
print("{:^5d}".format(12)) 
print("{:=5d}".format(-12)) 
print("{:^10.3f}".format(12.23456)) 
print("{:=8.3f}".format(-12.23456))