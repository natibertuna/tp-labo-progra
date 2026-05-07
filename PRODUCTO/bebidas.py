from PRODUCTO.producto import *

class Bebidas (Producto):

    #productos: Sprite, Cunnington, Agua, Manaos, Aquarius

    def __init__(self, nombre, codigo, marca, precio_por_unidad, stock, litros):
        super().__init__(nombre, codigo, marca, precio_por_unidad, stock)
        self.litros = litros
        self.lista= list #ahora que modificamos que en vez de gondolas hay productos, no se si tiene mucho sentido mas que para las promociones

        




