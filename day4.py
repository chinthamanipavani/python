list1 = [11,12,13,14,15]
print(id(list1[0]))
print(id(list1[1]))
print(id(list1[2]))
print(id(list1[3]))
print(id(list1[4]))
print("break-1")
print(list( range(5,0,3)))   
#[] -->slicing
list2=[1,3,2,4]
print(range(50))
print(list(range(5,-1)))
print(list(range(5 , 3,-2)))
# for i in list1:
#     print(i)
#     for i in range (0 , 5):
#         print(i)                                 # o/p is line by line
#         for i in range(0, len(list2)):
#          print(i,list2[i])
#Dictionary
# keys can be strings also
# keys should be strings also.it is a mutable.
# it accept changes.
#key should be uniqe.
# same value can have different keys.
# by using keys u can access the value.
dict1={1:'a',2:'b',3:'c','pavani':'c'}
print(dict1[3])
dict1[2]='pushpa-3'
print(dict1)
dict2={1:'a',2:'b',3:'c','pavani':'c' ,2:"fidaa"}
print(dict2[3])
# dict2[2]='pushpa-2'
print(dict2)
dict2['2']= 'RRR-2'              
print(dict2)
sets = {1,2,3,"hai" "good"}
print(sets)
print(sets)
print(sets)
print(sets)
list3=[1,1,3,2,4,5,5,9]
print(set((list3)))                           #it can not print the duplicate values
#        none 
# there is no memory value.
# it is a datatype.
num4 =2
num4= None
print(num4)
print(type(num4))
print(id(num4))

#take user inputs.we can add integers and strings . by default it take as a string.

input("enter input")
print(input("enter input"))
num7=input("enter num7:")
num6=input("enter num6")
print(num6)
print(num6 + num7)
num7=int(input("enter num7:"))
num6=int(input("enter num6:"))
print(num7 + num6)