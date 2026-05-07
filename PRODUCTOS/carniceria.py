<<<<<<<< HEAD:PRODUCTO/carniceria.py
from PRODUCTO.producto import *
========
from PRODUCTOS.producto import Producto
>>>>>>>> 9a98c5e93bedc8da104e5a3604dd3f61d5b9d025:PRODUCTOS/carniceria.py

#IPO DE CORTE, PREC P/ KILO, PESO VENDIDO Y CALCULAR SU PRECIO


class Carniceria (Producto):

    #productos: Vacio, Asado, Costillitas, Pechito, --> esto va en el main

    def __init__(self, nombre, codigo, marca, precio_por_unidad, stock, tipo_corte, peso_vendido):
        super().__init__(nombre, codigo, marca, precio_por_unidad, stock)

        self.tipo_corte= tipo_corte
        self.peso_vendido = peso_vendido
        self.precio_final = self.peso_vendido*self.prec

        if self.nombre=="Morcilla" or self.nombre == "Chorizo":
            self.tipo_corte=None
            self.peso_vendido= None #no existe el peso porque viene por unidad

            self.precio_final=self.prec


    
    

    