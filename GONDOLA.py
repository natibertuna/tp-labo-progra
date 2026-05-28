from __future__ import annotations
from typing import TYPE_CHECKING

from PRODUCTO.producto import Producto

if TYPE_CHECKING:
    from INVENTARIO import *

import os
os.system('cls')


class Gondola:
    def __init__(self, tipo:str, prod:list, max:int, min:int):
        self.tipo = tipo
        self.productos = prod #lista de productos YA en la gondola
        self.umbral_maximo=max
        self.umbral_min = min

        #dic de productos ---> tiene la cant de productos en gondola
        self.dic=self._llenar_diccionario()
    
    
    #me creo un metodo privado
    def _llenar_diccionario(self)-> dict[str, int]: 
        
        #relleno el diccionario con el codigo de cada producto y su stock en gondola
        dic: dict[str, int] = {}

        for i in self.productos:
            if i.codigo_barras in dic:
                dic[i.codigo_barras] += 1 #me aumenta el value
            else:
                dic[i.codigo_barras] = 1 #me crea la llave 

        return dic
    
    def buscar_producto(self, codigo_barras:str):

        for a in self.productos:
            if a.codigo_barras == codigo_barras:
                return a
        return None

    def mostrar_productos(self):
        print(f"Góndola: {self.tipo}")

        if not self.productos:
            print("No hay productos disponible.")
            return
        
        vistos: dict[str, Producto] = {} #evito imprimir repetidos

        for p in self.productos:
            if p.codigo_barras not in vistos:
                vistos[p.codigo_barras] = p
 
        for i, p in enumerate(vistos.values(), start=1):
            stock = self.dic.get(p.codigo_barras, 0)
            print(f"  {i}) {p.nombre} ({p.marca}) - ${p.precio:.2f}  "
                  f"[stock: {stock}]")
    
    def reponer_inventario(self, inv:Inventario ,prodcuto: Producto):
        inv.verificar_stock(self,prodcuto)
    
    def decrementar_gondola(self, cod):
        prod=self.buscar_producto(cod)

        if prod and self.dic.get(cod, 0) > 0:
            self.dic[cod] -= 1
            self.productos.remove(prod)
            return True
        
        return False





