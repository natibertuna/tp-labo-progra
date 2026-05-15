from PRODUCTO.producto import *

class Bebidas (Producto):

    #productos: Sprite, Cunnington, Agua, Manaos, Aquarius

    def __init__(self, nombre, codigo, marca, precio_por_unidad,umbral,litros):
        super().__init__(nombre, codigo, marca, precio_por_unidad, umbral)
        self.litros = litros
        self.CATEGORIA= "Bebidas"
        self.precio_final=self.prec



        




