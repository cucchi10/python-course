'''
Hereda de Persona
Atribusto:
    deporte -- q practica
comportamientos:
    entrenar --
'''

from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre="", edad=None, deporte=""):
        super().__init__(nombre, edad)
        self._deporte = deporte

    @property
    def deporte(self):
        return self._deporte

    @deporte.setter
    def deporte(self, valor):
        self._deporte = valor

    @deporte.deleter
    def deporte(self):
        del self._deporte

    def entrenar(self):
        print(f'{self.nombre} esta entrenardo {self.deporte}')
    
    '''@property
    def entrenar(self):
        return self._entrenar

    @entrenar.setter
    def entrenar(self, valor):
        self._entrenar = valor

    @entrenar.deleter
    def entrenar(self):
        del self._entrenar'''

    def __str__(self):
        return f'''{super().__str__()}
Deporte: {self.deporte}       '''
