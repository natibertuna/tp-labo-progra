from PRODUCTO.producto import *

class Galletitas (Producto):

    #productos: Toddy, Oreo Golden, Vainillas, pitusas, sonrisa, porteñitas

    def __init__(self, nombre, codigo, marca, precio_por_unidad):
        super().__init__(nombre, codigo, marca, precio_por_unidad)
        self.CATEGORIA="Galletitas"
        self.precio_final = self.calcular_precio_final()
 
    def calcular_precio_final(self): 
        return self._precio
    

      



        

