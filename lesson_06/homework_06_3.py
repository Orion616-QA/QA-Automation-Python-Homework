lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = []
for s in lst1:
    if type(s) == str:
        lst2.append(s)
print(lst2)