from PRODUCTOS import Producto

class Galletitas (Producto):

    #productos: Toddy, Oreo Golden, Vainillas, pitusas, sonrisa, porteñitas

    def __init__(self, precio_por_unidad, marca, stock):
        super().__init__(precio_por_unidad, marca, stock)
        self.galles = list

