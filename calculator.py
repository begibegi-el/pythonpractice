op = int(input("Каким оператором хотите воспользоваться? \n"
"1 - арифметические операторы \n"
"2 - операторы сравнения \n"
"3 - логические операторы \n"
"4 - операторы принадлежности \n"
"5 - операторы тождественности \n"
"Ваш выбор: "))

if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:
    match(op):
        case 1: 
            num1 = float(input("Введите первое число: "))
            sign = input("Знак: ")
            num2 = float(input("Введите второе число: "))
            if sign == '+':
                print(num1 + num2)
            elif sign == '-':
                print(num1 - num2)
            elif sign == '*':
                print(num1 * num2)
            elif sign == '/':
                if num2 != 0:
                    print(num1 / num2)
                else:
                    print('Ошибка: на ноль делить нельзя!')
            elif sign == '//':
                if num2 != 0:
                    print(num1 // num2)
                else:
                    print('Ошибка: на ноль делить нельзя!')
            elif sign == '%':
                if num2 != 0:
                    print(num1 % num2)
                else:
                    print('Ошибка: на ноль делить нельзя!')
            elif sign == '**':
                print(num1 ** num2)
            else:
                print("Неправильный ввод формата данных!")
        case 2: 
            num1 = float(input("Введите первое число: "))
            sign = input("Знак: ")
            num2 = float(input("Введите второе число: "))
            if sign == '<':
                print(num1<num2)
            elif sign == '>':
                print(num1>num2)
            elif sign == '==':
                print(num1==num2)             
            elif sign == '>=':
                print(num1>=num2) 
            elif sign == '<=':
                print(num1<=num2)
            elif sign == '!=':
                print(num1!=num2)
            else:
                print("Неправильный ввод!")
        case 3: 
            a = input("Введите False или True: ")
            if a == "False":
                a = False
                oper = input("Введите and, or, not: ")
                if oper == "not":
                    print(not a)
                elif oper == "and" or oper == "or":
                    b = input("Введите False или True: ")
                    if b == "False":
                        b = False
                        if oper == "or":
                            print(a or b)
                        elif oper == "and":
                            print(a and b)
                        else:
                            print("Неправильный ввод!")
                    elif b == "True":
                        b = True
                        if oper == "or":
                            print(a or b)
                        elif oper == "and":
                            print(a and b)
                        else:
                            print("Неправильный ввод!")
                    else:
                        print("Неправильный ввод!")
                else:
                    print("Неправильный ввод!")
            elif a == "True": 
                a = True
                oper = input("Введите and, or, not: ")
                if oper == "not":                                    
                    print(not a)            
                elif oper == "and" or oper == "or":            
                    b = input("Введите False или True: ")            
                    if b == "False":        
                        b = False        
                        if oper == "or":
                            print(a or b)
                        elif oper == "and":
                            print(a and b)
                        else:
                           print("Неправильный ввод!") 
                    elif b == "True":
                        b = True
                        if oper == "or":
                            print(a or b)
                        elif oper == "and":
                            print(a and b)
                        else:
                            print("Неправильный ввод!")
                    else:
                        print("Неправильный ввод!")
                else:
                    print("Неправильный ввод!")
            else:
                print("Неправильный ввод!")
        case 4: 
            sp = input("Введите что-нибудь: ")
            sign = input("Выберите операцию: in или not in: ")
            if sign == "in": 
                result = input("Принадлежность какого символа хотите проверить?: ")
                print(result in sp)
            elif sign == "not in":
                result = input("Не принадлежность какого символа хотите проверить?: ")
                print(result not in sp)
            else: 
                print("Неправильный ввод!")
        case 5:
            x = [1, 2, 3]
            y = x 
            z = [1, 2, 3]
            print("Есть данные:\n"
            "x = [1, 2, 3]\n" 
            "y = x \n" 
            "z = [1, 2, 3]\n")
            per1 = input("Введите одну из переменных (x, z, y): ")
            if per1 == "x" or per1 == "z" or per1 == "y": 
                sign = input("Введите is или is not: ")
                if sign == "is" or sign == "is not":
                        per2 = input("Введите другую переменную (x, z, y): ")
                        if (per1 == "x" and per2 == "y") or (per1 == "y" and per2 == "x"):
                            if sign == "is":
                                print(x is y)
                            else:
                                print(x is not y)
                        elif (per1 == "x" and per2 == "z") or (per1 == "z" and per2 == "x"):
                            if sign == "is":
                                print(x is z)
                            else:
                                print(x is not z)
                        elif (per1 == "y" and per2 == "z") or (per1 == "z" and per2 == "y"):
                            if sign == "is":
                                print(y is z)
                            else:
                                print(y is not z)
                        elif per1 == per2:
                            if sign == "is":
                                print(True)
                            else:
                                print(False)
                        else:
                            print("Неправильный ввод!")
                else: 
                    print("Неправильный ввод!")    
            else: 
                print("Непрвильный ввод!")                 
else: 
    print("Неправильный ввод!")