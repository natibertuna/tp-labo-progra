class Inventario:

    def __init__(self):
        self.gondolas = [] #lista de las gondolas
        self.deposito = self.deposito()

    def agregar_gondola(self, gondola):
        self.gondolas.append(gondola) #al final

    def buscar_producto(self, codigo_barra):
        for a in self.gondolas:
            for b in a.producto:
                if b.codigo_barra == codigo_barra:
                    return a
        return None

    def bajar_disponibilidad(self, producto):
        if producto.disponibilidad>0:
            producto.disponibilidad-=1
        else:
            print(f"En esta gondola no hay: {producto.nombre}")