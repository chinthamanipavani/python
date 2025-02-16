
#integer
a=int(input("enter a value:"))
print(type(a))
a=7
print(a+6)
print(a*2)
print(a-2)


#complex numbers
a=5+1j
b=9+10j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)


#float
f=int(input("enter f value: "))
print(type(f))
print(f+4)
print(f-3)
print(f*6)
print(f//2)

#Boolean Expressions
#it will have only True or False
a=25
print(a==35)
print(a==25)
print(a>3)
print(a<14)
print(a>=24)
print(45>43)
print(50<25)
print(19>=19)
print(56<=55)




#Sequences - Strings, List, Tuples, Range

#strings

fruits=["banana","orange","mango","apple"]
print(fruits)
print(fruits[0])
print(fruits[-1])
fruit=[]
print(fruit)
print(type(fruit))


#List- List is a ordered collection of data items and it can be changeable (Mutable)
list=[0,3,4,'String',True,[1,"Hello",3]]
print(id(list)) 
print(type(list))
print(len(list))
print(list)
print(list[2]) 
print(list[5])


tuple=(1,2,3,[1,2,3],"tuple")
print(tuple)
print(id(tuple))
print(type(tuple))
print(len(tuple))
print(tuple[3])
print(tuple[-1])




#print("----Range----")
list=[1,2,4,6,5,85]
print(len(list))
for i in range(0,len(list)):
    #print(i)
    print(i,list[i])

for i in range(0,100):
    print(i)
