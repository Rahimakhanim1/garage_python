lst = [1,2,3,4,5,6,7,8,1,2,3,6,5,4,3,7,3,2,1]
lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)

print(lst2)