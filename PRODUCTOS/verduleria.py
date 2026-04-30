from PRODUCTOS import Producto

class Verduleria (Producto):

    #productos: zanahoria, cebolla, lechuga, 

    def __init__(self, precio_por_unidad, marca, stock, peso_vendido):
        super().__init__(precio_por_unidad, marca, stock)
        #asumo que precio por unidad es por kilo 
        self.__peso_vendido = peso_vendido
        
        #calculo lo que va a ir en el carrito
        self.__precio_final = self.prec*self.__peso_vendido

        #if self.stock==0   --> hay que agregar la condicion de llamar a deposito
        
