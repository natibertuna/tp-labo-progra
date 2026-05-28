from PRODUCTO.producto import *

class Bebidas (Producto):

    #productos: Sprite, Cunnington, Agua, Manaos, Aquarius

    def __init__(self, nombre, codigo, marca, precio_por_unidad,litros):
        super().__init__(nombre, codigo, marca, precio_por_unidad)
        self.litros = litros
        self.CATEGORIA= "Bebidas"
        self.precio_final=self.calcular_precio_final()

    def calcular_precio_final(self):  # implementa el método abstracto
       return self._precio



        




