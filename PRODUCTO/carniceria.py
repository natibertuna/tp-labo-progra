from PRODUCTO.producto import *

class Carniceria (Producto):

    #productos: Vacio, Asado, Costillitas, Pechito, --> esto va en el main

    def __init__(self, nombre, codigo, marca, precio_por_unidad, tipo_corte, peso_vendido):
        super().__init__(nombre, codigo, marca, precio_por_unidad)

        self.tipo_corte= tipo_corte
        self.CATEGORIA="Carniceria"
        self.peso_vendido = peso_vendido
        self.precio_final = self.calcular_precio_final()

    def calcular_precio_final(self):  # implementa el método abstracto
        if self.peso_vendido is None:
            self.tipo_corte= None
            return self._precio           # vendido por unidad (chorizo, morcilla)
        return self._precio * self.peso_vendido

    
    

    