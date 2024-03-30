def budce(xercler,gelir):
    return gelir-xercler

gelir = int(input('Ayliq gelirinizi daxil edin: '))
xercler = int(input('Ayliq xerclerinizi daxil edin: '))

print('Sizin bu ay ucun qalan xercliyiniz:',budce(xercler,gelir))