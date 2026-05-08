from PRODUCTO.producto import *

class Lacteo(Producto):
    def __init__(self, nombre, codigo, marca, precio_por_unidad, stock, tipo):
        super().__init__(nombre, codigo, marca, precio_por_unidad, stock)
        self.__tipo= tipo #util por si es yogur, leche, queso, etc

        
