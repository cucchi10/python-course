import json
from libro import *
import os
import pathlib

class Biblioteca:
    AGREGAR_LIBRO = 1
    CONSULTAR_LIBROS = 2
    BUSCAR_LIBRO = 3
    SALIR = 0

    def __init__(self):
        self._libros = []
        self.recuperar_libros('libros.json')

    def __del__(self):
        self.almacenar_libros('libros.json')

    @property
    def libros(self):
        return self._libros
    @libros.setter
    def libros(self,valor):
        self.libros = valor
    @libros.deleter
    def libros(self):
        del self._libros

    def recuperar_libros(self, ruta):
        if pathlib.Path(ruta).exists():
            with open(ruta, 'r') as archivo:
                datos = json.load(archivo)
            for lib in datos['libros']:
                self.libros.append(desde_json(lib))

    def almacenar_libros(self, ruta):
        with open(ruta, 'w') as archivo:
            json.dump({'libros':self.libros}, archivo, cls=Libro_Encoder, indent=4)

    def agregar_libros(self):
        os.system('cls')
        print('         Agregar Libro')
        isbn = input('isbn: ')
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        self.libros.append(Libro(isbn, titulo, autor))

    def consultar_libros(self):
        os.system('cls')
        print('         Consultar Libro')
        if len(self.libros) == 0:
            print('No hay Libros registrados...')
        else:
            for lib in self.libros:
                print(f'{lib}')
                print('-'*50)

    def buscar_libro(self):
        os.system('cls')
        print('         Buscar Libro')
        nombre_titulo = input('Ingrese el Nombre del Libro que esta buscando: ').title
        i = 0
        encontrado = False
        while  not encontrado :
            if nombre_titulo == self.libros[i]:
             encontrado = True
        else:
             i+1


    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f'''          Biblioteca
{Biblioteca.AGREGAR_LIBRO}) Agregar Libro
{Biblioteca.CONSULTAR_LIBROS}) Consultar Libros
{Biblioteca.BUSCAR_LIBRO}) Buscar Libro por su Titulo
{Biblioteca.SALIR}) Salir''')
            opc = input('Selecciona una opcion: ')
            try:
                opc= int(opc)
            except:
                opc = -1
            if opc == Biblioteca.AGREGAR_LIBRO:
                self.agregar_libros()
            elif opc == Biblioteca.CONSULTAR_LIBROS:
                self.consultar_libros()
            elif opc == Biblioteca.BUSCAR_LIBRO:
                self.buscar_libro()
            elif opc == Biblioteca.SALIR:
                continuar = False
            else:
                os.system('cls')
                print('Opcion no valida')
            input('Presiona una tecla para continuar')
        input('Presiona enter para Salir.')
