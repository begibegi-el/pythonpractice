# Задание 1
'''sp = [1, 4, 4, 5, 6, 6, 7, 4, 4 ,3 ]
mn = set(sp)
print(mn)'''


# Задание 2
'''mn = {1, 2, 3}
mn.add(5)
mn.discard(1)
print(mn)'''

# Задание 3
'''mn1 = {12, 4, 'banan', 'apple'}
mn2 = {45, 'cherry', 'kiwi'}
mn = mn1.union(mn2)
print(mn)'''


# Задание 4
'''mn1 = {12, 4, 'banan', 'apple', 'kiwi'}
mn2 = {45, 'cherry', 'kiwi'}
mn = mn1.intersection(mn2)
print(mn)'''

# Задание 5
'''culinary_vegetables = {"огурец", "помидор", "картофель", "морковь", "кабачок"}
botanical_fruits = {"яблоко", "банан", "апельсин", "помидор", "огурец"}
s = culinary_vegetables.difference(botanical_fruits)
k = botanical_fruits.difference(culinary_vegetables)
print(s)
print(k)'''

# Задание 6
'''fruit1 = {"банан", "апельсин", "абрикос", "яблоко", "вишня"}
fruit2 = {"вишня", "арбуз", "дыня", "абрикос"}
fruits4 = fruit1.symmetric_difference(fruit2)
print(fruits4)'''

# Задание 7
'''mn = {'b', 3,5 ,7, 8,'v','d','s', 't'}
x = float(input('Введите число: '))
print(x in mn)'''

# Задание 8
'''fruit1 = {"банан", "апельсин", "абрикос", "яблоко"}
fruit2 = {"вишня", "арбуз", "дыня", "абрикос", "банан", "апельсин", "яблоко"}
print(fruit2.issubset(fruit1))'''

# Задание 9 
'''st = "Около кола колокола."
st.split()
mn = set(st)
print(mn)'''

# Задание 10
'''first = [10, 8, 5, 7, 3, 8]
second = [5, 9, 7, 4, 7, 12]
all_of_them = first + second
mn = set(all_of_them)
print(mn)'''



#Кортежи
# Задание 1
'''k = (1, 2, 3, 4, 5)
print(k[0], k[-1], k[len(k)//2])'''

# Задание 2
'''k = (15, 17, 14, 16, 18, 15, 19, 20)
print(k[0:2])
print(k[-2:])
print(k[::-1])'''

# Задание 3
'''a = (8, 12, 5, 10, 15, 7, 10, 14)
print(len(a), sum(a), min(a), max(a))'''

# Задание 4
'''b = (8, 12, 5, 10, 15, 7, 10, 14, 10)
x = int(input('Введите число x: '))
if x in b:
    print('Это число есть в кортеже, ', 'количество этого числа: ', b.count(x),",", 'индекс первого вхождения: ',b.index(x))
else:
    print('Этого числа нет в кортеже')'''


# Задание 5 
'''tuple_1 = ("облако", "быстрый", "компас", "зеленый", "гитара")
tuple_2 = ("океан", "яркий", "телескоп", "мудрый", "рюкзак")
print(tuple_1 + tuple_2)'''


# Задание 6 
'''t = ('float')
print(type(t))'''


# Задание 7 
'''tup = ('Anna', 17, 'Madrid')
name, age, city = tup
print(city)
print(name)
print(age)'''


# Задание 8 
a = 10
b = 5
t = (a, b)
b, a = t
print(a, b)

# Задание 9 
'''t = ("облако", "быстрый", "компас", "зеленый", "гитара")
s = list(t)
s[1] = 'небо'
s = tuple(s)
print(s)'''


# Задание 10
'''t = (3, 7, 2, 7, 5, 3, 9, 2, 7, 1)
res = tuple(set(t))
print(res)'''


