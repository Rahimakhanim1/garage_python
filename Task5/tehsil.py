def orta_bal(riyaziyyat,dil,xarici_dil):
    bal = (riyaziyyat+dil+xarici_dil)/3
    if bal>100*0.8:
        return'Baliniz yuksekdir'
    elif 0.8*100>bal>100*0.6:
        return'Baliniz ortadir'
    elif 100*0.6>bal:
        return 'baliniz asagidir'



riyaziyyat = int(input('Riyaziyyatdan topladiginiz balinizi daxil edin: '))
dil = int(input('Azerbaycan dilinden balinizi daxil edin: '))
xarici_dil = int(input('Xarici dilden balinizi daxil edin: '))

print(orta_bal(riyaziyyat,dil,xarici_dil))