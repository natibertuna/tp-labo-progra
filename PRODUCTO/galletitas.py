from PRODUCTO.producto import *

class Galletitas (Producto):

    #productos: Toddy, Oreo Golden, Vainillas, pitusas, sonrisa, porteñitas

    def __init__(self, nombre, codigo, marca, precio_por_unidad, umbral):
        super().__init__(nombre, codigo, marca, precio_por_unidad, umbral)
        self.precio_final=self.prec
        self.CATEGORIA="Galletitas"

      



        

