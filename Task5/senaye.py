def bmi(ceki,boy):
    hesablanmisBmi = ceki/(boy*boy)
    if hesablanmisBmi<18.5:
        return 'sizin kilonuz normalin altindadir',hesablanmisBmi
    elif 18.5<= hesablanmisBmi <= 24.9:
        return 'sizin kilonuz idealdir'
    elif 25<= hesablanmisBmi<=29.9:
        return 'sizin kilonuz ideal kilonun ustundedir',hesablanmisBmi
    elif 30<hesablanmisBmi<=39.9:
        return 'sizin kilonuz idealin cox ustunde',hesablanmisBmi
    else:
        return 'sizin kilonuz idealin cox ustunde',hesablanmisBmi

ceki = int(input("Cekinizi kg'la qeyd edin: "))
boy = int(input('Boyunuzu metrle qeyd edin: '))
print(bmi(ceki,boy))