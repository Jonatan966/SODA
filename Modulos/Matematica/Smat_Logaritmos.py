import sys
from Nucleo import *
import math

def mat_LOGARITMOS():
    sMain_Avisos().Welcome('LOGARITMOS')
    try:
        while True:

            option = sMain_Saidas().Prompt('MATEMATICA', 'LOGARITMOS')
            if option == 'PRODUTO' or option == 0:
                a1 = sMain_Avisos().Resposta('Digite o valor da base', 'FLOAT')
                a2 = sMain_Avisos().Resposta('Digite o primeiro valor do logaritmando', 'FLOAT')
                a3 = sMain_Avisos().Resposta('Digite o segundo valor do logaritmando', 'FLOAT')
                sMain_Avisos().Resposta('AINDA ES FASE DE TESTES')


            elif option == 'SAIR' or option == 'VOLTAR' or option == 'QUIT':
                break

            elif option == '':
                pass

            else:
                sMain_Avisos().nFound(option)

    except ValueError:
        sMain_Avisos().Erro(0)
