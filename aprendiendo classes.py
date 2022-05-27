class coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado =True
        print(f"El {self.marca}{self.modelo} se ha arrancado")

    def parar(self):
        self.arrancado = False
        print(f"El {self.marca}{self.modelo} se ha parado")


laguna = coche("Renault", "Laguna")
tesla = coche("Tesla", "Model 3")

print (type(laguna))
print (type(tesla))
print(laguna.marca, laguna.modelo)
print(tesla.marca, tesla.modelo)

laguna.arrancar()


print(laguna.arrancado)

laguna.parar()

print(laguna.arrancado)