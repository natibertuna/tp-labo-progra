from GONDOLA import Gondola

class Inventario:

    def __init__(self):
        self.gondolas = [] #lista de las gondolas
        self.deposito = []

    def agregar_gondola(self, gondola):
        self.gondolas.append(gondola) #al final

    def buscar_producto(self, codigo_barra):
        for a in self.gondolas:
            for b in a.producto:
                if b.codigo_barra == codigo_barra:
                    return b
        return None

    def bajar_disponibilidad(self, codigo_barra):
        producto = self.buscar_producto(codigo_barra)
        if producto:
            if producto.disponibilidad>0:
                producto.disponibilidad-=1
            else:
                print(f"En esta gondola no hay: {producto.nombre}")
