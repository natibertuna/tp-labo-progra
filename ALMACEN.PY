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

    PROMO_GALLETAS = "2x1"           # 2x1 cualquier marca
    PROMO_BEBIDAS  = 0.30            # 30% descuento segunda unidad misma marca
    PROMO_PERFUMERIA = 0.50          # 50% descuento cualquier producto


    def recorrer_lista(self, lista):
        for i in lista:
            
            
    def precio(self):
        #esta funcion es para det el precio del carrito
        prod= self.carrito.list_prod[]
        self.carrito.total=0 #inicializo en 0 asi no se agrega lo mismo cada vez que agregamos algo al carrito
        lista_bebidas=[]
    
        for i in prod:

            if type(prod[i])== 'Verduleria':
                cont_v+=1
            elif type(prod[i])== 'Lacteos':
                cont_l+=1            
            elif type(prod[i])== 'Higiene':
                cont_h+=1
            elif type(prod[i])== 'Bebidas':
                cont_v+=1
                lista_bebidas.append(i) #me sirve para despues buscar los de la misma marca
            elif type(prod[i])== 'Carniceria':
                cont_c+=1            
            elif type(prod[i])== 'Galletitas':
                cont_g+=1
            elif type(prod[i])== 'Panaderia':
                cont_p+=1

        
            


        #bebidas: 30% en la seg unidad
        #nro par --> (precio + prec*0.3)
        #nro impar --> (precio + prec*0.3)*nro par + precio


        #galletitas : 2x1 cualquier marca
        #nro par --> nro/2*precio
        #nro impar --> nro/2*precio + precio

        #perfumerio: 50% en cualquier unidad
        #(precio*0.5)k



    def realizar_pedido(ped:Pedido, prov:Proveedor): #funcion que va a ser llamada por deposito
        Proveedor.recibir_pedido(prov,ped)
        cant=Proveedor.confirmar_envio(prov, ped)
        return cant
        








    

        