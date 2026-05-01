class Producto:
    def __init__(self,nombre, precio, marca, disponibilidad,codigo_barra):
        self.precio = precio
        self.marca = marca
        self.disponibilidad = disponibilidad
        self.codigo_barra = codigo_barra
        self.nombre = nombre  #ver luego que atributos ponemos como privados

        #clase padre

    def __str__(self):
        return f"{self.marca} {self.nombre} - ${self.precio} - Disp: {self.disponibilidad}"
    