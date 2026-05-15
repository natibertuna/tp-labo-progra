
#SuperMarket Nati y Aylu :) - Clase Carrito

from __future__ import annotations
from typing import TYPE_CHECKING

import ALMACEN

if TYPE_CHECKING:
    from PRODUCTO.producto import *
    from GONDOLA import *
    from DEPOSITO import *
    from ALMACEN import *


class Carrito:
    
    #Pantalla OLED del carrito: muestra el total acumulado.
    #Se comunica con el controlador central (Almacen).
    
    def __init(self, gond:Gondola):
        self.list_prod=[]                    #me creo lista vacia en donde vamos agregando productos al carrito
        self.total: int                       #precio final de la compra
        self.gondola=gond
        self.almacen:Almacen           

     #carrito --> gondola --> llamar inventario y verificar stock 
            #si hay stock, agrega y resta uno a la gondola
            #si no hay e gondola pero si en inv, repone y agrega a gondola
            #si no hay ni en gondola ni en inv, llama a almacen que llama a proveedor   


#---------------Monitoreo y Reposición en Compra----------------------


    def agregar_a_carrito (self, producto:Producto, cantidad):
        if Gondola.buscar_producto(producto.codigo_barra) == -1:
            print("Producto no encontrado")
        else:
            if producto.stock_gondola - cantidad > producto.umbral_min: #si quiero una cant de productos que no me infiera con el umbral minimo
                producto.stock_gondola-=cantidad 
                for i in cantidad:
                    self.list_prod[producto].append #lo agrego a mi carrito
                    self.almacen.precio_promo
                    print ("Monto Carrito: ", self.total)
        
            elif producto.stock_gondola - cantidad < producto.umbral_min:
                print("No hay stock disponible. Vuelva a intentarlo mas tarde")
                self.gondola.reponer_inventario()






   

        