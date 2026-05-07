from PRODUCTO.producto import *

class Panaderia (Producto):

    #productos: miÑon, figasita,  

    def __init__(self, nombre, codigo, marca, precio_por_unidad, stock, tipo_pan, bolsones, peso):
        super().__init__(nombre, codigo, marca, precio_por_unidad, stock)
        self.peso = peso
        self.__pan = tipo_pan
        self.bolsones_depan = bolsones
        self.lista= list


        def agregar_a_lista (self):
            self.lista.append(self) #cada vez que agregan algo al carrito, lo agrego a la lista --> esta funcion debe ir en la clase de carrito

            
            