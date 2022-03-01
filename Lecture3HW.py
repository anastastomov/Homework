#Задача 1

school = 'Tsanko Lavrenov'

print ( school.replace ( 'o', 'w'))
print (school)

#Задача 2 

country = 'usa'
correct_country = country.upper()

print (correct_country)

#Задача 3 
filename = 'hello.py'

res1 = filename.endswith ('.py')
print(res1)

res2 = filename.startswith ('world')
print (res2)

#Задача 4
ASD = 'ONE'

print (ASD)

#Задача 5

user_name = ' $$John Smith '

print (user_name.strip())
print (user_name.lstrip())
print (user_name.rstrip())
print (user_name.split())

#Задача 6
a = '             Coding Temple, inc.'
b = '             283 Franklin St.'
c = '             Boston, MA'
d = '       Product Name   Product Price'
e = '       Books          $49.95'
f = '       Computer       $579.99'
g = '       Monitor        $124.89'
h = '                      Total'
i = '                      $754.83'
j = '       Thanks for shopping with us today!'

print('*'*50)
print(a)
print(b)
print(c)
print('='*50)
print(d)
print(f)
print(g)
print('='*50)
print(h)
print(i)
print('='*50)
print(j)
print('*'*50)