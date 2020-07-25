math_version = 'MODULO CRIPTOGRAFIA v0.0.1'
import sys
sys.path.append('Nucleo/')
sys.path.append('Modulos/Criptografia/')
from Nucleo.smain_Handler import *


def soda_CRIPTOGRAFIA():
    sMain_Avisos().Welcome('CRIPTOGRAFIA')
    while True:
        q = sMain_Saidas().Prompt('CRIPTOGRAFIA')
        handler = sMain_Handlers().crtHandler(q)

        if handler != None:
            handler()

        elif q == 'SAIR' or q == 'QUIT' or q == 'VOLTAR':
            break

        elif q == '':
            pass

        else:
            sMain_Avisos().nFound(q , 'CRYPT 1.0')

