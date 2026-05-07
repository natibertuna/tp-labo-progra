
#SuperMarket Nati y Aylu :) - Clase Almacén (Controlador Centralizado)

from PRODUCTO.producto import *


class Carrito:
    PROMO_GALLETAS = "2x1"           # 2x1 cualquier marca
    PROMO_BEBIDAS  = 0.30            # 30% descuento segunda unidad misma marca
    PROMO_PERFUMERIA = 0.50          # 50% descuento cualquier producto
    
    
    def __init(self):
        