#--------------------------- IMPORTO ARCHIVOS -------------------------------- 


#importo las clases de los productos

from PRODUCTO import producto
from PRODUCTO.panaderia import *
from PRODUCTO.bebidas import *
from PRODUCTO.carniceria import *
from PRODUCTO.galletitas import *
from PRODUCTO.verduleria import *
from PRODUCTO.higiene import *
from PRODUCTO.lacteos import *

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
p14 = Galletitas("Vainillas", "GALL003", "Valente", 2100.00, 20)
p15 = Galletitas("Pitusas", "GALL004", "Parripan", 950.00, 60)
p16 = Galletitas("Sonrisas", "GALL005", "Bagley", 1300.00, 40)
p17 = Galletitas("Porteñitas", "GALL006", "Bagley", 1100.00, 35)

lista_galletitas = [p12, p13, p14, p15, p16, p17]


#--------------------- HIGIENE ----------------------------------- 

p18 = Higiene("Jabón de Tocador", "HIG001", "Rexona", 1200.00, 50, 15, 120, "Corporal")
p19 = Higiene("Desodorante Roll-On", "HIG002", "Dove", 3100.00, 24, 6, 60, "Desodorante")
p20 = Higiene("Shampoo Control Caspa", "HIG003", "Head & Shoulders", 4500.00, 18, 5, 40, "Capilar")


# ---------------------- LACTEOS --------------------------------------------

p21 = Lacteo("Leche Entera 1L", "LAC001", "La Serenísima", 1400.00, 60, 15, 150, "Leche")
P22 = Lacteo("Yogur Frutilla 1Kg", "LAC002", "Ilolay", 2200.00, 25, 8, 60, "Yogur")
P23 = Lacteo("Queso Crema 300g", "LAC003", "Casancrem", 3100.00, 20, 5, 40, "Queso")


# ------------------------ PANADERIA -------------------------------






# ---------------- INVENTARIO --------------------------------
inv= Inventario(d1)



# ---------------- GONDOLA --------------------------------

g1= Gondola("Galletitas", lista_galletitas, )




# ---------------- DEPOSITO --------------------------------
d1= Deposito(p12, 150,Alm)



# ---------------- ALMACEN --------------------------------
Alm=Almacen()



#------------------------ ARMO EL CARRITO -------------------------

c1=Carrito()
pantalla= PantallaCarrito(c1)


while True: 
    rta=input("Desea agregar productos a su carrito? (si/no): ")

    if rta=="si":
        #llama a carrito
        Carrito.agregar_a_carrito(p16,3)

        #muestro lo que tengo en el carrito
        pantalla.mostrar_productos()
        pantalla.mostrar_total()

    



