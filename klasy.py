pkt = int(input('podaj punkty: '))
f = int(input('podaj frekwencje: '))
so = float(input('podaj srednia: '))
if f>=100 or f<0 or so>6 or so<0:
    print('error')
else:
    if f >= 94:
        if so >=4:
            pkt+=20
            print('twoje punkty: ',pkt)
    else:
        print('punkty',pkt)
