from PRODUCTO.producto import *

class Verduleria (Producto):

    #productos: zanahoria, cebolla, lechuga, 

    def __init__(self, nombre, codigo, marca, precio_por_unidad, stock, umbral_min, umbral_max,peso_vendido):
        super().__init__(nombre, codigo, marca, precio_por_unidad, stock, umbral_min, umbral_max)

        #asumo que precio por unidad es por kilo 
        self.peso_vendido = peso_vendido
        self.CATEGORIA="Verduleria"
        
        #calculo lo que va a ir en el carrito
        self.precio_final = self.prec*self.peso_vendido #se encuentra en kilogramos

        
