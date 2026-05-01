from PRODUCTOS.producto import Producto

class Panaderia (Producto):

    #productos: miÑon, figasita,  

    def __init__(self, precio_por_unidad, marca, stock, tipo_pan, bolsones, peso):
        super().__init__(precio_por_unidad, marca, stock)
        self.peso = peso
        self.__pan = tipo_pan
        self.bolsones_depan = bolsones
        self.lista= list


        def agregar_a_lista (self):
            self.lista.append(self) #cada vez que agregan algo al carrito, lo agrego a la lista --> esta funcion debe ir en la clase de carrito

            
            