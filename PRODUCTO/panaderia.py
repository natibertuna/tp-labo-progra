
from PRODUCTO.producto import *

class Panaderia (Producto):

    #productos: miÑon, figasita,  

    def __init__(self, nombre, codigo, marca, precio_por_unidad,tipo_pan, bolsones, peso):
        super().__init__(nombre, codigo, marca, precio_por_unidad)
        self.peso = peso
        self.__pan = tipo_pan
        self.cantidad = bolsones
        self.lista= list
        self.CATEGORIA="Panaderia"
        self.precio_final = self.calcular_precio_final()
 
    @property
    def tipo(self):
        return self.__tipo
 
    def calcular_precio_final(self):  # FIX: implementa el método abstracto
        return self._precio


 
    #FALTA DEFINIR LA PARTE DE FACTURAS


            
            