 #clase padre

from abc import ABC

class Producto(ABC):
    def __init__(self,nombre, codigo, marca,  precio_por_unidad, stock,umbral_min, umbral_max):


        # umbral de stock mínimo de reposición.

        self.prec = precio_por_unidad
        self.nombre = nombre
        self.marca = marca
        self.stock_gondola = stock
        self.codigo_barras= codigo
        self.umbral_min= umbral_min
        self.umbral_max=umbral_max #maxima cant de productos en gondola 

   
    def mostrar_info(self):
        return (
            f"[{self.codigo_barras}] {self.marca} {self.nombre} - "
            f"${self.prec} | Góndola: {self.stock_gondola}"
        )