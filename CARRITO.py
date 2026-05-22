
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
    
    #Pantalla OLED del carrito: muestra el total acumulado. --> deberiamos llamar a la clase Pantalla para que printee todo
    #Se comunica con el controlador central (Almacen).
    
    def __init(self, alm:Almacen):
        self.list_prod=[]                    #me creo lista vacia en donde vamos agregando productos al carrito
        self.total: int                       #precio final de la compra
        self.almacen=alm           

     #carrito --> gondola --> llamar inventario y verificar stock 
            #si hay stock, agrega y resta uno a la gondola
            #si no hay e gondola pero si en inv, repone y agrega a gondola
            #si no hay ni en gondola ni en inv, llama a almacen que llama a proveedor   


#---------------Monitoreo y Reposición en Compra----------------------


    def agregar_a_carrito (self, producto:Producto, cantidad, gondola:Gondola):

        if gondola.buscar_producto(producto.codigo_barra) == -1:
            print("Producto no encontrado")

        #bsuco los productos en base al diccionario que creamos en la clase Gondola

        else:
            if gondola.dic['producto.codigo_barras'] - cantidad > producto.umbral_min: #si quiero una cant de productos que no me infiera con el umbral minimo
                gondola.dic['producto.codigo_barras']-=cantidad #resto el valor del diccionario
                gondola.productos[producto].remove() #lo elimino de gondola


                for i in cantidad:
                    self.list_prod[producto].append #lo agrego a mi carrito
                    self.almacen.precio_promo()       #llamo a la funcion de almacen
                    print ("Monto Carrito: ", self.total)
        

            elif gondola.dic['producto.codigo_barras'] - cantidad < producto.umbral_min:
                print("No hay stock disponible. Vuelva a intentarlo mas tarde")
                self.gondola.reponer_inventario()






   

        