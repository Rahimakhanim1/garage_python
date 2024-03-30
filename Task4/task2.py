lst = ['a','b','l','z','x','q','w','e','u','p']
l = len(lst)
while l>0:
    l-=1
    if lst[l]=='l' or lst[l]=='w' or lst[l]=='b':
        continue
    else:
        print(lst[l])
    