
#SU UNICA FUNCION ES PRINTEAR LAS COSAS DE C/ GONDOLA 

from GONDOLA import *
import os
os.system('cls')


#marca, nombre, stock y precio por unidad (en liq la cant de liquidos)

class Tablet:
    def mostrar_productos_engondola(self, gond:Gondola):
        a = gond.productos
        
        print(f"\n  Productos en la góndola: {gond.tipo}")
        print(f"  {'─'*40}")
 
        if not gond.dic:
            print("  (vacía)")
            return
        
        por_codigo: dict = {}

        for prod in gond.productos:
            if prod.codigo_barras not in por_codigo: #me creo un diccionario y agrego el producto
                por_codigo[prod.codigo_barras] = prod
 
        for cod, cantidad in gond.dic.items(): #itero dentro del diccionario
            
            prod = por_codigo.get(cod)
            nombre = prod.nombre if prod else cod
            marca  = prod.marca  if prod else "—"
            print(f"  · {nombre} ({marca})  —  stock: {cantidad}")






