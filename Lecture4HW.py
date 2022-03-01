#Задача 1

a = 3
b = 2

if (a > b):
    print('a = 2')
    print('b = 3')
else:
    print('a = 3')
    print('b = 2')

#Задача 2

x = 3

if (x>0):
    print('+')
elif(x<0):
    print('-')
else:
    print(0)

#Задача 3

#Задача 4

a = 3

if ( a == 0 ):
    print('нула')
elif ( a == 1 ):
    print('едно')
elif ( a == 2 ):
    print('две')
elif ( a == 3 ):
    print('три')
elif ( a == 4):
    print('четири')
elif ( a == 5):
    print('пет')
elif ( a == 6):
    print('шест')
elif ( a == 7):
    print('седем')
elif ( a == 8):
    print('осем')
elif (a == 9):
    print('девет')

#Задача 5

#Задача 6

#Задача 7 

x = 3

if (x>=1 and x<=3):
    print(x*10)
elif(x>=4 and x<=6):
    print(x*100)
elif(x>=7 and x<=9):
    print(x*1000)
else:
    print('error')

#Задача 8

#Задача 9 

#Задача 10

dog_age = 2

if (dog_age>0 and dog_age<=2):
    print(dog_age*10.5)
else:
    print(21+dog_age*4)

#Задача 11

a = 3
b = 4
c = 5

print((a+b+c)/2)

#Задача 12 

user_age = 30
user_gender = 'm'
user_f_status = 'Y'

if (user_gender == 'f'):
    print ('градски райони')
elif (user_gender == 'm' and user_age>=20 and user_age<=40):
    print('навсякъде')
elif (user_gender== 'm' and user_age>40 and user_age<=60):
    print('градски райони')
else:
    print('грешка')

#Задача 13 (потърсих в интернет тъй като из лекциите не успях да намеря начин за решаване)

num = '1234'[::-1]

print(num)

#Задача 17

num1 = 5
num2 = 10
res1 = num1 +  num2
res2 = num1/num2
res3 = num1%num2 
if (res1%2==0):
    print(res1, '-', 'even')
else:
    print(res1, '-', 'odd')

print(res2)

print(res3)