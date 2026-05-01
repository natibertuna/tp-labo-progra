from PRODUCTOS.producto import Producto

class Bebidas (Producto):

    #productos: Sprite, Cunnington, Agua, Manaos, Aquarius

    def __init__(self, precio_por_unidad, marca, stock, litros):
        super().__init__(precio_por_unidad, marca, stock)
        self.litros = litros
        self.lista= list




