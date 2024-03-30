dictt = {
    'sual1':{
        'sual':'Azerbaycanin paytaxti haradir?',
        'cavab':'bakı'
    },
    'sual2':{
        'sual':'Nece okean var?',
        'cavab':'4'
    },
    'sual3':{
        'sual':'Nyutonun nece qanunu var?',
        'cavab':'3'
    },
    'sual4':{
        'sual':'6-nin faktorialı neçədir?',
        'cavab':'120'
    },
    'sual5':{
        'sual':'Turkiyenin paytaxti haradir?',
        'cavab':'istanbul'
    },
    'sual6':{
        'sual':'Rusiyanin paytaxti haradir?',
        'cavab':'moskva'
    },
     'sual7':{
        'sual':'Fransanin paytaxti haradir?',
        'cavab':'paris'
    },
    'sual8':{
        'sual':'Ingilternin paytaxti haradir?',
        'cavab':'london'
    },
    'sual9':{
        'sual':'Yunanistanin paytaxti haradir?',
        'cavab':'afina'
    },
    
}
sehv = 0

for key in dictt.values():
    print('sual-',key['sual'])
    ans = input('Cavabi qeyd edin: ')
    if ans.lower() != key['cavab']:
        sehv += 1

cixilanbal = sehv//4
print('bal: ',len(dictt)-cixilanbal-sehv)

