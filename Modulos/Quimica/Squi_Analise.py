import sys
from Nucleo.smain_Variaveis import *

def qui_ANALISE():
    sMain_Avisos().Welcome("ANALISE")
    try:
        while True:
            option = sMain_Saidas().Prompt("QUIMICA", "ANALISE")
            if option == "MOLARIDADE":

                M = float(input(f'{console_raiz}Digite a massa (em gramas): '))
                Sm = float(input(f'{console_raiz}Digite a soma atômica: '))
                V = sMain_Avisos().Resposta('Digite o Volume (em ml)', 'FLOAT')/1000
                sMain_Avisos().Resposta(f'M = ({M} / {Sm}) * {V}')
                sMain_Avisos().Resposta(f'M = {M / Sm} * {V}')
                sMain_Avisos().Resposta(f'M = {(M / Sm)*V}')
                
            
            elif option == 'VOLTAR' or option == 'SAIR' or option == 'QUIT':
                break

    except ValueError:
        sMain_Avisos().Erro(0)
        qui_ANALISE()
