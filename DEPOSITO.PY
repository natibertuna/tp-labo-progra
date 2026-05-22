from GONDOLA import * 
from ALMACEN import *

class Deposito:
    def __init__(self,  gondola:Gondola, cantidad, al:Almacen):
        self.cant = cantidad #cantidad de cada producto en deposito --> cantidad universa;
        self.tipo = gondola
        self.almacen=al


    def agregar_stock(self):
        
        if self.cant==0:
            #llama a almacen que llama a proveedor 

            self.cant=self.almacen.realizar_pedido() #ERROR

            pass #nuestra intencion es que despues de actualizarse, entre a los otros ifs
        
        if self.tipo.stock_gondola+self.cant < self.tipo.umbral_max:

            self.tipo.dic
            
            self.cant=0

        elif self.tipo.stock_gondola+self.cant > self.tipo.umbral_max: 
            resto=(self.tipo.stock_gondola+self.cant)- self.tipo.umbral_max
            self.tipo.stock_gondola+= (self.cant-resto)
            self.cant=resto
    