

def calcDiaSemana(dia):
    res = 0

    if dia=='domingo':
        res=0
    else:
        if dia == 'lunes':
            res=1

    return res 

if __name__ == '__main__':

    d = calcDiaSemana("domingo")

    print(d)
