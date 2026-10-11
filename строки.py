'''a = 'Предложение, запятая, точка'
print(len(a), a[0], a[-1])'''


'''f = 'Плыли мы по морю, ветер мачту рвал'
s = len(f)
if s%2==0:
    print("Ответ: ",f[(s//2)-1], f[s//2])
else:
    print("Ответ: ",f[s//2])'''


'''g = 'Быстрый бурый лис перепрыгивает через ленивую собаку'
print(g[:3], g[-3:], g[1::2], g[::-1])'''

'''h = "Я изучаю язык составного программирования Python в 2026 году!"
c = 'с'
if c in h:
    print(h.count(c), h.index(c))
else:
    print('Буквы "с" нет')'''

'''s = "А роза упала на лапу Азора."
print(s.replace(" ","_"))'''


'''o = "    Около колодца окопался одинокий крокодил    "
print(len(o))
o = o.rstrip()
o = o.lstrip()
print(len(o))'''


'''name = 'Cупкин Павел'
name = name.split()
print(name)
name1 = name[1]
surname = name[0]
print(name1, surname, surname[0], name1[0])'''



'''sh = 'шалаш'
print(sh)
t = sh.lower()
if t == t[::-1]:
    print('Эта строка палиндромом')
else:
    print("Эта строка не палиндромом")'''


sp = "яблоко банан груша апельсин мандарин киви"
sp = sp.split()
print(sp)
print(len(sp), sp[0], sp[-1])

