'''Дан список из 10 элементов.
Удалить все элементы, расположенные
перед минимальным элементом списка.
'''
a = [16, 21, 12, -1, 5, 65, 44, -8, 6, -3]
s = sorted(a)
print(s)
del s[:3]
print(s)
