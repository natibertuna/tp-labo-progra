 #clase padre

from abc import ABC

class Producto(ABC):
    def __init__(self,nombre, codigo, marca,  precio_por_unidad, ):

        self.precio = precio_por_unidad
        self.precio_final=0
        self.CATEGORIA:str
        self.nombre = nombre
        self.marca = marca
        self.codigo_barras= codigo

   
    def mostrar_info(self):
        print(
            f"[{self.codigo_barras}] {self.marca} {self.nombre} - "
            f"${self.prec} | Góndola: {self.CATEGORIA}"
        )
    
    def crear_producto(self):

        #
