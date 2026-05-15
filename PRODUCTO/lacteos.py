from PRODUCTO.producto import *

class Lacteo(Producto):
    def __init__(self, nombre, codigo, marca, precio_por_unidad, stock, umbral_min, umbral_max, tipo):
        super().__init__(nombre, codigo, marca, precio_por_unidad, stock, umbral_min, umbral_max)
        self.__tipo= tipo #util por si es yogur, leche, queso, etc
        self.precio_final=self.prec
        self.CATEGORIA="Lacteos"

        
