from .smain_Variaveis import *
variaveis = vars()


def soda_DEBUG():
    sMain_Avisos().Resposta('Voce esta agora no menu DEBUG')
    while True:
        q = sMain_Saidas().Prompt('DEBUG')

        if q == 'SAIR' or q == 'VOLTAR' or q == 'QUIT':
            break

        elif q == 'SYS.PATH' or q == '0':
            print(f'Todos os modulos')
            sMain_Avisos().Resposta(sys.path, 'LISTA')

        elif q == 'PLATAFORMA' or q == '1':
            sMain_Avisos().Resposta(f'{soda_version} está rodando atualmente no: {sys.platform}')

        elif q == 'SYS.COPYRIGHT' or q == '2':
            sMain_Avisos().Resposta(sys.copyright)

        elif q == 'VARIAVEIS' or q == '3':
            print(f'Todas as variaveis disponiveis no {soda_version}')
            sMain_Avisos().Resposta(variaveis, 'LISTA')

        elif q == 'MODULOS' or q == '4':
            sMain_Avisos().Resposta(sys.modules, 'LISTA')
        
        elif q == 'TESTE':
            sMain_Avisos().Resposta(sys.displayhook(sMain_Avisos().Resposta('Digite algo', 'STRING')))



