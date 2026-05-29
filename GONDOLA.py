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
        
        if not self.dic:
            print("No hay productos disponibles.")
            return
 
        for i, (cod, stock) in enumerate(self.dic.items(), start=1):
            prod = self.buscar_producto(cod)
            if prod is None:
                continue
            estado = f"[stock: {stock}]" if stock > 0 else "[sin stock]"
            print(f"  {i}) {prod.nombre} ({prod.marca}) - ${prod.precio:.2f}  {estado}")
    
    def reponer_inventario(self, inv:Inventario ,prodcuto: Producto):
        inv.reponer_stock(self,prodcuto)
    
    def decrementar_gondola(self, cod, cantidad=1):

        if cod in self.dic and self.dic[cod] > 0:
            
            self.dic[cod] -= cantidad
            self.dic[cod] = round(self.dic[cod], 3)
            return True
        return False
    
    def aumentar_gondola(self, cod):
        self.dic[cod]+=1

        






