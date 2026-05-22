#--------------------------- IMPORTO ARCHIVOS -------------------------------- 


#importo las clases de los productos

from PRODUCTO import producto
from PRODUCTO.panaderia import *
from PRODUCTO.bebidas import *
from PRODUCTO.carniceria import *
from PRODUCTO.galletitas import *
from PRODUCTO.verduleria import *
from PRODUCTO.perfumeria import *
from PRODUCTO.lacteos import *
from PRODUCTO.golosinas import *

#importo las funciones necesarias

from CARRITO import *
from ALMACEN import *
from GONDOLA import *
from INVENTARIO import *
from DEPOSITO import *
from prov_ped import *
from PANTALLA_CARRITO import *
from TABLET import *


import os
os.system('cls')


#me creo 3 productos de cada clase

# ----------------------------- VERDULERIA -----------------------

p1 = Verduleria("Zanahoria","V001","Genérica",precio_por_unidad=1200,umbral=15,peso_vendido=4.5)
p2 = Verduleria(nombre="Cebolla", codigo="V002", marca="Genérica", precio_por_unidad=980, umbral=20, peso_vendido=12.2)
p3 = Verduleria(nombre="Lechuga", codigo="V003", marca="Huerta Orgánica", precio_por_unidad=2500, umbral=8, peso_vendido=2.8)

p3.mostrar_info()
v1=[p1,p2,p3,p1,p1,p2,p3,p1,p2,p3,p1,p1,p2,p3,p1,p2,p3,p1,p1,p2,p3,p1,p2,p3,p1,p1,p2]

# ----------------------------- BEBIDAS----------------------------

p4 = Bebidas("Sprite Lima-Limón", "B001", "Coca-Cola", 3200, 10, 2.25)
p5 = Bebidas("Fanta Naranja", "B002", "Coca-Cola", 3100, 8, 2.25)
p6 = Bebidas("Manaos Cola", "B003", "Manaos", 2100, 15, 2.25)
p7 = Bebidas("Manaos Uva", "B004", "Manaos", 2200, 12, 2.25)
p8 = Bebidas("Aquarius Pera", "B005", "Coca-Cola", 2800, 7, 1.5)
p31 = Bebidas("Aquarius Naranja", "B006", "Coca-Cola", 2800, 7, 1.5)
p32 = Bebidas("Agua Mineral", "B007", "Villavicencio", 1700, 20, 2)
p33 = Bebidas("Cunnington Cola", "B008", "Cunnington", 1900, 10, 2.25)

bebidas=[p4,p5,p6,p7,p8,p8,p4,p5,p4,p4,p5,p6,p7,p8,p8,p4,p5,p4,p4,p5,p6,p7,p8,p8,p4,p5,p4]


#---------------------------- CARNICERIA --------------------------

p9 = Carniceria("Vacío", "C001", "Swift", 9500, 5, "Vacuno", 2.5)
p10 = Carniceria("Asado", "C002", "Coto", 8700, 4, "Vacuno", 3.0)
p11 = Carniceria("Chorizo", "C003", "Paladini", 3200, 10, None, None)
p24 = Carniceria("Morcilla", "C004", "Paladini", 2800, 8, None, None)

car=[p9,p10,p11,p24,p24,p11,p9,p10,p10,p10,p11,p24,p24,p9,p9]


#----------------------- GALLETITAS ------------------------------

p12 = Galletitas("Toddy Chocolatadas", "G001", "Toddy", 2500, 10)
p13 = Galletitas("Toddy Rellenas", "G002", "Toddy", 2700, 8)
p14 = Galletitas("Oreo Clásicas", "G003", "Oreo", 3000, 7)
p15 = Galletitas("Oreo Golden", "G004", "Oreo", 3100, 6)
p16 = Galletitas("Pitusas", "G005", "Terrabusi", 1800, 12)
p17 = Galletitas("Vainillas", "G006", "9 de Oro", 2200, 5)
p25 = Galletitas("Sonrisa Chocolate", "G007", "Bagley", 2000, 9)
p26 = Galletitas("Sonrisa Frutilla", "G008", "Bagley", 2000, 9)
p27 = Galletitas("Porteñitas", "G009", "Bagley", 2400, 4)

lista_galletitas = [p12, p13, p14, p15, p16, p17,p17,p16,p15,p26,p27,p25,p12,p12,p12,p14,p14,p15,p17,p17]


#--------------------- PERFUMERIA ----------------------------------- 

p18 = Perfumeria("Shampoo Reparación Total", "PF001", "Elvive", 4800, 6, "Shampoo")
p19 = Perfumeria("Desodorante Aerosol", "PF002", "Rexona", 3500, 8, "Desodorante")
p20 = Perfumeria("Jabón Líquido", "PF003", "Dove", 2900, 5, "Jabón")

perfu=[p18,p19,p18,p20,p20,p18,p20]

# ---------------------- LACTEOS --------------------------------------------

p21 = Lacteo("Leche Entera", "L001", "La Serenísima", 2500, 10, "Leche")
p22 = Lacteo("Yogur de Frutilla", "L002", "Ser", 1800, 5, "Yogur")
p23 = Lacteo("Queso Cremoso", "L003", "Casancrem", 4200, 3, "Queso")

l1=[p21,p21,p22,p23,p21,p22]


# ------------------------ PANADERIA -------------------------------






#------------------------- GOLOSINAS ---------------------------------

p28 = Golosinas("Gomitas Ácidas", "GO001", "Arcor", 1500, 10, 120)
p29 = Golosinas("Alfajor Triple", "GO002", "Jorgito", 1800, 8, 70)
p30 = Golosinas("Chupetín Pop", "GO003", "Topline", 500, 20, 15)

gol=[p28,p28,p29,p28,p29,p30,p30,p30,p28,p29,p30]


# ---------------- INVENTARIO --------------------------------
inv= Inventario(d1)



# ---------------- GONDOLA --------------------------------

g1= Gondola("Galletitas", lista_galletitas, 40)
g2= Gondola("Bedidas", bebidas, 50)
g3=Gondola ("Carniceria", car, 46)
g4=Gondola("Golosinas", gol, 150)
g5=Gondola("Lacteos", l1, 400)
g5= Gondola("Perfumeria", perfu, 600)

GONDOLAS=[g1,g2,g3,g4,g5]




# ---------------- DEPOSITO --------------------------------
d1= Deposito(g1, 460)



# ---------------- ALMACEN --------------------------------
Alm=Almacen()



#------------------------ ARMO EL CARRITO -------------------------

c1=Carrito()
pantalla= PantallaCarrito(c1)


while True: 
    rta=input("Desea agregar productos a su carrito? (si/no): ")
    #con la cantidad que quieRA AGREGAR, me creo un bucle

    if rta=="si":
        #llama a carrito
        Carrito.agregar_a_carrito(p16,3)

        #muestro lo que tengo en el carrito
        pantalla.mostrar_productos()
        pantalla.mostrar_total()

    



