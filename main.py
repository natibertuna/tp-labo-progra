from PRODUCTO import producto

from PRODUCTO.producto import panaderia
from PRODUCTO.producto import bebidas
from PRODUCTO.producto import carniceria
from PRODUCTO.producto import verduleria
from PRODUCTO.producto import galletitas

import os
os.system('cls')



#me creo 3 productos de cada gondola

#--- VERDULERIA ---
zanahoria=verduleria("zanahoria","001", "larga", 1000, 15, 0.35)
morron= verduleria("morron","002", "rojo", 2500, 15, 2)
lechuga= verduleria("lechuga","003", "morada", 4000, 12, 0.5)

#--- BEBIDAS---
#self, nombre, codigo, marca, precio_por_unidad, stock, litros):
coca= bebidas("coca", "004", "Coca-Cola", 2500, 16, 1.5)
sprite = bebidas("sprite", "005","Sprite", 1500, 14, 1.5 )
manaos= bebidas("manaos", "006", "Manaos", 1000, 10, 2 )








rta=input("Desea agregar productos a su carrito? (si/no): ")

#if rta=="si":
    #llama a carrito



