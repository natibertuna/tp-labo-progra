
#SuperMarket Nati y Aylu :) - Clase Carrito

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PRODUCTO.producto import *
    from GONDOLA import *
    from DEPOSITO import *
    from ALMACEN import *
    from INVENTARIO import *


class Carrito:
    
    #Pantalla OLED del carrito: muestra el total acumulado. --> deberiamos llamar a la clase Pantalla para que printee todo
    #Se comunica con el controlador central (Almacen).
    
    def __init__(self, alm: "Almacen", inv: Inventario):
        self.list_prod=[]                    #me creo lista vacia en donde vamos agregando productos al carrito
        self.total: 0                       #precio final de la compra
        self.almacen=alm  
        self.inventario = inv         

     #carrito --> gondola --> llamar inventario y verificar stock 
            #si hay stock, agrega y resta uno a la gondola
            #si no hay e gondola pero si en inv, repone y agrega a gondola
            #si no hay ni en gondola ni en inv, llama a almacen que llama a proveedor   


#---------------Monitoreo y Reposición en Compra----------------------


    def agregar_a_carrito (self, producto:Producto, gondola:Gondola):
        #agrego al carrito de a uno

        if gondola.buscar_producto(producto.codigo_barra) == None:
            print("Producto no encontrado")

        #bsuco los productos en base al diccionario que creamos en la clase Gondola

        else:
            if gondola.dic[producto.codigo_barras] - 1 >= 0: #si quiero una cant de productos que no me infiera con el umbral minimo
                gondola.decrementar_gondola(producto.codigo_barras)

                self.list_prod.append(producto)   #lo agrego a mi carrito
                self.almacen.precio_final(producto.codigo_barras, self)       #llamo a la funcion de almacen DE PRECIO FINAL 
        

            elif gondola.dic[producto.codigo_barras] - 1 < 0:
                print("No hay stock disponible. Vuelva a intentarlo mas tarde")
                gondola.reponer_inventario(self.inventario, producto)






   

        