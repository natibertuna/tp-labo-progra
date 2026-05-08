from PRODUCTO.producto import * 
from ALMACEN import *

class Deposito:
    def __init__(self,  producto:Producto, cantidad):
        self.cant = cantidad #cantidad de ese producto en deposito
        self.tipo = producto

    #NO VA, PERO POR LAS DUDAS LO DEJAMOS
    #def obtener_stock(self, codigo_barra): #codigo de barras es único
     #   return self.disponibilidad.get(codigo_barra,0) #get: si no encuentra el codigo devuelve 0
    

    def agregar_stock(self):
        
        if self.cant==0:
            #llama a almacen que llama a proveedor 
            self.cant=Almacen.realizar_pedido()
            pass #nuestra intencion es que despues de actualizarse, entre a los otros ifs
        
        if self.tipo.stock_gondola+self.cant < self.tipo.umbral_max:
            self.tipo.stock_gondola+=self.cant
            self.cant=0

        elif self.tipo.stock_gondola+self.cant > self.tipo.umbral_max:
            resto=(self.tipo.stock_gondola+self.cant)- self.tipo.umbral_max
            self.tipo.stock_gondola+= (self.cant-resto)
            self.cant=resto
    