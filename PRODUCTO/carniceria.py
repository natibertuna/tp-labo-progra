from PRODUCTO.producto import *

class Carniceria (Producto):

    #productos: Vacio, Asado, Costillitas, Pechito, --> esto va en el main

    def __init__(self, nombre, codigo, marca, precio_por_unidad, stock, umbral_min, umbral_max, tipo_corte, peso_vendido):
        super().__init__(nombre, codigo, marca, precio_por_unidad, stock, umbral_min, umbral_max)

        self.tipo_corte= tipo_corte
        self.CATEGORIA="Carniceria"
        self.peso_vendido = peso_vendido
        self.precio_final = self.peso_vendido*self.prec

        if self.nombre=="Morcilla" or self.nombre == "Chorizo":
            self.tipo_corte=None
            self.peso_vendido= None #no existe el peso porque viene por unidad

            self.precio_final=self.prec


    
    

    