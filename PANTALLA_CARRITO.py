
#la unica funcion de la pantalla es mostrar todo el tiempo el precio total de carrito y los productos que tiene 

from __future__ import annotations
from typing import TYPE_CHECKING

#evito bucles

if TYPE_CHECKING:
    from CARRITO import Carrito
import os
os.system('cls')


class PantallaCarrito():
    def __init__(self, car:Carrito):
        self.carrito=car


    def mostrar_productos(self):
        #muestra todo lo que hay en el carrito

        for i in self.carrito.list_prod:
            print ("\n ----------- ELEMENTOS EN EL CARRITO----------------")

            if not self.carrito.list_prod:
                print ("El carrito se encuentra vacio ")
            else:
                for prod in self.carrito.list_prod:
                    print (f"  - [{prod.codigo_barras}]   [{prod.nombre}] [{prod.marca}] [{prod.codigo_barras}] "
                           f"  - $[{prod.precio:.2f}] ") 
                    #imprime todo

    
    def mostrar_total(self):

        #muestra el precio total del carrito

        print ("\n MONTO TOTAL: $", self.carrito.total)

    def mostrar_promos(self):
        print("PROMOCIONES DISPONIBLES")
        print("\n PROMO GALLETITAS: 2x1 cualquier marca ")
        print("\n PROMO PERFUMERIA: 50% en cada producto")
        print("\n PROMO BEBIDAS: 30% en la segunda unidad de la misma marca")

