#logicaloperators
# logical-and or and not
# in python there is no symbols for logical operators.

print(True and True)
print(False and True)
print(False and(True and False))
print(False and False)
#it can not perform operations.

print(2 and 3)         #output depend on AND operator.0 ,"" are False value. All numbers without 0 is truthy.
print(-1 and -3)
print(3 and "")
print(0 and "")
print(3 and  " ")
print("" and 0)

print(2 and 6)
print("" and 2)            #depends upon False
print(None and 4)
print(4 and None)

print(2 and 4)



 #OR operator

print(True or False)
print(False or True)
print(False or (True and True))
print(True or ((True and True ) or (3 or 6)))
print(False and (False or False))
print(False and False)
print("" or 1)
print(not ("" and False))
print(not (True or False))



# Bitwise operators
#it  can return values to perform some operations
print(3& 4)

# 0100=4 & 0011 ==>add both bonary numbers.   0100         001       001
                                         #    0011         100       100
                                         #   + _______    &______   | ____
                                         #     0000        000        101 ==5

print(1 & 4)
print(bin(1))
print(bin(4))
print(1 | 4)



#Xor operator
print(12^4)         
print(1^2)        




#Left shift

# 1010(>>)
#10100
# 1010 => 0*1+1*2+0*4+1*8 =>10
#10100 => 0*1+0*2+1*4+0*8+1*16 =>20

print(4<<1)
print(4>>1)
print(4<<3)
print(4>>2)
print(4>>3)


#right shift

#0011 =3   (<<  ) 
#00001 =1


#tidley  (add one number)
print(~34)






                                         