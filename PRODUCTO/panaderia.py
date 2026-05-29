from PRODUCTO.producto import *

class Panaderia (Producto):

    def _init_(self, nombre, codigo, marca, precio_por_unidad,tipo):
        super()._init_(nombre, codigo, marca, precio_por_unidad)
        self.__tipo = tipo #lactal,pebete,etc.
        self.CATEGORIA="Panaderia"
        self.precio_final = self.calcular_precio_final()
 
    @property
    def tipo(self):
        return self.__tipo
 
    def calcular_precio_final(self):  
        return self._precio

            
            