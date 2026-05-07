 #clase padre

class Producto:
    def __init__(self,nombre, codigo, marca,  precio_por_unidad, stock):
        self.prec = precio_por_unidad
        self.nombre = nombre
        self.marca = marca
        self.stock_gondola = stock
        self.codigo_barras= codigo

       
        def reducir_stock(self, cantidad=1):
        
            #Decrementa el stock cuando un cliente agrega un producto al carrito.
            #funcion que va a ser llamada por el carrito
        
            if self.stock_gondola >= cantidad: 
                self.stock_gondola -= cantidad
                return True
            return False

    def incrementar_stock(self, cantidad):
        
        #Incrementa el stock tras una reposición exitosa.
        #funcion para la reposicion o para cuando se elimina algo del carrito
        
        self.stock_gondola += cantidad

   
    def mostrar_info(self):
        return (
            f"[{self.codigo_barras}] {self.marca} {self.nombre} - "
            f"${self.prec} | Góndola: {self.stock_gondola}"
        )