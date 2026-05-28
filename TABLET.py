
#SU UNICA FUNCION ES PRINTEAR LAS COSAS DE C/ GONDOLA 

from GONDOLA import *


#marca, nombre, stock y precio por unidad (en liq la cant de liquidos)

class Tablet:
    def mostrar_productos_engondola(self, gond:Gondola):
        a = gond.productos
        
        print ("Productos en la gondola: ", gond.tipo)

        for clave, valor in gond.dic.items():
            print ("Producto: ",{clave} )
            print ("Disponibilidad: ", {valor})
            






