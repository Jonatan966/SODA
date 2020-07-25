from Nucleo.smain_Variaveis import *

def soda_INF(valor = 0):
    print('Bem vindo(a) ao modulo INFO, digite o comando desejado para mais detalhes.')
    sMain_Avisos().Resposta(sMain_Saidas().Ajuda("INFO"), "LISTA")

    #INFO por gatilho
    if valor == 1:
        print('Ajuda sobre matematica:')

    while True:

        resp = sMain_Saidas().Prompt('INFO')

        if resp == 'SAIR' or resp == 'QUIT' or resp == 'VOLTAR':
            break

        elif resp == 'DOCUMENTACAO' or resp == 'CREDITOS':
            sMain_Saidas().Documentacao('documentacao.txt')



