from __future__ import annotations
from typing import TYPE_CHECKING

#evito bucles

if TYPE_CHECKING:
    from almacen import Almacen
    from gondola import Gondola
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

            #print(f" '{producto.nombre}' agregado a la góndola {gondola.tipo}.")

    def verificar_stock(self, gondola: Gondola, producto: Producto) -> bool:
        # SOLO VERIFICA
        
        stock_en_gondola = gondola.dic.get(producto.codigo_barras, 0)
        return stock_en_gondola > 0

    
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
  
         
         es_venta_por_peso = gondola.tipo in ["Carniceria", "Carnicería", "Verduleria", "Verdulería"]

         # Calculamos cuánto falta para llegar al umbral máximo
         stock_actual = gondola.dic.get(codigo, 0)
         espacio_libre = gondola.umbral_maximo - stock_actual

         if espacio_libre <= 0:
          print(f"  La góndola de '{producto.nombre}' ya está llena.")
          return

         # Lo máximo que podemos pasar es lo que hay en reserva o el espacio libre
         a_reponer = min(self.depo[codigo], espacio_libre)

         if es_venta_por_peso:
            gondola.dic[codigo] = stock_actual + a_reponer
            # Si mantienes la lista de objetos físicos, añadimos solo una instancia de referencia si no existía
            if producto not in gondola.productos:
                gondola.productos.append(producto)
         else:
            # Para productos unitarios (enteros), usamos int() por seguridad y el bucle tradicional
            a_reponer_unidades = int(a_reponer)
            for _ in range(a_reponer_unidades):
                self.agregar_producto(gondola, producto)

        # Restamos de la reserva lo que movimos a la góndola
         self.depo[codigo] -= a_reponer
 
         print(f"  ✓ Góndola de '{producto.nombre}' actualizada con éxito.")

    def devolver_producto(self, lista_productos:list[Producto]):
         for i in lista_productos:
              for j in self.gondolas:
                   if i.CATEGORIA==j.tipo:
                        self.agregar_producto(j,i)
         


        


        
