
#SuperMarket Nati y Aylu :) - Clase Carrito

from PRODUCTO.producto import *
from GONDOLA import *
from DEPOSITO import *





class Carrito:
    PROMO_GALLETAS = "2x1"           # 2x1 cualquier marca
    PROMO_BEBIDAS  = 0.30            # 30% descuento segunda unidad misma marca
    PROMO_PERFUMERIA = 0.50          # 50% descuento cualquier producto
    
    #Pantalla OLED del carrito: muestra el total acumulado.
    #Se comunica con el controlador central (Almacen).
    
    def __init(self):
        self.list_prod=[] #me creo lista vacia en donde vamos agregando productos al carrito
        self.total #precio final de la compra

     #carrito --> gondola --> llamar inventario y verificar stock 
            #si hay stock, agrega y resta uno a la gondola
            #si no hay e gondola pero si en inv, repone y agrega a gondola
            #si no hay ni en gondola ni en inv, llama a almacen que llama a proveedor    
    
    def agregar_a_carrito (self, producto:Producto, cantidad):
        if Gondola.buscar_producto(producto.codigo_barra) == -1:
            print("Producto no encontrado")
        else:
            if producto.stock_gondola - cantidad > producto.umbral_min: #si quiero una cant de productos que no me infiera con el umbral minimo
                for i in cantidad:
                    self.list_prod[producto].append #lo agrego a mi carrito

                    self.total+=cantidad*
            elif producto.stock_gondola - cantidad < producto.umbral_min:
                print("No hay stock disponible. Vuelva a intentarlo mas tarde")

                #debo llamar a deposito
                Deposito.agregar_stock() 




   

        