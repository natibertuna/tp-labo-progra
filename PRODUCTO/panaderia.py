
from PRODUCTO.producto import *

class Panaderia (Producto):

    #productos: miÑon, figasita,  

    def __init__(self, nombre, codigo, marca, precio_por_unidad, stock, umbral_min, umbral_max, tipo_pan, bolsones, peso):
        super().__init__(nombre, codigo, marca, precio_por_unidad, stock, umbral_min, umbral_max)
        self.peso = peso
        self.__pan = tipo_pan
        self.bolsones_depan = bolsones
        self.lista= list
        self.CATEGORIA="Panaderia"


 
        #FALTA DEFINIR LA PARTE DE FACTURAS


            
            