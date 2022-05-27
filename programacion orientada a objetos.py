
class Figura:
    def __init__(self):
        self._lados = None

    @property #getter: Regresa el valor asociado a la cantidad de lados
    def lados(self):
        return self._lados

    @lados.setter #permite asignarle valor a la propiedad o atributo
    def lados(self,valor):
        if valor < 3:
            print("El valor debe ser mayo que 3")
            self._lados = None
        else:
            self._lados = valor

    @lados.deleter #permite borrar valor a la propiedad o atrabitu
    def lados(self):
        del self._lados

def main():
    triangulo = Figura()
    cuadrado = Figura()
    triangulo.lados = -3
    cuadrado.lados = 4
    #del cuadrado.lados
    print(f"El tiangrulo tiene {triangulo.lados} lados")
    print(f"El cuadrado tiene {cuadrado.lados} lados")

if __name__ == "__main__":
    main()
