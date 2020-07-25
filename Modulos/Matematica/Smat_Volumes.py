import sys
sys.path.append('Nucleo/')
from Nucleo.smain_Variaveis import *
import math

def mat_VOLUMES():
    sMain_Avisos().Welcome('VOLUMES')
    try:
        while True:

            option = sMain_Saidas().Prompt('MATEMATICA', 'VOLUMES')
            if option == 'CUBO' or option == '0':
                n1 = sMain_Avisos().Resposta('Digite a medida de um dos lados do CUBO', 'FLOAT')
                sMain_Avisos().Resposta(f'O volume do CUBO é:\n{n1}³ = {n1**3}')

            elif option == 'PARALELEPIPEDO' or option == '1' or option == 'PL':
                n1 = sMain_Avisos().Resposta('Digite o comprimento do PARALELEPIPEDO', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite a largura do PARALELEPIPEDO', 'FLOAT')
                n3 = sMain_Avisos().Resposta('Digite a altura do PARALELEPIPEDO', 'FLOAT')
                sMain_Avisos().Resposta(f'O volume do PARALELEPIPEDO é:\n{n1}*{n2}*{n3} = {n1*n2*n3}')

            elif option == 'PRISMA REGULAR' or option == 'PR' or option == '2':
                n1 = sMain_Avisos().Resposta('Digite a área da base do PRISMA REGULAR', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite a altura do PRISMA REGULAR', 'FLOAT')
                sMain_Avisos().Resposta(f'O volume do PRISMA REGULAR é:\n{n1}*{n2} = {n1*n2}')

            elif option == 'CILINDRO' or option == '3':
                n1 = sMain_Avisos().Resposta('Digite o raio da base do CILINDRO', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite a altura do CILINDRO', 'FLOAT')
                sMain_Avisos().Resposta(f'O volume do CILINDRO é:\n({math.pi}*{n1}²)*{n2} = {(math.pi*n1**2)*n2}')

            elif option == 'CONE' or option == '4':
                n1 = sMain_Avisos().Resposta('Digite a área da base do CONE', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite a altura do CONE', 'FLOAT')
                sMain_Avisos().Resposta(f'O volume do CONE é:\n1/3*({n1}*{n2}) = {(1/3)*(n1*n2)}')

            elif option == 'ESFERA' or option == '5':
                n1 = sMain_Avisos().Resposta('Digite o raio da ESFERA', 'FLOAT')
                sMain_Avisos().Resposta(f'O volume da esfera é:\n(4*({math.pi}*{n1}³)/3 = {(4*(math.pi*n1**3))/3}m³')

            elif option == 'VOLTAR' or option == 'SAIR' or option == 'QUIT':
                break

            elif option == '':
                pass

            else:
                sMain_Avisos().nFound(option, soda_version)

    except ValueError:
        sMain_Avisos().Erro(0)