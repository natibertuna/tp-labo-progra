from gondola import *

class Verduleria (Gondola):

    #productos: zanahoria, cebolla, lechuga, 

    def __init__(self, precio_por_unidad, marca, stock, verdura, peso_vendido):
        super().__init__(precio_por_unidad, marca, stock)
        #asumo que precio por unidad es por kilo 
        self.verdura= verdura
        self.__peso_vendido = peso_vendido
        
        #calculo lo que va a ir en el carrito
        self.precio_final = self.prec*self.__peso_vendido
