# Задание №1
# def say_hello():
#     print("Привет, мир!")

# say_hello()
# say_hello()



# # Задание №2
# def greet(name):
#     print(f"Привет, {name}!")

# greet("Анна")
# greet("Олег")

# # Задание №3
# def add(a, b):
#     return a+b
# c = add(3, 5)
# print(c)

# #Задание №4
# def greet(name="Гость"):
#     print(f"Привет, {name}!")
# greet("Оля")
# greet()

# # Задание №5
# def subtract(a, b):
#     return a - b
# print(subtract(10, 6))

# print(subtract(a = 5, b = 10))
# print(subtract(b =10, a = 5))

# # Задание №6
# def introduce (name, city = "Москва"):
#     return f"Меня зовут - {name}, я из города {city}"

# print(introduce("Анна", "Омск" ))
# print(introduce("Катя"))


# # Задание №7
# def multiply(*numbers):
#     res = 1
#     for i in numbers:
#         res = res*i
#     return res
# print(f"Произведение введенных чисел: {multiply(2, 4, 7)}")
# print(multiply())



# # Задание №8
# def display_info(**арг):
#     for key, value in арг.items():
#         print(f"{key}: {value}")
# display_info(name = "Дима", age = 18, city = "Балашиха")

# Задание №9
# def order(product, quantity = 1, *dop):
#     res = f"Товар - {product}, кол-во {quantity}"
#     if dop:
#         res  = res + ". Дополнения: "+", ".join(dop)
#     return res
# print(order("Пицца", 4,"кола"))


# # Задание №10
def profile(name, age = 18, **kwargs):
    res = [f"Имя — {name}", f"Возраст — {age}"]
    for key, value in kwargs.items():
        res.append(f"{key} — {value}")
    return res
   
info = profile("Антон", 19, статус="Студент")
print(info)


