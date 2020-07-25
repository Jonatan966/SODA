import sys
sys.path.append('Nucleo/')
from Nucleo.smain_Variaveis import *

class sMain_Fence:
    def __railfence_id(self, tam, key):
        ''' (Railfence, int, int) -> list of int
        Retorna um lista de inteiros com a posicao da
        linha que o caracter do texto ira ocupar,
        variando de 0 ate key - 1.
        '''
        j = 0
        inc = 0
        idx = []
        for i in range(tam):
            if j == key - 1:
                inc = -1
            elif j == 0:
                inc = 1
            idx.append(j)
            j += inc
        return idx
 
    def encrypt(self, texto, key):
        ''' (Railfence, str, int) -> str
        Retorna o texto plano cifrado na cifra rail
        fence com a chave key.
        '''
        texto = texto.replace(' ', '')
        tam = len(texto)
        idx = self.__railfence_id(tam, key)
        
        cifrado = ''
        for i in range(key):
            for z in range(tam):
                if idx[z] == i:
                    cifrado += texto[z]
        return cifrado.upper()
 
    def decrypt(self, texto, key):
        ''' (Railfence, str, int) -> str
        Retorna o texto plano para um texto cifrado
        com a cifra rail fence com a chave key.
        '''
        texto = texto.replace(' ', '')
        tam = len(texto)
        idx = self.__railfence_id(tam, key)
        idx_sorted = sorted(idx)
 
        texto_plano = ''
        for i in range(tam):
            for j in range(tam):
                if idx[i] == idx_sorted[j] and idx[i] > -1:
                    texto_plano += texto[j]
                    idx[i] = -1
                    idx_sorted[j] = -1
        return texto_plano.lower()

def crt_FENCE():
    sMain_Avisos().Welcome('FENCE')
    while True:
        option = sMain_Saidas().Prompt('CRIPTOGRAFIA', 'FENCE')
        if option == 'CIFRAR' or option == '0':
            txt = sMain_Avisos().Resposta('Digite o texto a ser cifrado', 'STRING')
            senha = sMain_Avisos().Resposta(f'Digite a senha (SOMENTE NÚMEROS) (Tamanho da senha: {len(txt)})', 'INT')
            if senha >= len(txt) or senha <= 1:
                sMain_Avisos().Resposta("ERRO: A senha não pode ser, maior ou igual ao tamanho do texto, igual ou menor que 1")
            else:
                sMain_Avisos().Resposta(sMain_Fence().encrypt(txt, senha))

        elif option == 'DECIFRAR' or option == '1':
            txt = sMain_Avisos().Resposta('Digite o texto a ser decifrado', 'STRING')
            senha = sMain_Avisos().Resposta('Difite a senha (SOMENTE NÚMEROS)', 'INT')
            if senha >= len(txt) or senha <= 1:
                sMain_Avisos().Resposta("ERRO: A senha não pode ser, maior ou igual ao tamanho do texto, igual ou menor que 1")
            else:
                sMain_Avisos().Resposta(sMain_Fence().decrypt(txt, senha))
        
        elif option == 'SAIR' or option == 'QUIT' or option == 'VOLTAR':
            break

