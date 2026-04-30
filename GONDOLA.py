from PRODUCTOS.producto import Producto

class Gondola:
    def __init__(self, tipo):
        self.tipo = tipo
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        print(f"Gondola: {self.tipo}")
        for a in self.productos:
            print(f"{a.marca} {a.nombre} - ${a.precio} - Disp: {a.disponibilidad}")
