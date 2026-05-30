from PRODUCTO.producto import *

class Verduleria (Producto):

    #productos: zanahoria, cebolla, lechuga, 

    def __init__(self, nombre, codigo, marca, precio_por_unidad ,peso_disponible):
        super().__init__(nombre, codigo, marca, precio_por_unidad)

        #asumo que precio por unidad es por kilo 
        self.peso_disponible:float = peso_disponible #es en kg
        self.CATEGORIA="Verduleria"
        self.precio_final = self.calcular_precio_final()

    def calcular_precio_final(self): 
        return self._precio * self.peso_vendido

        
