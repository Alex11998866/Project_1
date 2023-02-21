lst = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(lst)
print(lst[:0:-1])
lst_1 = []
for i in lst:
    m = i * 2
    lst_1.append(m)

print(lst_1)
lst_2 = []
for i in lst_1:
    x = i + 2
    lst_2.append(x)

print(lst_2)