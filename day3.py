num1 = 123
print(num1==123)
print(num1 ==342)
# print(num1 = 123)             'num1' is an invalid keyword argument for print()
print(32.5>32)
print(7>7)
print(7>=7)

#if

num=123
num2=123
if num == num2:
    print("correct number")

    first=[2,7,4,"string",True ,[1,"abc","hell",2,2]]   
    print(first)  
    print(first[1])  
    print(type[first])    
    print(len(first)) 
    # print(list[6])                       //IndexError: list index out of range
    print(first[1 : 3 :2])
    print(first[1:7])
    print(first[-1][1])
    print(first[-2])
    first[5][1]="False"
    print(first)
    first[4]="False"
    print(first)
    print(first[-2])
    print(len(first[-2]))
    print(len(first[-1]))
    #one way
    print((first[5][2]))
    print(len(first[5][2]))
    #another way
    sublist=first[5]
    print(sublist)
    print(sublist[1])

    #Range

    # 1. limit 

    print(range(0,19))                                #o/p:-range(0, 19)
    print(list(range(0,19)))  
    
    # print(list(range[0,19]))                        # type 'range' is not subscriptable                                             
    print(list(range(0,100,2)))
    print(list(range(0,100)))
    print(list(range(1,100,2)))
