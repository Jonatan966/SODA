from .smain_Variaveis import *

def soda_CONFIG():
    sMain_Avisos().Welcome('CONFIG')
    
    while True:

        resp = sMain_Saidas().Prompt('CONFIG')

        if resp == 'SAIR' or resp == 'QUIT' or resp == 'VOLTAR':
            break

