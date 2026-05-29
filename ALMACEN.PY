from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PRODUCTO import *
    from CARRITO import Carrito
    from prov_ped import *
    from GONDOLA import *

import os
os.system('cls')

#realiza contacto con los proveedores de los productos, el cálculo de las promociones, 
# determinación de precios del producto

class Almacen:

    def __init__(self):
       self.carritos_previos: list[Carrito]=[] #lista que contiene todos los carritos
       self.proveedores :list= []
    

    #-------------------- Determinación de Precios ---------------------------


    def determinar_precio(self, codigo_barra: str, Gondolas:list) -> float | None:

        for gondola in Gondolas:
            for producto in gondola.productos:
                if codigo_barra== producto.codigo_barras:
                    
                    #encontramos el producto y le extraigo su precio
                    
                    precio= producto.precio_final
                    return precio
        return None
                

    #------------------ Cálculo de Promociones-----------------------


    def precio_final (self, producto:Producto, carrito:Carrito):
        #producto = self.hallar_producto(cod_bar,carrito)

        cat=producto.CATEGORIA

        #inicializo los contadores

        cont=0.0
        precio_pasajero=0
        cont_sinpromo=0

        if cat=="Galletitas":

            #HAY QUE GENERALIZAR LO DE LOS PRECIOS

             PROMO_GALLETAS = "2x1"           # 2x1 cualquier marca

             ya_en_carrito=0

             if carrito:

                galles=[]

                for item in carrito.list_prod:

                    ya_en_carrito += 1
                    galles.append(item) #agrego las galletitas a una lista auxiliar 
                    cont+= item.precio #acumulo el precio total

                if ya_en_carrito%2==0:
                    precio_pasajero= cont*(ya_en_carrito/2)
                    print ("Promocion 2x1 aplicada correctamente")
                else: 
                    precio_pasajero= cont*((ya_en_carrito-1)/2)+galles[-1].precio
                    print ("Promocion 2x1 aplicada correctamente")
        
        elif cat=="Perfumeria":
    
            PROMO_PERFUMERIA = 0.50

            ya_en_carrito = 0

            for item in carrito.list_prod:

                if item.CATEGORIA == "Perfumeria":
                    ya_en_carrito += 1
                    cont += item.precio

            precio_pasajero = cont * PROMO_PERFUMERIA

            print("Promocion 50% aplicada Correctamente")

        elif cat=="Bebidas":

            PROMO_BEBIDAS  = 1.7          # 30% descuento segunda unidad misma marca


            #bebidas: 30% en la seg unidad
            #nro par --> (precio + prec*0.3)
            #nro impar --> (precio + prec*0.3)*nro par + precio

            #comparar por marcas
            # Contar unidades de esta MARCA ya en el carrito
            ya_en_carrito = 0

            prod=producto
            
            if carrito:
                for item in carrito.list_prod:

                    if (item.CATEGORIA == "Bebidas" and item.marca == prod.marca):
                        ya_en_carrito += 1


            # Unidades que aplican descuento (un par)

            if ya_en_carrito%2==0:                                                       #si es nro par
                precio_pasajero=producto.precio*(ya_en_carrito/2)*PROMO_BEBIDAS

                print ("Promocion 30% en la segunda unidad aplicada correctamente")

            else: 
                precio_pasajero=producto.precio*((ya_en_carrito-1)/2)*PROMO_BEBIDAS + producto.precio
                print ("Promocion 30% en la segunda unidad aplicada correctamente")

            # Si no hay segunda unidad de la misma marca, sin promo

        else:

            #el precio para las demas categorias de productos

            cont_sinpromo+=producto.precio #importante que este contador NO SE INICIALICE EN 0

        total = cont_sinpromo + precio_pasajero
        carrito.total  += total

        return total


    #---------------------- Generación de Pedidos a un Proveedor externo ---------------------


    def realizar_pedido(self, producto: "Producto",gondola: "Gondola") -> int:

        if not self.proveedores:
            print("  ✗ Almacen: sin proveedores registrados.")
            return 0
        
        # Por ahora se usa el primer proveedor --> aquí se podría filtrar por tipo
        prov = self.proveedores[0]
        pedido = Pedido(producto, gondola.umbral_maximo)
        return self._realizar_pedido(pedido, prov)
        
    def _realizar_pedido(self, ped: "Pedido", prov: "Proveedor") -> int:
        #comunicación concreta con el proveedor (uso interno)
        
        prov.recibir_pedido(ped)
        return prov.confirmar_envio(ped)
 

    def agregar_prov(self, proveedor:Proveedor):
        self.proveedores.append(proveedor)
        print ("Proveedor", proveedor.nombre, "agregado correctamente")









    

        