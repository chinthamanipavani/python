#control statements
#controls the flow of the execution of a code.
#Control statements -  conditional statements , looping statements, jumpstatemente.

print('good morning')


n1=5
if n1>0:
 print('positive')
else:
 print('negative')


n2=18
if n2>18:
  print('eligible for vote')
else:
  print('not eligible for vote')


n3=9
if n3<=9:
  print('number is:',n3)
else:
  print('number is integer')


n4=0
if n4>0:
   if n4==1:
    print('one')
   else:
    print('positivenumber')
  
else:
  if n4==1:
    print('number is one')
  else:
    print('not one')  
  if n4==0:
    print('number is zero')
  else:
    print('not zoro number')   


#if condition is having the  more than one we can use the nestedif. 

n6=3
n5=1
if n5 ==2:
  print('2')
elif n5>2:
  print('number is greater than 2')
elif n5>1:
  print('n5 is greater than 1')  
elif n5<=1:
  print('number is greater than 1')
elif n5> n6:
  print('n5 is greater than the n6')

n7=3
if n7>0 and n7==2:
    print('not true ')
elif n7>0 and n7>1:
    print('2')


n1 = int (input("enter n1:"))

if n1 <=50:
  print(50*0)
else:
     if n1<=100:
      print(50*100)
     else:
       if n1<=201:
          print(100*200)
       else :
           if n1<=300:
               print(150*200)


