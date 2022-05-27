'''
atributo:
    tipo
    ataque
    energia
    fuerza

comportamietnos:
    atacar
'''

rocho = 0
limpia_vidrio = 1
trapito = 2

tipos = [rocho, limpia_vidrio, trapito]

class Enemigo:
    def __init__(self, tipo='', ataque='', energia=5,fuerza=5):
        self._tipo = tipo
        self._ataque = ataque
        self._energia = energia
        self._fuerza = fuerza


    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo (self, valor):
        self._tipo = valor
    @tipo.deleter
    def tipo(self):
        del self._tipo

    @property
    def ataque(self):
        return self._ataque
    @ataque.setter
    def ataque(self, valor):
        self._ataque = valor
    @ataque.deleter
    def ataque(self):
        del self._ataque

    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self, valor):
        self._energia = valor
    @energia.deleter
    def energia(self):
        del self._energia

    @property
    def fuerza(self):
        return self._fuerza
    @fuerza.setter
    def fuerza(self, valor):
        self._fuerza = valor
    @fuerza.deleter
    def fuerza(self):
        del self._fuerza

    def atacar(self):
        print(f'''{self.tipo} ha atacado con {self.ataque} y causo {self.fuerza} de daño.''')

class Rocho(Enemigo):
    def __init__(self):
        super().__init__("Rocho", "Lanza llamas de Vino con Naranja",12,8)

class Limpia_Vidrio(Enemigo):
    def __init__(self):
        super().__init__("Limpia Vidrio", "Hidrobomba en Semaforo",15,12)

class Trapito(Enemigo):
    def __init__(self):
        super().__init__("Trapito", "Robo Siniestro de Monedas",12,10)
        self._recuperacion = 4

    @property
    def recuperacion(self):
        return self._recuperacion
    @recuperacion.setter
    def ecuperacion(self, valor):
        self._recuperacion = valor
    @recuperacion.deleter
    def recuperacion(self):
        del self._recuperacion  
    
    def atacar(self):
        super().atacar()
        print(f'{self.tipo} ha recuperado {self.recuperacion} energia.')
        self.energia += self.recuperacion