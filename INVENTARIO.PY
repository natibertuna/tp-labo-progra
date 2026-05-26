from __future__ import annotations
from typing import TYPE_CHECKING


from GONDOLA import *
from PRODUCTO import *

if TYPE_CHECKING:
    from ALMACEN import *

class Inventario:
    def __init__(self, gondolas: list, almacen: "Almacen"):
        self.gondolas= gondolas
        self.almacen= almacen
        self.depo={} #reemplaza el deposito.
    
    #def stock()
        
    #Debe interactuar con los métodos que decrementan el stock (ej., al agregar un producto al carrito
    # de compras) para verificar si la cantidad disponible se encuentra por debajo del umbral mínimo de
    # reposición.

    def agregar_producto (self,gondola:Gondola ,producto: Producto):
            gondola.productos.append(producto)
            if producto.codigo_barras in gondola.dic:
                 gondola.dic[producto.codigo_barras]+=1
            else:
                 gondola.dic[producto.codigo_barras]=1

            print("producto agregador correctamente")

    def verificar_stock(self, gondola:Gondola, producto:Producto):

        a=gondola.dic[producto.codigo_barras]

        if a == 0:
             print("sin disponibilidad")

             self.reponer_stock(gondola,producto)
             print("intente nuevamente mas tarde")

    
    def reponer_stock(self, gondola:Gondola, producto:Producto):
         codigo= producto.codigo_barras

         cant= self.almacen.realizar_pedido(producto)

         if codigo in self.depo:
                self.depo[codigo]+=cant
         else:
                self.depo[codigo]=cant
            
         print("reserva actualizada")



        
