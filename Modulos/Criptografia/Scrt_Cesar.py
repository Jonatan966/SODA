import sys
sys.path.append('Nucleo/')
from Nucleo.smain_Variaveis import *

abc = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,;:?!-_~#"'&()[]|`\/@°+=*$£€<> '''
n = 0

# error = 'Informacao Invalida'
class sMain_CESAR:
    def cifrar(self, texto, rot):
        text_cifrado = ''
        texto = str(texto)
        for letra in texto:
            soma = abc.find(letra) + rot
            modulo = int(soma) % len(abc)
            text_cifrado = text_cifrado + str(abc[modulo])

        return text_cifrado

    def decifrar(self, texto, rot):
        text_cifrado = ''
        texto = str(texto)

        for letra in texto:
            soma = abc.find(letra) - rot
            modulo = int(soma) % len(abc)
            text_cifrado = text_cifrado + str(abc[modulo])

        return text_cifrado
        

def crt_CESAR():
    sMain_Avisos().Welcome('CESAR')
    print('OBS: Este método de criptografia não é um dos mais seguros, favor utiliza-lo somente para fins educacionais.')

    while True:
        option = sMain_Saidas().Prompt('CRIPTOGRAFIA', 'CESAR')
        if option == 'CIFRAR' or option == '0':
            n = sMain_Avisos().Resposta('Digite a senha desejada(SOMENTE NUMEROS)', 'INT')
            c = sMain_Avisos().Resposta('Digite o texto a ser CIFRADO (NÃO INSIRA SÓ NÚMEROS)', 'STRING')  # .lower()
            if n == 0 or c == '':
                sMain_Avisos().Resposta("ERRO: Senha não pode ser igual a 0")
                continue
            sMain_Avisos().Resposta(sMain_CESAR().cifrar(c, n))

        elif option == 'DECIFRAR' or option == '1':
            n = sMain_Avisos().Resposta('Digite a senha correta (SOMENTE NUMEROS)', 'INT')
            c = sMain_Avisos().Resposta('Digite o texto a ser DECIFRADO (NÃO INSIRA SÓ NÚMEROS)', 'STRING')  # .lower()
            if n == 0 or c == '':
                sMain_Avisos().Resposta("ERRO: Senha não pode ser igual a 0")
                continue
            sMain_Avisos().Resposta(sMain_CESAR().decifrar(c, n))
        
        elif option == 'PADRAO' or option == 'PADRÃO' or option == '2':
            sMain_Avisos().Resposta(f"Padrão de caracteres: {abc}")

        elif option == 'SAIR' or option == 'QUIT' or option == 'VOLTAR':
            break