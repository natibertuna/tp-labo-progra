from __future__ import annotations
from typing import TYPE_CHECKING

from PRODUCTO.producto import Producto

if TYPE_CHECKING:
    from INVENTARIO import *

#from INVENTARIO import * #sobra


class Gondola:
    def __init__(self, tipo:str, prod:list, max:int, min:int):
        self.tipo = tipo
        self.productos = prod #lista de productos YA en la gondola
        self.umbral_maximo=max
        self.umbral_min = min

        #dic de productos ---> tiene la cant de productos en gondola
        self.dic=self.diccionario()
    
    def diccionario(self): #relleno el diccionario con el codigo de cada producto y su stock en gondola
        dic = {}
        for i in self.productos:
            if i.codigo_barras in dic.keys():
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
        
        for a in self.productos:
            for b in len(self.productos):
                print(b)  #imprime el nro del producto
                a.mostrar_info()
    
    def reponer_inventario(self, inv:Inventario ,prodcuto: Producto):
        inv.verificar_stock(self,prodcuto)
    
    def decrementar_gondola(self, cod):
        a=self.buscar_producto(cod)

        if a:
            self.dic[cod]-=1 #resto el valor del diccionario
            self.productos.remove(a) #lo elimino de gondola





