a = {
    'ad':['Fuad','Rovsen','Orxan']
}
ad = input('Adi daxil edin: ')
if ad=='':
    print('Ad daxile etmediniz')
else:
    if ad not in a['ad']:
        print('bu ad bazada yoxdur')
        print('eger elave etmek isteyirsinizse "yes" yazin')
        cvb = input()
        if cvb=='yes':
            a['ad'].append(ad)
            print(a['ad'])
    else:
        print('adi silmek isteyirsinizse "yes" yazin')
        cvb = input()
        if cvb == 'yes':
            a['ad'].remove(ad)
            print(a['ad'])

