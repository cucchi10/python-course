from persona import Persona

def main():
    persona_1 = Persona()
    persona_2 = Persona()

    persona_1.nombre = "Roque Narvaja"
    persona_1.edad = 63

    persona_2.nombre = "Eddy Ficio"
    persona_2.edad = 99

    print("Datos de la primer persona: ")
    print(f"Nombre: {persona_1.nombre}")
    print(f"Edad: {persona_1.edad}")

    print("Datos de la segunda persona: ")
    print(f"Nombre: {persona_2.nombre}")
    print(f"Edad: {persona_2.edad}")
    
    persona_1.hablar(f"Hola {persona_2.nombre}, como se encuentra usted?")
    persona_2.hablar(f"Hey Guachin {persona_1.nombre}, todo liso y naranja?")

    persona_1.comer(f"Manzana")
    persona_2.comer(f"Vino con sandia")

if __name__ == "__main__":
    main()