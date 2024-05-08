password = 'codecode'
count = 0
for i in range(3):
    n = input()
    if count == 2:
        print('block olundunuz')
        break
    if n!=password:
        print('1 sansiniz azaldi')
    else:
        print('Kod duzdur')
        break
    count+=1

