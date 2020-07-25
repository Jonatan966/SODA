import sys
sys.path.append('Nucleo/')
sys.path.append('Modulos/')
from Nucleo import *
from Modulos import *

'''
    Aqui ficará todos os Handlers de todos os módulos
    para deixar o sistema mais dinâmico, e mais fácil
    para futuras alterações.
'''

class sMain_Handlers:
    def matHandler(self, name):
        name = name.upper()
        return globals().get(f"mat_{name}")

    def crtHandler(self, name):
        name = name.upper()
        return globals().get(f"crt_{name}")

    def quiHandler(self, name):
        name = name.upper()
        return globals().get(f'qui_{name}')
