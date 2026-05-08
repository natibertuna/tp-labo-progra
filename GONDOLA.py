from PRODUCTO.producto import Producto
from INVENTARIO import *


class Gondola:
    def __init__(self, tipo, prod, inv:Inventario):
        self.tipo = tipo
        self.productos = prod #lista de productos YA en la gondola
        self.inv=inv
        
    
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
    
    def reponer_inventario(self):
        self.inv.verificar_stock()



