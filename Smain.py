#Aqui onde o sistema inicia
from Nucleo import *
print(f'{soda_version}\nDigite INFO para mais informações.\n')


def getHandler(name):
    name = name
    return globals().get(f"soda_{name}")


def Main():
    while True:
        resp = sMain_Saidas().Prompt()
        handler = getHandler(resp)
        if handler != None :
            handler()
        elif resp == 'SAIR' or resp == 'QUIT':
            q = input('Deseja mesmo sair? <S/N> ').upper().strip()
            if q == 'Y' or q == 'YES' or q == 'SIM' or q == 'S':
                sys.exit()
            elif q == 'N' or q == 'NAO' or q == 'NO':
                continue
        elif resp == '':
            pass
        else:
            sMain_Avisos().nFound(resp)

Main()
