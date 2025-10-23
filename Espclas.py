from subesp import Mamifero, Ave, Reptil

class Leon(Mamifero):
    def __init__(self, nombre, edad, melena=True):
        super().__init__(nombre, edad, "Sabana", "Corto y dorado", 4)
        self._melena = melena

    def hacer_sonido(self):
        return f"🦁 {self._nombre} ruge: ¡GRRRR!"

    def moverse(self):
        return f"{self._nombre} corre ágilmente por la sabana"

    def comer(self):
        return f"{self._nombre} caza y come carne"

    def get_info(self):
        melena_info = "con melena" if self._melena else "sin melena"
        return f"León {melena_info} - {super().get_info()}"

class Aguila(Ave):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Montañas", 200, True)

    def hacer_sonido(self):
        return f"🦅 {self._nombre} chilla: ¡Kreee!"

    def moverse(self):
        return f"{self._nombre} vuela majestuosamente por el cielo"

    def comer(self):
        return f"{self._nombre} caza pequeños mamíferos"

    def get_info(self):
        return f"Águila - {super().get_info()}"

class Serpiente(Reptil):
    def __init__(self, nombre, edad, venenosa=False):
        super().__init__(nombre, edad, "Jungla", "Escamas lisas", True)
        self._venenosa = venenosa

    def hacer_sonido(self):
        return f"🐍 {self._nombre} sisea: Ssssss..."

    def moverse(self):
        return f"{self._nombre} se desliza silenciosamente"

    def comer(self):
        return f"{self._nombre} traga enteras a sus presas"

    def get_info(self):
        veneno = "Venenosa" if self._venenosa else "No venenosa"
        return f"Serpiente ({veneno}) - {super().get_info()}"
