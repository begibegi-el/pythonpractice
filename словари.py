# Задание 1
'''names = {
    'Anna': 5,
    'Maria': 3, 
    'Alex': 4
}
name = input('Write a name: ')
print({names[name]})'''


# Задание 2
'''dict2 = {'name': 'Bob', 'age': 17, 'city': 'Barcelona', 'country':'Spain'}
dict2['native_language'] = 'russian'
dict2.update({'city': 'Madrid'})
del dict2['age']
print(dict2)'''


# Задание 3
'''dict3 = {'subject':'math', 'num_of_stud': 24, 'minutes': 90}
key = input('Введите название ключа: ')
if key in dict3:
    print(dict3[key])
else:
    print('Нет такого ключа')'''


# Задание 4 
'''dict4 = {
    'cat': 'кот',
    'dog': 'собака',
    'bird': 'птица',
    'fish': 'рыба'
}
print(dict4.keys())
print(dict4.values())
print(len(dict4))'''

# Задание 5 
'''dict4 = {
    'яблоки': 120,
    'молоко': 85,
    'хлеб': 45,
    'сыр': 350,
    'кофе': 420
} 
for i, p in dict4.items():
    print(i, p)'''


# Задание 6
'''dict5 = {
    'Смартфон': 45000,
    'Ноутбук': 85000,
    'Наушники': 12000,
    'Умные часы': 18000,
    'Планшет': 32000
}
sum = 0
max_price = 0
for i, p in dict5.items():
    sum += p
    if p > max_price:
        max_price = p
        mostex = i
print('Сумма всех цен: ', sum)
print('Самый дорогой товар: ', mostex)'''

# Задание 7
'''text = 'В резерве перезеленеют все весенние деревья.'
st = set(text)
empthy_dict = {}
for char in st:
    print(char, text.count(char))
    empthy_dict[char] = text.count(char)
print(empthy_dict)'''


# Задание 8 
'''text = "код питон циклы код словари пиthon код списки циклы функции код"
text2 = text.split()
mn = set(text2)
empthy_dict8 = {}
maxvs = 0
for word in mn:
    empthy_dict8[word] = text2.count(word)
    c = text2.count(word)
    if c>maxvs:
        maxvs = c
for word, count in empthy_dict8.items():
    if count == maxvs:
        print('Самое частое слово: ', word)'''


# Задание 9
'''population = {
    "Китай": 1411,
    "Индия": 1428,
    "США": 340,
    "Индонезия": 277,
    "Пакистан": 240,
    "Бразилия": 216
}
pomen = {}
for key, value in population.items():
    pomen[value]=key
print(pomen)'''


# Задание 10
countries = ["Россия", "Франция", "Япония", "Египет", "Бразилия"]
cities = ["Москва", "Париж", "Токио", "Каир", "Бразилиа"]
dict10 = {}
for i in range(len(countries)):
    dict10[countries[i]] = cities[i]
cities = input('Введите страну: ')
print(dict10[cities])





