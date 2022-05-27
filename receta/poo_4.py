
from ingrediente import Ingrediente

def main():
    #ingrediente = Ingrediente("papa", 3, "kilos")
    ingrediente = Ingrediente("papa", unidad = "kilos")
    ingrediente.cantidad = 35
    print(ingrediente)

if __name__ == "__main__":
    main()



'''
el programador de Fox conoce bastante bien las variables PUBLIC y las LOCAL.

Las variables públicas existen en toda la aplicación  y se liberan de memoria con RELEASE ALL EXTENDED (ten en cuenta que un RELEASE ALL no borra las variables públicas)

Las variables locales solo existen en la función o método en la que se definen y no pueden ser accedidas por métodos de más alto o bajo nivel (métodos o funciones que sean invocadas desde el método o función donde se crean estas variables).

Las variables PRIVATE son menos conocidas y tienen múltiples utilidades.  Estas variables se parecen a las locales en el sentido de que desaparecen cuando se acaba de finalizar el método o función en la que fueron creadas pero tienen una ventaja añadida y es que los métodos o funciones que son invocadas desde el método en el que se han creado pueden usar esa información.

Una de las ventajas más importantes de este tipo de variables es que los report que son llamados desde el método en el que son creadas pueden gozar de su uso.

'''