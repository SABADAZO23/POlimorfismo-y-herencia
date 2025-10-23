from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre, edad, habitat):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    def dormir(self):
        return f"{self._nombre} está durmiendo"

    def get_info(self):
        return f"{self._nombre} - Edad: {self._edad} años - Hábitat: {self._habitat}"

  
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad


