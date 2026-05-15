from PRODUCTO.producto import Producto
from INVENTARIO import *


class Gondola:
    def __init__(self, tipo:str, prod, max ):
        self.tipo = tipo
        self.productos = prod #lista de productos YA en la gondola
        self.dic=self.diccionario()
        self.umbral_maximo=max

        #dic de productos ---> tiene la cant de productos en gondola
        
    
    def diccionario(self): #relleno el diccionario con el codigo de cada producto y su stock en gondola
        dic = {}
        for i in self.productos:
            if i.codigo_barras in dic.keys():
                dic['i.codigo_barras'] += 1 #me aumenta el value
            else:
                dic['i.codigo_barras'] = 1 #me crea la llave 

        return dic
    
    def buscar_producto(self, codigo_barra):
        for a in self.productos:
            if a.codigo_barra == codigo_barra:
                return a
            else:
                return -1
        return None

    def mostrar_productos(self):
        print(f"Góndola: {self.tipo}")

        if not self.productos:
            print("No disponible.")
            return
        
        for a in self.productos:
            print(a)
    
    def reponer_inventario(self, inv:Inventario):
        inv.verificar_stock()



