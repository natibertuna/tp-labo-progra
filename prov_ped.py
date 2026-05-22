
from PRODUCTO.producto import *

#creo el objeto pedido 

class Pedido:
    def __init__(self, prod:Producto, cant):
        self.prod=prod

class Proveedor:
    def __init__(self, nombre, direccion,tipo, telefono):
        self.nombre=nombre
        self.dire=direccion
        self.tipo=tipo
        self.tel=telefono

    def recibir_pedido(self, pedido: Pedido):
        print(f"  [PROVEEDOR '{self.nombre}'] Pedido recibido: {pedido}")
 
    def confirmar_envio(self, pedido: Pedido) -> int:
        print(f"  [PROVEEDOR '{self.nombre}'] Envío confirmado para pedido #{pedido.id_pedido} "
              f"({pedido.cantidad} unidades de {pedido.nombre})")
        return pedido.cantidad
    




    