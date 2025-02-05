
bool1=True
print(bool(1)) #True

print(bool(0))#False
print(bool(2))
print(bool(-1))
print(bool(-9))
#truthy values --all  numbers except 0,True,Strings
#False values --0,False, ''
print(bool('  '))
print(bool("hai"))
print(bool(''))               #O/p--false
#string to int
print(int('25'))
# print(int('25a'))
# print(int('26.556'))                          error:-invalid literal for int() with base 10: '26.556'
print(float('26.556'))                          #O/P:-25.556 (it converted string to float values.)
int1=float(25.556)
print(int(int1))                             #O/P:-25(converted float to  integer)


# int1 = ( float(input('enter values:' )))
print(int1)
#string to list
str1="good morning"
print(len(str1))
print(len(list(str1)))
str1="hai"
list1 = [1,3,6,8,9,11]
str1=str(list1)
print(str1)
print(str1[0])
s1="gap"
s2="hai"
print(f'"{s1}"')  
print(f'"{s2}"')
print(f'my name,"{s2}"')

#control statements
