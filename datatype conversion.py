num=int(input("enter tha num value: "))
print(type(num))
print(bool(num))
print(str(num))
print(float(num))
print(complex(num))


string="hai"
print(string)
print(type(string))
# print(int(string))         #invalid literal for int() with base 10: 'hai'
# print(float(string))         #ValueError: could not convert string to float: 'hai'
print(bool(string))           

complex=5+8j
print(complex)
print(type(complex))
print(bool(complex))
# print(int(complex))              #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# print(float(complex))              #TypeError: float() argument must be a string or a real number, not 'complex'
print(str(complex))





a=[3,5,6,7]
print(a)
print(type(a))
print(type(list(a)))
print((set(a)))
print(type(set(a)))
print((tuple(a)))
print(type(tuple(a)))
print(bool(a))
# print(float(a))
print(str(a))