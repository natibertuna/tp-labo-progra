 #clase padre

from abc import ABC

class Producto(ABC):
    def __init__(self,nombre, codigo, marca,  precio_por_unidad ):

        self._precio = precio_por_unidad
        self.precio_final=0
        self.CATEGORIA= ""
        self.nombre = nombre
        self.marca = marca
        self.codigo_barras= codigo

   
    @property
    def precio_por_unidad(self):
        return self._precio
    

    @precio_por_unidad.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = nuevo_precio


    #defino un metodo magico para imprimir las cosas

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} ({self.marca}) {self.CATEGORIA} - ${self.precio}"
    
    @abstractmethod
    def crear_producto(self):

        #
