qui_version = 'MODULO QUIMICA v0.0.1'
import sys
sys.path.append('Nucleo/')
sys.path.append('Modulos/Quimica/')
from Nucleo.smain_Handler import *

def soda_QUIMICA():
    sMain_Saidas().Welcome("QUIMICA")
    while True:
        q = sMain_Saidas().Prompt("QUIMICA")
        handler = sMain_Handlers().quiHandler(q)

        if handler != None:
            handler()

        elif q == 'SAIR' or q == 'QUIT' or q == 'VOLTAR':
            break

        elif q == '':
            pass

        else:
            sMain_Avisos().nFound(q, qui_version)
