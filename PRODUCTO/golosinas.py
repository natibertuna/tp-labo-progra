from PRODUCTO.producto import *

class Golosinas (Producto):
    def __init__(self, nombre, codigo, marca, precio_por_unidad, peso):
        super().__init__(nombre, codigo, marca, precio_por_unidad)
        self.peso=peso  #en gramos
        self.CATEGORIA =  "Golosinas"

        self.precio_final = self.calcular_precio_final()
 
    def calcular_precio_final(self):  # implementa el método abstracto
        return self._precio*(self.peso/1000)

        