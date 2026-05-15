from PRODUCTO.producto import *


class Higiene (Producto):
    def __init__(self, nombre, codigo, marca, precio_por_unidad,umbral, tipo):
        super().__init__(nombre, codigo, marca, precio_por_unidad, umbral)
        self.__tipo= tipo #papel, toallitas, tampones
        self.precio_final=self.prec
        self.CATEGORIA="Higiene"
