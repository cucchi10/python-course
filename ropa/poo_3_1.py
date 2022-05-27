class Prenda:
    def __init__(self):
        self._tipo = ""
        self._talla = ""

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor
    
    @tipo.deleter
    def tipo(Self):
        del Self._tipo


    @property
    def talla(self):
        return self._talla

    @talla.setter
    def talla(self, valor):
        self._talla = valor
    
    @talla.deleter
    def talla(Self):
        del Self._talla

    def __str__(self):
        return f'''Tipo: {self.tipo}
Talla: {self.talla}'''