from PRODUCTOS.producto import Producto

class Verduleria(Producto):

    def __init__(self, nombre, precio, marca, disponibilidad, codigo_barra, peso_vendido, precio_unidad):
        super().__init__(nombre, precio, marca, disponibilidad, codigo_barra)

        self.__peso_vendido = peso_vendido
        self.__precio_unidad = precio_unidad

        self.__precio_final = self.__precio_unidad * self.__peso_vendido

        #if self.stock==0   --> hay que agregar la condicion de llamar a deposito
        
