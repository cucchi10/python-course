from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre="", edad=None, promedio=None, Codigo=''):
        super().__init__(nombre, edad)
        self._promedio = promedio
        self._codigo = Codigo


    @property
    def promedio(self):
        return self._promedio

    @promedio.setter
    def promedio(self, valor):
        if valor < 0.0:
            self._promedio = None
        self._promedio = valor

    @promedio.deleter
    def promedio(self):
        del self._promedio

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @codigo.deleter
    def codigo(self):
        del self._codigo
    
    
    def estudiar(self, materia):
        print(f'{self.nombre} esta estudiando {materia}')

    def __str__(self):
        return f'''{super().__str__()}
Promedio: {self.promedio}
Codigo: {self.codigo}'''