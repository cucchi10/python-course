

import enemigo
import os
import random

def main():
    enemigos =[]
    for i in range(5):
        tipo_enemigo = random.randint(0, len(enemigo.tipos)-1)
        if tipo_enemigo == enemigo.rocho:
            enemigos.append(enemigo.Rocho())
        elif tipo_enemigo == enemigo.limpia_vidrio:
            enemigos.append(enemigo.Limpia_Vidrio())
        else:
            enemigos.append(enemigo.Trapito())

    '''for e in enemigos:
        os.system('cls')
        e.atacar()
        input('Presiona enter para continuar...')'''


    personaje = {'energia': 100, 'fuerza': 6}
    ganancia_energia = 5
    incremento_fuerza = 2

    while personaje['energia'] > 0 and len(enemigos) > 0:
        while personaje['energia'] > 0 and enemigos[0].energia > 0:
            os.system('cls')
            print(f'Personaje: {personaje["energia"]} VS {enemigos[0].tipo}: {enemigos[0].energia}')
            enemigos[0].atacar()
            personaje['energia'] -= enemigos[0].fuerza
            if personaje['energia'] > 0:
                print(f'Has atacado a {enemigos[0].tipo} y causaste {personaje["fuerza"]} de daño.')
                enemigos[0].energia -= personaje['fuerza']
                input('Continuar Batalla...')
        if personaje['energia'] > 0:
            os.system('cls')
            print(f'Energia: {personaje["energia"]} {enemigos[0].tipo}: {enemigos[0].energia}')
            print(f'Has derrotado a {enemigos[0].tipo}')   
            print(f'Fas recuperado {ganancia_energia} de energia y ganaste {incremento_fuerza} de fuerza.')
            personaje['energia'] += ganancia_energia
            personaje['fuerza'] += incremento_fuerza
            enemigos.pop(0)
            input('Continuar Aventura...')
    if personaje['energia'] > 0:
        print('Has vencido a todos tus rivales!')
    else:
        print('Has sido vencido, RIP')


if __name__ == "__main__":
    main()