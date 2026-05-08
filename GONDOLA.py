from PRODUCTO.producto import Producto

class Gondola:
    def __init__(self, tipo, prod):
        self.tipo = tipo
        self.productos = prod #lista de productos YA en la gondola
        
    #SACAR Y PONER EN INV
    def agregar_producto(self, producto: Producto):
        for p in self.productos:
            if p.codigo_barra == producto.codigo_barra:
                print("El producto ya está en la góndola")
                return
            else:
                self.productos.append(producto)
                print ("Se agrego correctamente a la gondola")

    def eliminar_producto(self,producto, cant):
        
        if producto.stock_gondola - cant > producto.umbral_min:
            producto.stock_gondola -= cant
             #elimino un prducto de la gondola , que esa cantidad estaba en producto
        else:
            
        
    
    def buscar_producto(self, codigo_barra):
        for a in self.productos:
            if a.codigo_barra == codigo_barra:
                return a
            else:
                return -1
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
