
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

        print ("\n PRECIO TOTAL: $", self.carrito.total)

