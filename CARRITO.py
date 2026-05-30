
#SuperMarket Nati y Aylu :) - Clase Carrito

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PRODUCTO.producto import *
    from gondola import *
    from almacen import Almacen
    from inventario import Inventario
    from pantalla_carrito import *

import os
os.system('cls')


class Carrito:
    
    #Pantalla OLED del carrito: muestra el total acumulado
    #Se comunica con el controlador central (Almacen).
    
    def __init__(self, alm: Almacen, inv: Inventario):
        self.list_prod :list[Producto]=[]                    #me creo lista vacia en donde vamos agregando productos al carrito
        self.total:float = 0                       #precio final de la compra
        self.almacen=alm  
        self.inventario = inv         

     #carrito --> gondola --> llamar inventario y verificar stock 
            #si hay stock, agrega y resta uno a la gondola
            #si no hay e gondola pero si en inv, repone y agrega a gondola
            #si no hay ni en gondola ni en inv, llama a almacen que llama a proveedor   



    #-------------------------Mostrar Productos ------------------------

    def mostrar_productos(self):
        if not self.list_prod:
            print ("No hay productos en el carrito")
            return 

        else:
            for i in self.list_prod:
                i.mostrar_info()  #como i es un producto, puedo usar las funciones del mismo


    #---------------Vaciar Carrito -----------------
    def vaciar(self):
        self.list_prod.clear()
        self.total = 0.0

    #---------------Monitoreo y Reposición en Compra----------------------


    def agregar_a_carrito (self, producto:Producto, gondola:Gondola):
        #agrego al carrito de a uno

        if producto.codigo_barras not in gondola.dic:
            print("Producto no encontrado en la gondola")
            return 

        #bsuco los productos en base al diccionario que creamos en la clase Gondola

        else:
            if gondola.dic[producto.codigo_barras]> 0: #si quiero una cant de productos que no me infiera con el umbral minimo
                
                gondola.decrementar_gondola(producto.codigo_barras)
                self.list_prod.append(producto)   #lo agrego a mi carrito

                #self.almacen.precio_final(producto.codigo_barras, self)       
                self.almacen.precio_final(self) #llamo a la funcion de almacen DE PRECIO FINAL 

            elif gondola.dic[producto.codigo_barras]< 0:
                print("No hay stock disponible. Vuelva a intentarlo mas tarde")
                gondola.reponer_inventario(self.inventario, producto)






   

        

   

        