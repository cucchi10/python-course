
from estudiante import Estudiante

def main():
    nombre = input('Nombre del estudiante: ')
    edad = input('Edad del estudiante: ')
    promedio = float(input("Promedio: "))
    codigo = input("Codigo: ")

    estudiante = Estudiante(nombre, edad, promedio, codigo)

    print(f'''Los datos del estudiante son: 
{estudiante}''')
    print('-'*30)
    estudiante.estudiar("Historia del Mundo del Arte de la Guerra")

if __name__ == '__main__':
    main()
