from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PRODUCTO import *
    from carrito import Carrito
    from gondola import *

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


    def precio_final (self, carrito:Carrito):
        #producto = self.hallar_producto(cod_bar,carrito)
        galles:list[Producto] = []

        bebidas:list[Producto] = []
       
        coca:list = []
        manaos:list[int] = []
        villavicencio:list = []
        cunnington:list = []
        

        lista_c=carrito.list_prod

        #inicializo los contadores

        precio_pasajero=0
        precio_pas2:int=0
        precio_pasajero3=0
        cont_sinpromo:float=0.0

        ya_en_carrito=0


        cc1=0
        cc2=0
        cc3=0
        cc4=0

        cont2=0
        contflotante=0

        for item in lista_c:
            if item.CATEGORIA=="Galletitas":

            #HAY QUE GENERALIZAR LO DE LOS PRECIOS

                PROMO_GALLETAS = "2x1"           # 2x1 cualquier marca

                ya_en_carrito += 1
                cont=0
                galles.append(item) #agrego las galletitas a una lista auxiliar 
                    
                if ya_en_carrito%2==0:
                    for i in range(0,(ya_en_carrito-1),2):
                        
                        cont+= max(galles[i].calcular_precio_final(), galles[i+1].calcular_precio_final())
                else:
                    for i in range(0,(ya_en_carrito-2),2):
                        
                        cont+= max(galles[i].calcular_precio_final(), galles[i+1].calcular_precio_final())
                    cont+=galles[-1].calcular_precio_final()

                precio_pasajero= cont
        
            elif item.CATEGORIA=="Perfumeria":
    
                PROMO_PERFUMERIA = 0.50

                ya_en_carrito +=1
                cont2 += item.calcular_precio_final()

                precio_pas2 = cont2 * PROMO_PERFUMERIA
            elif item.CATEGORIA=="Carniceria" or item.CATEGORIA=="Verduleria":
                
                contflotante+=item.calcular_precio_final()

            elif item.CATEGORIA =="Bebidas":

                PROMO_BEBIDAS  = 1.7          # 30% descuento segunda unidad misma marca

                cont4=0
                cont5=0
                cont6=0
                cont7=0
                #bebidas: 30% en la seg unidad
                #nro par --> (precio + prec*0.3)
                #nro impar --> (precio + prec*0.3)*nro par + precio

                bebidas.append(item)

                if item.marca=="Coca-Cola":
                    coca.append(item.calcular_precio_final())
                    cc1+=1
                elif item.marca=="Manaos":
                    manaos.append(item.calcular_precio_final())
                    cc2+=1
                elif item.marca=="Cunnington":
                    cunnington.append(item.calcular_precio_final())
                    cc3+=1
                elif item.marca=="Villavicencio":
                    villavicencio.append(item.calcular_precio_final())
                    cc4+=1

                if cc1!=0:
                    if cc1%2==0:
                        for item5 in range(0, len(coca)-1, 2):
                            cont4+=coca[item5]+ coca[item5+1]*0.7
                    else:
                        for item5 in range(0, len(coca)-2, 2):
                            cont4+=coca[item5]+ coca[item5+1]*0.7
                        cont4+=coca[-1]
                
                if cc2!=0:

                    if cc2%2==0:
                        for item6 in range(0, len(manaos)-1, 2):
                            cont5+=manaos[item6]+manaos[item6+1]*0.7
                    else:
                        for item6 in range(0, len(manaos)-2, 2):
                            cont5+=manaos[item6]+manaos[item6+1]*0.7
                        cont5+=manaos[len(manaos)-1]

                if cc3!=0:

                    if cc3%2==0:
                        for item7 in range(0, len(cunnington)-1, 2):
                            cont6+=cunnington[item7]+cunnington[item7+1]*0.7
                    else:
                        for item7 in range(0, len(cunnington)-2, 2):
                            cont6+=cunnington[item7]+cunnington[item7+1]*0.7
                        cont6+=cunnington[-1]

                if cc4!=0:

                    if cc4%2==0:
                        for item8 in range(0, len(villavicencio)-1, 2):
                            cont7+=villavicencio[item8]+villavicencio[item8+1]*0.7
                    else:
                        for item8 in range(0, len(villavicencio)-2, 2):
                            cont7+=villavicencio[item8]+villavicencio[item8+1]*0.7
                        cont7+=villavicencio[-1]

                precio_pasajero3=cont4 + cont5 + cont6+ cont7


            else:

                #el precio para las demas categorias de productos

                cont_sinpromo+=item.calcular_precio_final() #importante que este contador NO SE INICIALICE EN 0

        total = cont_sinpromo + precio_pasajero + precio_pasajero3+precio_pas2+contflotante
        carrito.total=total


    #---------------------- Generación de Pedidos a un Proveedor externo ---------------------


    def realizar_pedido(self, producto: Producto,gondola: Gondola) -> int:

        if not self.proveedores:
            print("  ✗ Almacen: sin proveedores registrados.")
            return 0
        from prov_ped import Proveedor
        from prov_ped import Pedido
        
        # Por ahora se usa el primer proveedor --> aquí se podría filtrar por tipo
        prov = self.proveedores[0]
        cantidad1= 100
        pedido1 = Pedido(producto, cantidad1)
        return self._realizar_pedido(pedido1, prov)
    
    from prov_ped import Proveedor
    from prov_ped import Pedido
        
    def _realizar_pedido(self, ped: Pedido, prov: Proveedor) -> int:
        #comunicación concreta con el proveedor (uso interno)
        
        prov.recibir_pedido(ped)
        return prov.confirmar_envio(ped)
 

    def agregar_prov(self, proveedor:Proveedor):
        self.proveedores.append(proveedor)
        print ("Proveedor", proveedor.nombre, "agregado correctamente")









    

        