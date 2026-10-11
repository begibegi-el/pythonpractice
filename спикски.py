'''a = [6,3 , 2 , 24, 5, 6, 0, -4]
print(a[0] , a[-1])
a[0], a[-1] = a[-1], a[0]
print(a)'''


'''b = [6, 9, 9, 7, 5, 9, 25, 6, 24, 4]
c = len(b)
if c%2==0:
    print(b[(c//2) -1 ], b[(c//2)])
else: 
    print(b[(c//2)])'''

'''d = [83, 29, 92, 11, 22, 57, 77, 78, 29, 54]
print(d[:3])
print(d[-3:])
print(d[0::2])
print(d[::-1])'''


'''e = []
e.extend([24, 8, 12])
print(e)
e.insert(0, 6)
print(e)
e.pop(-1)
print(e)'''

'''f = [17, 89, 5, 63, 28, 71, 94, 12, 50]
print(len(f), sum(f), min(f), max(f), round(sum(f)/len(f), 2))'''

'''g = [35, 12, 78, 12, 44, 91, 35, 6, 78, 44, 50, 12]
x = int(input("Введите число:"))
if x in g:
    print(g.count(x), g.index(x))
else: 
    print('Это числа нет в списке')'''

'''h = [7, 22, 84, 7, 15, 93, 22, 61, 7, 48, 15, 84, 30, 22, 93]
m = sorted(h)
print(m[:3])
print(m[-3:])'''

'''n =[14, 52, 9, 14, 38, 77, 52, 63, 5, 91, 38]
l = [41, 8, 23, 8, 66, 41, 15, 99, 88, 23, 70, 15, 41]
nl = n+l
nl.sort(reverse=True)
print(nl[1])'''

'''text = 'яблоко горизонт рюкзак гитара синий чашка внезапно блокнот теплый тишина'
words = text.split()
words = sorted(words)
joined = ', '.join(words)
print(joined)'''

list1 = [42, 'яблоко', True, 15, 'гитара', False, 42, 'банан', 7]
k = int(input("Введите на сколько позиций сдвинуть?: "))
list1.rjust(k)
print(list1)