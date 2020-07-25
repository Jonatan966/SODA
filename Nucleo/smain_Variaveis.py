import sys
import os

'''import pyglet'''

'''
Aqui estao guardados todas as variaveis e funcoes que poderao ser compartilhadas com o resto do sistema
Também contém funções essenciais para o funcionamento de todo os sistema
'''

soda_version = 'SODA 1.7'
soda_raiz = 'SODA.MAIN'
console_raiz = '>>'

soda_misc = ['LIMPAR', 'CLEAR']

class sMain_Avisos:
    def Resposta(self, resp = 0, tipo = ''):
        '''
        ----------------------------------------------------
        RESP - Aqui onde será inserido o texto a ser exibido
        TIPO - Aqui onde será inserido o tipo da saída de dados.
        ----------------------------------------------------
        O que posso inserir no TIPO:
        INT - Saída de dados de tipo Inteiro;
        FLOAT - Saída de dados de tipo Flutuante;
        STRING - Saída de dados de tipo String;
        LISTA - Criação de uma lista com os dados recebidos;
        Vazio - Sem saída de dados, útil para comunicados do sistema.
        ----------------------------------------------------
        Exemplo: variavel = Resposta('Digite um número: ', 'FLOAT')
        ----------------------------------------------------
        Sistema de tratamento de exceções
        Se casso ocorra um erro, o valor 0 é devolvido.
        ----------------------------------------------------
        '''
        try:
            tipo = tipo.upper().strip()
            nulo = 0
            if tipo != '' and resp != None:
                if tipo != 'LISTA':
                    saida = input(f'{console_raiz}>{resp}: ')
                    if tipo == 'FLOAT' or tipo == 0:
                        variavel = float(saida)
                        return variavel
                    elif tipo == 'STRING' or tipo == 1:
                        variavel = str(saida)
                        return variavel
                    elif tipo == 'INT' or tipo == 2:
                        variavel = int(saida)
                        return variavel
                elif tipo == 'LISTA':
                    print(f'{console_raiz}Comandos disponíveis:')
                    for c, v in enumerate(resp):
                        print(f'    {c} - {v}')
                    
            else:
                print(f'{console_raiz}{resp}')
        except ValueError:
            sMain_Avisos().Erro(0)
            return nulo
        except TypeError:
            sMain_Avisos().Erro(0)
            return nulo
        except:
            sMain_Avisos().Erro(3)
            return nulo

    def nFound(self, comando, sistema=soda_version):  # Mensagem de Comando Nao Encontrado
        '''
        ----------------------------------------------------
        Comando: O comando inexistente no sistema;
        Sistema: Nome do sistema ou módulo.
        ----------------------------------------------------
        Exemplo: naoEncontrado('CHURRO', 'MÓDULO MATEMATICA')
        >>"CHURRO" não foi encontrado no MÓDULO MATEMATICA
        ----------------------------------------------------
        '''
        if comando == 'LIMPAR' or comando == 'CLEAR' or comando == 'INFO':
            pass
        else:
            sMain_Avisos().Resposta(f'"{comando}" não foi encontrado no {sistema}')

    def Erro(self, erro):  # Mensagens de Erro
        '''
        ----------------------------------------------------
        Tipos de ERROS:
        0 - Erro ao digitar uma letra ao invés de um número;
        1 - Erro quando duas entradas contém o mesmo valor;
        2 - Erro ao preencher os dados incorretamente.
        ----------------------------------------------------
        '''
        if erro == 0:
            sMain_Avisos().Resposta(f'ERRO cód.{erro}: Digite apenas numeros <Valor 0 atribuido>')
        elif erro == 1:
            sMain_Avisos().Resposta(f'ERRO cód.{erro}: Os valores nao podem ser iguais')
        elif erro == 2:
            sMain_Avisos().Resposta(f'ERRO cód.{erro}: Preencha os dados corretamente')
        elif erro == 3:
            sMain_Avisos().Resposta(f'ERRO cód.{erro}: Erro desconhecido')

    def Welcome(self, modulo, tipo=0):  # Mensagem de Boas Vindas
        '''
        ----------------------------------------------------
        MODULO - Nome do módulo em questão.
        ----------------------------------------------------
        Exemplo: welcome('MATEMÁTICA')
        >>Bem vindo(a) ao módulo MATEMATICA
        >>Digite INFO para mais informações
        ----------------------------------------------------
        '''
        sMain_Avisos().Resposta(f'Bem vindo(a) ao módulo {modulo}\nDigite INFO para mais informações\n')
    '''

    def sons(n): #TODOS OS SONS DO SISTEMA

        ----------------------------------------------------
        Tipos de sons:
        0 - Som de inicialização;
        1 - Som de erro;
        2 - Som de click.
        ----------------------------------------------------
        
        s1 = pyglet.media.load('soda_ligar.wav', streaming=False)
        s2 = pyglet.media.load('soda_erro.wav', streaming=False)
        s3 = pyglet.media.load('soda_click.wav', streaming=False)
        
        if n == 0:
            s1.play()
        elif n == 1:
            s2.play()
        elif n == 2:
            s3.play()
        
        print(n)
    '''

class sMain_Saidas:
    def Ajuda(self, modulo = '',complemento = '', tipo=0):
        '''
        ----------------------------------------------------
        MODULO - Aqui será inserido o módulo desejado.
        COMPLEMENTO - Aqui será inserido o complemento desejado.
        TIPO - Aqui será inserido o tipo de saida de dados.
        ----------------------------------------------------
        MODULOS DISPONIVEIS:
        MATEMATICA; QUIMICA; CRIPTOGRAFIA; DEBUG.
        Se deixar vazio, estes dados sairão
        ----------------------------------------------------
        Exemplo: ajuda('MATEMATICA', 'AREAS')
        >> return ['QUADRADO', 'RETANGULO', 'TRIANGULO', 'LOSANGULO', 'TRAPEZIO', 'POLIGONO REGULAR (PR)', 'CIRCULO', 'CONE', 'ESFERA']
        ----------------------------------------------------
        '''
        if tipo == 0:
            if modulo == 'MATEMATICA':
                if complemento == '':
                    return ['AREAS', 'VOLUMES', 'LOGARITMOS', 'TRIGONOMETRIA']
                elif complemento == 'AREAS':
                    return ['QUADRADO', 'RETANGULO', 'TRIANGULO', 'LOSANGULO', 'TRAPEZIO', 'POLIGONO REGULAR (PR)', 'CIRCULO', 'CONE', 'ESFERA']
                elif complemento == 'VOLUMES':
                    return ['CUBO', 'PARALELEPIPEDO', 'PRISMA REGULAR (PR)', 'CILINDRO', 'CONE', 'ESFERA']
                elif complemento == 'LOGARITMOS':
                    return ['PRODUTO', 'QUOCIENTE', 'POTENCIA', 'RAIZ']
                elif complemento == 'TRIGONOMETRIA':
                    return ['PROGRESSAO ARITMETICA (P.A)', 'PROGRESSAO GEOMETRICA (P.G)', 'RAZAO', 'SOMA DOS TERMOS DE UMA P.A(S.N)', 'NUMEROS TRIANGULARES (N.T)', 'DELTA', 'HIPOTENUSA', 'CATETO']
            elif modulo == 'QUIMICA':
                if complemento == '':
                    return ['ANALISE']
                elif complemento == 'ANALISE':
                    return ['MOLARIDADE', 'TITULAÇÃO']
            elif modulo == 'CRIPTOGRAFIA':
                if complemento == '':
                    return ['CESAR', 'FENCE']
                elif complemento == 'CESAR':
                    return ['CIFRAR', 'DECIFRAR', 'PADRAO']
                elif complemento == 'FENCE':
                    return ['CIFRAR', 'DECIFRAR']
            elif modulo == 'DEBUG':
                if complemento == '':
                    return ['SYS.PATH', 'PLATAFORMA', 'SYS.COPYRIGHT', 'VARIAVEIS', 'MODULOS']
            elif modulo == '':
                return ['INFO - Exibe ajuda;', 'MATEMATICA - Modulo de operacoes matematicas;',
                        'CRIPTOGRAFIA - Oferece modulos de CRIPTOGRAFIA;',
                        'QUIMICA - Módulo de operações quimicas;',
                        'CONFIG - Configuracoes do sistema;',
                        'LIMPAR - Limpa o prompt de comandos;']
            else:
                return ['NaN']

    def Prompt(self, modulo='', componente='', raiz=soda_raiz):  # Cuida do Prompt de Comandos
        '''
        ----------------------------------------------------
        Responsavel pelo prompt do sistema
        MODULO - O módulo onde o usuário está.
        COMPONENTE - O componente do módulo  onde o usuário está.
        RAIZ - A pasta raiz do sistema.
        ----------------------------------------------------
        Exemplo: prompt('MATEMATICA', 'AREAS')
        >> <SODA/MATEMATICA/AREAS>>
        ----------------------------------------------------
        OBS: É possivel deixar os campos MODULO e COMPONENTE
        vazios.
        ----------------------------------------------------
        '''
        resp = f'<{raiz}({modulo}.{componente}){console_raiz} '
        q = input(resp).upper().strip()
        if q == 'LIMPAR' or q == 'CLEAR':
            os.system('cls')
        elif q == 'INFO':
            sMain_Avisos().Resposta(sMain_Saidas().Ajuda(modulo, componente), 'LISTA')
        return q

    '''
    def lista(lista, tipo=0):
            
            ----------------------------------------------------
            Responsável por criar uma lista de comandos.
            ----------------------------------------------------
            LISTA - Inserir aqui a lista de comandos, ou uma
            variável com eles;
            TIPO - Inserir o tipo de lista.
            ----------------------------------------------------
            Tipos de lista:
            0 - Lista enumerada.
            1 - Lista não enumerada.
            ----------------------------------------------------
            
            Resposta('Comandos disponíveis')
            if tipo == 0:
                for c, v in enumerate(lista):
                    print(f'    {c} - {v}', end='\n')

            elif tipo == 1:
                for c in lista:
                    print(f'    {c}', end='\n')
    '''

    def Documentacao(self, arquivo):
        manipulador = open(arquivo, 'r')
        print(manipulador.read())

    '''EXPERIMENTAIS----------------------------
    def misc(modulo):
        if modulo == 'INFO':
        
    Implementar comando INFO no def prompt

    -----------------------------------------'''
