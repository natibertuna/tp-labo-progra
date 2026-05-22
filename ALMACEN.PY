from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PRODUCTO import *
    from CARRITO import *
    from prov_ped import *

#realiza contacto con los proveedores de los productos, el cálculo de las promociones, 
# determinación de precios del producto

class Almacen:

    def __init__(self, car:Carrito):
       self.carrito=car
       self.carritos_previos=[] #lista que contiene todos los carritos
    

    def hallar_producto(self, cod):
        p = self.carrito.list_prod

        for i in p:
            if i.codigo_barras==cod: #encontramos el producto 
                prod=i 
                #me devuelve el producto 
                return prod
            else:
                return False #producto no encontrado


    #-------------------- Determinación de Precios ---------------------------


    def determinar_precio(self, codigo_barra: str) -> float | None:
        p = self.carrito.list_prod

        for i in p:
            if i.codigo_barras==codigo_barra: #encontramos el producto y le extraigo su precio
                precio=i.precio_final
                return precio
            else:
                print ("Producto No Encontrado")
                return None 
                #si no encuentra el producto en el carrito, no devuelve nada
                

    #------------------ Cálculo de Promociones-----------------------


    def precio_promo (self, cod_bar):
        producto = self.hallar_producto(cod_bar)

        cat=producto.CATEGORIA

        if cat=="Galletitas":

            #HAY QUE GENERALIZAR LO DE LOS PRECIOS

             PROMO_GALLETAS = "2x1"           # 2x1 cualquier marca

             ya_en_carrito=0
                # rever


            #PREGUNTAR SI ESTA BIEN ENTENDIDA  

             if self.carrito:
                cont=0
                galles=[]
                for item in self.carrito.list_prod:
                    if (item.CATEGORIA == "Galletitas"):
                        ya_en_carrito += 1
                        galles.append(item) #agrego las galletitas a una lista auxiliar 
                        cont+= self.carrito.list_prod.prec[item] #acumulo el precio total


                if ya_en_carrito%2==0:
                    self.carrito.total=cont*(ya_en_carrito/2)
                    print ("Promocion aplicada correctamente")
                else: 
                    self.carrito.total=cont*((ya_en_carrito-1)/2) + galles[-1].precio
                    print ("Promocion aplicada correctamente")

        
        elif cat=="Higiene":

            PROMO_PERFUMERIA = 0.50          # 50% descuento cualquier producto

            ya_en_carrito=0

            if self.carrito:
                for item in self.carrito.items:
                    if (item.CATEGORIA == "Higiene"):
                        ya_en_carrito += 1

            self.carrito.total=self.determinar_precio(cod_bar)*ya_en_carrito*PROMO_PERFUMERIA

            print ("Promocion aplicada Correctamente")

        elif cat=="Bebidas":

            PROMO_BEBIDAS  = 1.7            # 30% descuento segunda unidad misma marca


            #bebidas: 30% en la seg unidad
            #nro par --> (precio + prec*0.3)
            #nro impar --> (precio + prec*0.3)*nro par + precio


            #comparar por marcas
            # Contar unidades de esta MARCA ya en el carrito
            ya_en_carrito = 0

            prod=self.hallar_producto(cod_bar)
            
            if self.carrito:
                for item in self.carrito.items:
                    if (item.CATEGORIA == "Bebidas" and item.marca == prod.marca):
                        ya_en_carrito += 1


            # Unidades que aplican descuento (un par)

            if ya_en_carrito%2==0:                                                       #si es nro par
                self.carrito.total=producto.precio*(ya_en_carrito/2)*PROMO_BEBIDAS

                print ("Promocion aplicada correctamente")
            else: 
                self.carrito.total=producto.precio*((ya_en_carrito-1)/2)*PROMO_BEBIDAS + producto.precio

            # Si no hay segunda unidad de la misma marca, sin promo


        #bebidas: 30% en la seg unidad


    #---------------------- Generación de Pedidos a un Proveedor externo ---------------------


    def realizar_pedido(ped:Pedido, prov:Proveedor): #funcion que va a ser llamada por deposito
        Proveedor.recibir_pedido(prov,ped)
        cant=Proveedor.confirmar_envio(prov, ped)
        return cant
        








    

        