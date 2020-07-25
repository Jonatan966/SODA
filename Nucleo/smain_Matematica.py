math_version = 'MODULO MATEMATICA v0.0.1'
import sys
sys.path.append('Nucleo/')
sys.path.append('Modulos/Matematica/')
from Nucleo.smain_Handler import *


def soda_MATEMATICA():
    sMain_Avisos().Welcome('MATEMATICA')
    while True:
        q = sMain_Saidas().Prompt('MATEMATICA')
        handler = sMain_Handlers().matHandler(q)

        if handler != None:
            handler()

        elif q == 'SAIR' or q == 'QUIT' or q == 'VOLTAR':
            break

        elif q == '':
            pass

        else:
            sMain_Avisos().nFound(q , math_version)

