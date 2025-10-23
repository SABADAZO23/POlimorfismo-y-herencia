from Espclas import Leon, Aguila, Serpiente
from subesp import Mamifero, Ave, Reptil

def main():
    print("=== ZOOLÓGICO VIRTUAL ===\n")

    # Crear instancias de animales
    animales = [
        Leon("Simba", 5),
        Leon("Nala", 4),
        Aguila("Thor", 3),
        Serpiente("Kaa", 8, True),
        Serpiente("Monty", 2, False)
    ]

    # Demostrar polimorfismo
    for animal in animales:
        print("=" * 50)
        print(animal.get_info())
        print(animal.hacer_sonido())
        print(animal.moverse())
        print(animal.comer())
        print(animal.dormir())

        # Comportamientos específicos de cada tipo (dentro del bucle)
        if isinstance(animal, Mamifero):
            print(animal.amamantar())
        elif isinstance(animal, Ave):
            print(animal.poner_huevos())
        elif isinstance(animal, Reptil):
            print(animal.tomar_sol())

if __name__ == "__main__":
    main()