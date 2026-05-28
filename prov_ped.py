
from PRODUCTO.producto import *

#creo el objeto pedido 

class Pedido:
    _contador = 0  # id autoincremental
 
    def __init__(self, prod: Producto, cantidad: int):
        Pedido._contador += 1
        self.id_pedido = Pedido._contador
        self.prod = prod
        self.cantidad = cantidad        # FIX: faltaba guardar la cantidad
        self.nombre = prod.nombre       # FIX: faltaba este atributo (usado en Proveedor)
 
    def __str__(self):
        return f"Pedido #{self.id_pedido}: {self.cantidad}x {self.nombre}"
    

class Proveedor:
    def __init__(self, nombre, direccion,tipo, telefono):
        self.nombre=nombre
        self.dire=direccion
        self.tipo=tipo
        self.tel=telefono

    def recibir_pedido(self, pedido: Pedido):
        print(f"  [PROVEEDOR '{self.nombre}'] Pedido recibido: {pedido}")
 
    def confirmar_envio(self, pedido: Pedido) -> int:
        print(f"  [PROVEEDOR '{self.nombre}'] Envío confirmado — "
              f"Pedido #{pedido.id_pedido}: {pedido.cantidad}x {pedido.nombre}")
        return pedido.cantidad
    




    