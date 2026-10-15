#for

# Задание 1, 2, 3
'''
for i in range(1, 11):
    print(i)

    
for i in range(2, 51, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
'''

# Задание 4
'''
n = int(input('n:' ))
sum = 0
for i in range(1,n+1):
    sum=sum+i
print(sum)
'''

# Задание 5
'''
n = int(input())
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(fact)
'''

# Задание 6
'''
n = int(input('Введите число:'))
for i in range(1, 11):
    print(n, '*', i, '=', n * i)'''

# Задание 7
'''
s = [-24, -48, 67, 1, 4, 5 , 6, 7, 8, 0, 6, 3, 17, 95, 94]
t = 0
for i in s:
    if i>0:
        t+=1
print(t)
'''

# Задание 8
'''
st = "понедельник"
gl = 0
for i in st.lower():
    if i == 'е' or i == 'у' or i == 'а' or i == 'о' or i == 'э' or i == 'я' or i == 'и' or i == 'ю' or i == 'ё' or i == 'ы':
        gl+=1
print(gl)
'''

# Задание 9
'''
num = [1, 4, 6, 3, 6, 8, 9, 10, 47, 99, 39]
maxn = num[0]
for i in num:
    if i > maxn:
        maxn=i
print(maxn)
'''

# Задание 10
'''
for i in range(1, 10):
    for g in range(1, 10):
        print(i * g, end="\t")
    print()
'''



#while
# Задание 1
'''p = 1
while p<=10:
    print(p)
    p+=1
'''

# Задание 2
'''num2 = int(input('Введите число (0 для выхода): '))
s = 0
while num2 != 0:
    s += num2
    num2 = int(input('Введите число (0 для выхода): '))
print('Вы ввели ноль! Сумма всех чисел равна:')
print(s)'''

# Задание 3
'''num = int(input("Введите натуральное число: "))
count_of_numbers = 0
s = num
if num <= 0:
    print('Введите натуральное число:')
else:
    while s > 0:
        count_of_numbers+=1
        s=s//10 
print(count_of_numbers)
'''

# Задание 4
'''num = int(input("Введите натуральное число: "))
count_of_numbers = 0
s = num
if num <= 0:
    print('Введите натуральное число')
else:
    while s > 0:
        k=s%10 
        count_of_numbers+=k
        s = s//10
print(count_of_numbers)'''

# Задание 5
'''num = int(input())
s = num 
reversed_num = 0
while s > 0:
    k = s % 10
    reversed_num = reversed_num * 10 + k
    s = s // 10
print(reversed_num)'''


# Задание 6
'''n = int(input('Введите число: '))
i = 0
while 2**i<=n:
   print(2**i)
   i+=1'''


# Задание 7
'''password = 'qwerty'
passw = input('Введите пароль')
while passw!=password:
    print('Error')
    passw= input('Введите пароль: ')
print('Correct')'''


# Задание 8
'''a = int(input('1st num: '))
b = int(input('2nd num: '))
while b!=0:
    a, b = b, a%b
print(a)'''

# Задание 9
'''n = int(input('write a num: '))
a = 0
b = 1
while a<=n:
    print(a)
    next_num = a+b
    a = b
    b = next_num'''

# Задание 10
import random
n = random.randint(1, 100)
k = int(input('Введите число:'))
attempts = 1
while k!=n:
    attempts += 1
    if k<n:
        print('Больше')
    else:
        print('Меньше')
    k = int(input('Введите число:'))
print('Вы угадали это число', n)
print("Количество попыток:", attempts)








