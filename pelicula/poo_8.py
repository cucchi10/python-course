from pelicula import Pelicula

def main():
    peliculas = []
    peliculas.append(Pelicula('El Padrino', 'Francis Ford Coppola', 1972, 175))
    peliculas.append(Pelicula('Sueño De Fuga', 'Frank Darabont', 1994, 142))
    peliculas.append(Pelicula('La Lista De Schindler', 'Steven Spielberg', 1193, 195))
    peliculas.append(Pelicula('Toro Salvaje', 'Martin Scorsese', 1980, 129))
    peliculas.append(Pelicula('Casablanca', 'Michael Curtiz', 1942, 102))

    peliculas.sort()

    print('¿La Pelicula 1 es igual a la Pelicula 2 ?')
    print(peliculas[0] == peliculas[1])

    print('¿La Pelicula 3 es menor o igual a la Pelicula 2 ?')
    print(peliculas[2] <= peliculas[1])

    for pelicula in peliculas:
        print(pelicula)
        print('-'*30)
        
    print(f'Menor Pelicula en la coleccion: \n {min(peliculas)}')
    print(f'Mayor Pelicula en la coleccion: \n {max(peliculas)}')

if __name__ == "__main__":
    main()

