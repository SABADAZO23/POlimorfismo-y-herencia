from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad, habitat, pelaje, gestacion_meses):
        super().__init__(nombre, edad, habitat)
        self._pelaje = pelaje
        self._gestacion_meses = gestacion_meses

    def amamantar(self):
        return f"{self._nombre} está amamantando a sus crías"

    def get_info(self):
        return f"{super().get_info()} - Pelaje: {self._pelaje} - Gestación: {self._gestacion_meses} meses"

# Subclase Ave
class Ave(Animal):
    def __init__(self, nombre, edad, habitat, envergadura_alas, puede_volar):
        super().__init__(nombre, edad, habitat)
        self._envergadura_alas = envergadura_alas
        self._puede_volar = puede_volar

    def poner_huevos(self):
        return f"{self._nombre} está poniendo huevos"

    def get_info(self):
        vuelo = "Sí" if self._puede_volar else "No"
        return f"{super().get_info()} - Envergadura: {self._envergadura_alas}cm - Vuela: {vuelo}"

# Subclase Reptil
class Reptil(Animal):
    def __init__(self, nombre, edad, habitat, escamas, sangre_fria):
        super().__init__(nombre, edad, habitat)
        self._escamas = escamas
        self._sangre_fria = sangre_fria

    def tomar_sol(self):
        return f"{self._nombre} está tomando el sol para regular su temperatura"

    def get_info(self):
        temp = "Sangre fría" if self._sangre_fria else "Sangre caliente"
        return f"{super().get_info()} - Escamas: {self._escamas} - {temp}"
