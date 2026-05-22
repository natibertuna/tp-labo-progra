
#la unica funcion de la pantalla es mostrar todo el tiempo el precio total de carrito y los productos que tiene 

from CARRITO import *
from ALMACEN import *


class PantallaCarrito():
    def __init__(self, car:Carrito):
        self.carrito=car


    def mostrar_productos(self):
        #muestra todo lo que hay en el carrito

        for i in self.carrito.list_prod:
            print ("\n ELEMENTOS EN EL CARRITO")
            print ("\n", self.carrito.list_prod[i]) #imprime todo

    
    def mostrar_total(self):

        #muestra el precio total del carrito

        print ("\n MONTO TOTAL: $", self.carrito.total)

    def mostrar_promos(self):
        print("PROMOCIONES DISPONIBLES")
        print("\n PROMO GALLETITAS: 2x1 cualquier marca ")
        print("\n PROMO PERFUMERIA: 50% en cada producto")
        print("\n PROMO BEBIDAS: 30% en la segunda unidad de la misma marca")

