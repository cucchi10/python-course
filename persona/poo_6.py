

'''class Derivada (Base_1, Base_n):
    instrucciones'''

from persona import Persona
from deportista import Deportista


def main():
    per_1= Persona('Hector Nillo', 44)
    deportista = Deportista('Susana Torio', 33, 'Natacion')

    print(f'''Datos de la persona:
{per_1} ''')
    print('-'*30)
    print(f'''Datos de la persona:
{deportista} ''')

    deportista.entrenar()
    deportista.hablar('Listo para ganar una medalla')


if __name__ == '__main__':
    main()