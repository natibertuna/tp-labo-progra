 #clase padre

from abc import ABC
from abc import abstractmethod, __str__
import os
os.system('cls')

class Producto(ABC):
    def __init__(self,nombre, codigo, marca,  precio_por_unidad ):

        self._precio = precio_por_unidad
        self.precio_final=0
        self.CATEGORIA= ""
        self.nombre = nombre
        self.marca = marca
        self.codigo_barras= codigo

   
    @property
    def precio(self):
        return self._precio
    

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = nuevo_precio


    #defino un metodo magico para imprimir las cosas

    def __str__(self):
        return f"[{self.codigo_barras}] {self.nombre} ({self.marca}) {self.CATEGORIA} - ${self._precio}"
    
    @abstractmethod
    def calcular_precio_final(self):
        """Cada subclase define cómo se calcula su precio final."""
        pass


