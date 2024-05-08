n,m = map(int,input().split())
k = 0
for i in range(n,m+1):
    if i%2==0:
        k+=1
        print('eded cutdur:',i)
    else:
        print('eded tekdir:',i)
print(k,'eded cutdur')
