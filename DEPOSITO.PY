"""""
from GONDOLA import * 
from ALMACEN import *

class Deposito:
    def __init__(self,  gondola:Gondola, cantidad, al:Almacen):
        self.cant = cantidad #cantidad de cada producto en deposito --> cantidad universal;
        self.tipo = gondola
        self.almacen=al


    def agregar_stock(self, prod:Producto):
        
        if self.cant==0:
            #llama a almacen que llama a proveedor 

            self.cant=self.almacen.realizar_pedido(prod) #ERROR

            pass #nuestra intencion es que despues de actualizarse, entre a los otros ifs
        
        if self.tipo.dic[prod.codigo_barras]+self.cant < self.tipo.umbral_max:   #accedo al value

            self.tipo.dic[prod.codigo_barras]=self.cant

            self.cant=0

        elif self.tipo.dic[prod.codigo_barras]+self.cant > self.tipo.umbral_max: 
            resto=(self.tipo.dic[prod.codigo_barras]+self.cant)- self.tipo.umbral_max
            self.tipo.dic[prod.codigo_barras]= (self.cant-resto)
            self.cant=resto
"""""