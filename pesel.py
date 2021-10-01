

pesel = str(input('Podaj pesel '))

def plec(pesel):
    if int(pesel[10])%2 !=0:
        print('K')
    else:
        print('M')


def sprawdz(pesel):

    if len(pesel)==11:
        plec(pesel)
    else:
        print('nieprawidlowy pesel')
        print('wprowadz ponownie')
        pesel = str(input('Podaj pesel '))
        sprawdz(pesel)
sprawdz(pesel)
