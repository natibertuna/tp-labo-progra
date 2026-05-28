from PRODUCTO.producto import *


class Perfumeria (Producto):
    def __init__(self, nombre, codigo, marca, precio_por_unidad, tipo):
        super().__init__(nombre, codigo, marca, precio_por_unidad)
        self.__tipo= tipo  #cuantos ml tiene
        self.CATEGORIA="Perfumeria"
        self.precio_final = self.calcular_precio_final()
 
    @property
    def tipo(self):
        return self.__tipo
 
    def calcular_precio_final(self): 
        return self._precio
