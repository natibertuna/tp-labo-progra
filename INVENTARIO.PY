from __future__ import annotations
from typing import TYPE_CHECKING

#evito bucles

if TYPE_CHECKING:
    from ALMACEN import Almacen
    from GONDOLA import Gondola
    from PRODUCTO.producto import Producto


import os
os.system('cls')

class Inventario:
    def __init__(self, gondolas: list[Gondola], almacen: Almacen):

        self.gondolas= gondolas
        self.almacen= almacen
        self.depo: dict[str, int] = {}   # stock de reserva por código
    
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

            print(f" '{producto.nombre}' agregado a la góndola {gondola.tipo}.")

    def verificar_stock(self, gondola:Gondola, producto:Producto):

        a=gondola.dic.get(producto.codigo_barras, 0)

        if a == 0:
             print("Sin disponibilidad")
             self.reponer_stock(gondola,producto)
             print("Intente nuevamente mas tarde")
        elif a > 0:
            return

    
    def reponer_stock(self, gondola:Gondola, producto:Producto):  #reemplaza a DEPOSITO
         
         # Repone la góndola desde la reserva
         # Si la reserva está vacía, delega el pedido a Almacen y luego repone
         
         codigo= producto.codigo_barras  #extraigo el codigo de barras
         en_reserva = self.depo.get(codigo, 0) #me creo la reserva de los productos, asi elimino la clase deposito
 
         cantidad_recibida=0

         if en_reserva==0: #significa que no hay stock en depo
             print(f"  ⚠ Reserva vacía para '{producto.nombre}. \n Solicitando reabastecimiento a Almacen…")
             cantidad_recibida = self.almacen.realizar_pedido(producto, gondola)
         
         if cantidad_recibida == 0:
                print("  ✗ No se pudo reabastecer. Intente más tarde.")
                return
         
         self.depo[codigo] = self.depo.get(codigo, 0) + cantidad_recibida
    
         
         # mover unidades de reserva a la góndola hasta llenar el umbral

         a_reponer = min(self.depo[codigo], gondola.umbral_maximo)
         for _ in range(a_reponer):
            self.agregar_producto(gondola, producto)

         self.depo[codigo] -= a_reponer
 
         print("Gondola actualizada")



        
