from PRODUCTO import *
from CARRITO import *
from prov_ped import *

#realiza contacto con los proveedores de los productos, el cálculo de las promociones, 
# determinación de precios del producto

class Almacen:

    def __init__(self):
       pass

    
    #def precio(self):
        
            

    def realizar_pedido(ped:Pedido, prov:Proveedor): #funcion que va a ser llamada por deposito
        Proveedor.recibir_pedido(prov,ped)
        cant=Proveedor.confirmar_envio(prov, ped)
        return cant
        








    

        