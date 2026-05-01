from PRODUCTOS.producto import Producto

class Gondola:
    def __init__(self, tipo):
        self.tipo = tipo
        self.productos = []

    def agregar_producto(self, producto: Producto):
        for p in self.productos:
            if p.codigo_barra == producto.codigo_barra:
                print("El producto ya está en la góndola")
                return
        self.productos.append(producto)

    def eliminar_producto(self, codigo_barra):
        for a in self.productos:
            if a.codigo_barra == codigo_barra:
                self.productos.remove(a)
                print("Producto eliminado")
                return
        print("Producto no encontrado")
    
    def buscar_producto(self, codigo_barra):
        for a in self.productos:
            if a.codigo_barra == codigo_barra:
                return a
        return None

    def mostrar_productos(self):
        print(f"Góndola: {self.tipo}")

        if not self.productos:
            print("No disponible.")
            return
        
        for a in self.productos:
            print(a)

        

    
    #def mostrar_productos(self):
       # print(f"Gondola: {self.tipo}")
       # for a in self.productos:
          #  print(f"{a.marca} {a.nombre} - ${a.precio} - Disp: {a.disponibilidad}")
