from PRODUCTOS.producto import Producto

#IPO DE CORTE, PREC P/ KILO, PESO VENDIDO Y CALCULAR SU PRECIO


class Carniceria (Producto):

    #productos: Vacio, Asado, Costillitas, Pechito, --> esto va en el main

    def __init__(self, precio_por_unidad, marca, stock, tipo_corte, peso_vendido):
        super().__init__(precio_por_unidad, marca, stock)

        self.tipo_corte= tipo_corte
        self.peso_vendido = peso_vendido
        self.precio_final = self.peso_vendido*self.prec

        if self.marca=="Morcilla" or self.marca == "Chorizo":
            self.tipo_corte=None
            self.peso_vendido= None #no existe el peso porque viene por unidad

            self.precio_final=self.prec


    
    

    