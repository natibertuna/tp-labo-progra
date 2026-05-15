from PRODUCTO import producto

from PRODUCTO.panaderia import *
from PRODUCTO.bebidas import *
from PRODUCTO.carniceria import *
from PRODUCTO.galletitas import *
from PRODUCTO.verduleria import *

import os
os.system('cls')



#me creo 3 productos de cada gondola

# ----------------------------- VERDULERIA -----------------------
p1 = Verduleria("Zanahoria", "VERD001", "Huerta Orgánica", 1200.00, 50, 10, 100, 1.5)
p2 = Verduleria("Cebolla", "VERD002", "Don Juan", 950.00, 80, 15, 150, 2.0)
p3 = Verduleria("Lechuga", "VERD003", "Fattoria", 1800.00, 25, 5, 40, 0.6)

p3.mostrar_info()

# ----------------------------- BEBIDAS----------------------------
p4 = Bebidas("Sprite", "BEB001", "The Coca-Cola Co.", 2500.00, 40, 10, 80, 2.25)
p5 = Bebidas("Cunnington Tónica", "BEB002", "Cunnington", 1800.00, 30, 8, 60, 1.5)
p6 = Bebidas("Agua Mineral", "BEB003", "Kin", 1200.00, 100, 20, 200, 2.0)
p7 = Bebidas("Manaos Cola", "BEB004", "Manaos", 1400.00, 60, 15, 120, 2.25)
p8 = Bebidas("Aquarius Pera", "BEB005", "Aquarius", 2100.00, 35, 10, 70, 1.5)


#---------------------------- CARNICERIA --------------------------

p9 = Carniceria("Vacío", "CARN001", "Estancia Sur", 8500.00, 15, 5, 30, "Corte Entero", 2.5)
p10 = Carniceria("Asado", "CARN002", "Don Pedro", 7900.00, 20, 8, 40, "Tira de Asado", 3.0)
p11 = Carniceria("Costillitas de Cerdo", "CARN003", "Granja Sol", 6200.00, 12, 4, 25, "Cerdo", 1.8)



#----------------------- GALLETITAS ------------------------------
p12 = Galletitas("Toddy", "GALL001", "PepsiCo", 1800.00, 45, 10, 100)
p13 = Galletitas("Oreo Golden", "GALL002", "Mondelez", 1650.00, 30, 8, 80)
p14 = Galletitas("Vainillas", "GALL003", "Valente", 2100.00, 20, 5, 50)
p15 = Galletitas("Pitusas", "GALL004", "Parripan", 950.00, 60, 15, 120)
p16 = Galletitas("Sonrisas", "GALL005", "Bagley", 1300.00, 40, 10, 90)
p17 = Galletitas("Porteñitas", "GALL006", "Bagley", 1100.00, 35, 8, 80)













rta=input("Desea agregar productos a su carrito? (si/no): ")

#if rta=="si":
    #llama a carrito



