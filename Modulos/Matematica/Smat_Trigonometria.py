import sys
from Nucleo import *
import math

def mat_TRIGONOMETRIA():
    sMain_Avisos().Welcome('TRIGONOMETRIA')
    while True:
        try:
            option = sMain_Saidas().Prompt('MATEMATICA', 'TRIGONOMETRIA')
            if option == 'PROGRESSAO ARITMETICA' or option == 'P.A' or option == '0':
                n1 = sMain_Avisos().Resposta('Digite o primeiro termo de sua P.A', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite o segundo termo de sua P.A','FLOAT')
                n3 = sMain_Avisos().Resposta('Digite o termo a ser descoberto', 'FLOAT')
                sMain_Avisos().Resposta(f'O {n3}º termo de sua PA é:\n\nAn = {n1}+({n3}-1)*{n2-n1} = {n1 + (n3 - 1) * (n2 - n1)}')

            elif option == 'PROGRESSAO GEOMETRICA' or option == 'P.G' or option == '1':
                n1 = sMain_Avisos().Resposta('Digite o termo a ser descoberto', 'FLOAT')
                sMain_Avisos().Resposta(f'O {n1}º termo da PG é:\n({n1}²+{n1})/2 = {(n1**2 + n1)/2}')
            elif option == 'RAZAO' or option == '2':
                n1 = sMain_Avisos().Resposta('Digite o primeiro termo de sua sequencia', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite o segundo termo de sua sequencia', 'FLOAT')
                sMain_Avisos().Resposta(f'A razao de sua sequencia é:\n{n2}-{n1} = {n2-n1}')

            elif option == 'SOMA DOS TERMOS DE UMA PA' or option == 'S.N' or option == '3':
                n1 = sMain_Avisos().Resposta('Digite o numero de termos de sua P.A', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite a razao de sua P.A', 'FLOAT')
                n3 = sMain_Avisos().Resposta('Digite o primeiro termo de sua P.A', 'FLOAT')
                an = n3 + (n1 - 1)*n2
                sMain_Avisos().Resposta(f'O ultimo termo desta P.A equivale a:\n\nAn = {n3} + ({n1} - 1)*{n2}\nAn = {n3 + (n1 - 1)*n2}')
                sMain_Avisos().Resposta(f'A soma dos termos desta P.A equivale a:\n\nSn = ({n1}({n2} + {an}))/2 = {(n1*(n2 + an))/2}')


            elif option == 'NUMEROS TRIANGULARES' or option == 'N.T' or option == '4':
                n1 = sMain_Avisos().Resposta('Digite o termo desejado (n)', 'INT')
                sMain_Avisos().Resposta(f'O {n1}º termo é: {(n1 * (n1 + 1)) / 2}')

            elif option == 'DELTA' or option == '5':
                sMain_Avisos().Resposta('OBS: Caso a formula não tenha um dos termos , digite 0')
                n1 = sMain_Avisos().Resposta('Digite o termo (a)', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite o termo (b)', 'FLOAT')
                n3 = sMain_Avisos().Resposta('Digite o termo (c)', 'FLOAT')
                r = n2 ** 2 - 4 * n1 * n3
                if r <= 0:
                    sMain_Avisos().Resposta('Delta igual ou menor que 0')
                else:
                    sMain_Avisos().Resposta(f'Delta é igual a: {n2}²-4*{n1}*{n3} = {r}')
                    r = math.sqrt(r)
                    r2 = (-(n2) + r) / 2 * (n1)
                    r3 = (-(n2) - r) / 2 * (n1)

                    sMain_Avisos().Resposta(f'+X é igual a: (-{n2}+{r})/2*{n1} = {r2}')
                    sMain_Avisos().Resposta(f'-X é igual a: (-{n2}-{r})/2*{n1} = {r3}')

            elif option == 'HIPOTENUSA' or option == '6':
                n1 = sMain_Avisos().Resposta('Digite o valor de um cateto', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite o valor de outro cateto', 'FLOAT')
                sMain_Avisos().Resposta(f'A hipotenusa é igual a:\nH² = {n1}² + {n2}² = {math.sqrt(n1**2 + n2**2)}²\nH = {n1**2} + {n2**2} = {n1**2 + n2**2}')

            elif option == 'CATETO' or option == '7':
                n1 = sMain_Avisos().Resposta('Digite o valor do cateto', 'FLOAT')
                n2 = sMain_Avisos().Resposta('Digite o valor da HIPOTENUSA', 'FLOAT')
                sMain_Avisos().Resposta(f'C² + {n1}² = {n2}²\nC² = {n2**2} - {n1**2}\nC² = {n2**2 - n1**2}\nC = {math.sqrt(n2**2 - n1**2)}')



            elif option == 'VOLTAR' or option == 'SAIR' or option == 'QUIT':
                break

            elif option == '':
                pass

            else:
                sMain_Avisos().nFound(option)

        except ValueError:
            sMain_Avisos().Erro(0)

