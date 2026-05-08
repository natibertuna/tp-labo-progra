
from DEPOSITO import *

class Inventario:
    def __init__(self, deposito:Deposito):
        self.deposito = deposito
    
    #def stock()
        
    #Debe interactuar con los métodos que decrementan el stock (ej., al agregar un producto al carrito
    # de compras) para verificar si la cantidad disponible se encuentra por debajo del umbral mínimo de
    # reposición.

    def agregar_producto(self, producto: Producto):
        for p in self.productos:
            if p.codigo_barra == producto.codigo_barra:
                print("El producto ya está en la góndola")
                return
            else:
                self.productos.append(producto)
                print ("Se agrego correctamente a la gondola")

    def verificar_stock(self):
        self.deposito.agregar_stock()




