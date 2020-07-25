import sys
from Nucleo.smain_Variaveis import *
import math


def mat_AREAS():
    sMain_Avisos().Welcome('AREAS')
    try:
        while True:
            option = sMain_Saidas().Prompt('MATEMATICA', 'AREAS')
            if option == 'QUADRADO' or option == '0':
                n1 = sMain_Avisos().Resposta('Digite a medida de um dos lados do QUADRADO', 'FLOAT')
                sMain_Avisos().Resposta(f'A area do QUADRADO é: {n1}*{n1} {n1*n1}')

            elif option == 'RETANGULO' or option == '1':
                while True:
                    n1 = sMain_Avisos().Resposta('Digite o comprimento do retangulo', 'INT')
                    n2 = sMain_Avisos().Resposta('Digite a largura do RETANGULO', 'INT')
                    if n1 == n2:
                        sMain_Avisos().Erro(1)
                        continue
                    else:
                        sMain_Avisos().Resposta(f'A area do RETANGULO é: {n1}*{n2} = {n1*n2}')
                        break

            elif option == 'TRIANGULO' or option == '2':
                n1 = sMain_Avisos().Resposta('Digite o tamanho da base do TRIANGULO', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite a altura do TRIANGULO', 'FLOAT')
                sMain_Avisos().Resposta(f'A área do TRIANGULO é: ({n1}*{n2})/2 = {(n1*n2)/2}')

            elif option == 'LOSANGULO' or option == '3':
                while True:
                    n1 = sMain_Avisos().Resposta('Digite a Diagonal Maior do LOSANGULO', 'FLOAT')
                    n2 = sMain_Avisos().Resposta('Digite a Diagonal Menor do LOSANGULO', 'FLOAT')
                    if n2 > n1:
                        sMain_Avisos().Erro(2)
                        continue
                    else:
                        sMain_Avisos().Resposta(f'A área do LOSANGULO é: ({n1}*{n2})/2 = {(n1*n2)/2}')
                        break

            elif option == 'TRAPEZIO' or option == '4':
                while True:
                    n1 = sMain_Avisos().Resposta('Digite a Base Maior do TRAPEZIO', 'FLOAT')
                    n2 = sMain_Avisos().Resposta('Digite a Base Menor do TRAPEZIO', 'FLOAT')
                    n3 = sMain_Avisos().Resposta('Digite a Altura do TRAPEZIO', 'FLOAT')
                    if n1 < n2:
                        sMain_Avisos().Erro(2)
                        continue
                    else:
                        sMain_Avisos().Resposta(f'A Area do TRAPEZIO é: (({n1}+{n2})/2)*{n3} = {((n1+n2)/2)*n3}')
                        break

            elif option == 'POLIGONO REGULAR' or option == 'PR' or option == '5':
                n1 = sMain_Avisos().Resposta(f'Digite o perimetro do POLIGONO REGULAR', 'FLOAT')
                n2 = sMain_Avisos().Resposta(f'Digite a apótema do POLIGONO REGULAR', 'FLOAT')
                sMain_Avisos().Resposta(f'A área do POLIGONO REGULAR é: ({n1}/2)*{n2} = {(n1/2)*n2}')

            elif option == 'CIRCULO' or option == '6':
                n1 = sMain_Avisos().Resposta('Digite o raio do CIRCULO', 'FLOAT')
                sMain_Avisos().Resposta(f'A área do CIRCULO é: {math.pi}*n1² = {math.pi*n1**2}')
                sMain_Avisos().Resposta(f'O perimetro do CIRCULO é: 2*{math.pi}*n1 = {2*math.pi*n1}')

            elif option == 'CONE' or option == '7':
                n1 = sMain_Avisos().Resposta('Digite o raio do CONE', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite a geratriz do CONE', 'FLOAT')
                sMain_Avisos().Resposta(f'A área do CONE é: ({math.pi}*{n1})*{n2} = {(math.pi * n1)*n2}')

            elif option == 'ESFERA' or option == '8':
                n1 = sMain_Avisos().Resposta('Digite o raio da ESFERA', 'FLOAT')
                sMain_Avisos().Resposta(f'A área da ESFERA é: 4*{math.pi}*{n1}² = {4*math.pi*n1**2}')


            elif option == 'VOLTAR' or option == 'SAIR' or option == 'QUIT':
                break

            elif option == '':
                pass

            else:
                sMain_Avisos().nFound(option)
                continue
    except ValueError:
        sMain_Avisos().Erro(0)
        mat_AREAS()
