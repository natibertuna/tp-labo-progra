from producto import *

class Golosinas (Producto):
    def __init__(self, nombre, codigo, marca, precio_por_unidad, umbral, peso):
        super().__init__(nombre, codigo, marca, precio_por_unidad, umbral)
        self.peso=peso
        self.precio_final=self.peso*self.prec

        