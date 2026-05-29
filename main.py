#--------------------------- IMPORTO ARCHIVOS -------------------------------- 


#importo las clases de los productos

from PRODUCTO.producto import *
from PRODUCTO.panaderia import *
from PRODUCTO.bebidas import *
from PRODUCTO.carniceria import *
from PRODUCTO.galletitas import *
from PRODUCTO.verduleria import Verduleria
from PRODUCTO.perfumeria import *
from PRODUCTO.lacteos import *
from PRODUCTO.golosinas import *

#importo las funciones necesarias1


from CARRITO import *
from ALMACEN import *
from GONDOLA import *
from INVENTARIO import *
from prov_ped import *
from PANTALLA_CARRITO import *
from TABLET import *


import os
os.system('cls')


#me creo 3 productos de cada clase

# ----------------------------- VERDULERIA -----------------------

p1 = Verduleria("Zanahoria "," V001","Genérica", precio_por_unidad=1200 ,peso_vendido=4.5)
p2 = Verduleria(nombre="Cebolla", codigo="V002", marca="Genérica", precio_por_unidad=980, peso_vendido=12.2)
p3 = Verduleria(nombre="Lechuga", codigo="V003", marca="Huerta Orgánica", precio_por_unidad=2500, peso_vendido=2.8)

print (p3)
v1=[p1,p2,p3]

# ----------------------------- BEBIDAS----------------------------

p4 = Bebidas("Sprite Lima-Limón", "B001", "Coca-Cola", 3200, 2.25)
p5 = Bebidas("Fanta Naranja", "B002", "Coca-Cola", 3100, 2.25)
p6 = Bebidas("Manaos Cola", "B003", "Manaos", 2100, 2.25)
p7 = Bebidas("Manaos Uva", "B004", "Manaos", 2200, 2.25)
p8 = Bebidas("Aquarius Pera", "B005", "Coca-Cola", 2800, 1.5)
p31 = Bebidas("Aquarius Naranja", "B006", "Coca-Cola", 2800, 1.5)
p32 = Bebidas("Agua Mineral", "B007", "Villavicencio", 1700, 2)
p33 = Bebidas("Cunnington Cola", "B008", "Cunnington", 1900, 2.25)

bebidas=[p4,p5,p6,p7,p8,p31, p32, p33]


#---------------------------- CARNICERIA --------------------------

p9 = Carniceria("Vacío", "C001", "Swift", 9500, "Vacuno", 2.5)
p10 = Carniceria("Asado", "C002", "Coto", 8700, "Vacuno", 3.0)
p11 = Carniceria("Chorizo", "C003", "Paladini", 3200, None, None)
p24 = Carniceria("Morcilla", "C004", "Paladini", 2800, None, None)

car=[p9,p10,p11,p24]


#----------------------- GALLETITAS ------------------------------

p12 = Galletitas("Toddy Chocolatadas", "G001", "Toddy", 2500)
p13 = Galletitas("Toddy Rellenas", "G002", "Toddy", 2700)
p14 = Galletitas("Oreo Clásicas", "G003", "Oreo", 3000)
p15 = Galletitas("Oreo Golden", "G004", "Oreo", 3100)
p16 = Galletitas("Pitusas", "G005", "Terrabusi", 1800)
p17 = Galletitas("Vainillas", "G006", "9 de Oro", 2200)
p25 = Galletitas("Sonrisa Chocolate", "G007", "Bagley", 2000)
p26 = Galletitas("Sonrisa Frutilla", "G008", "Bagley", 2000)
p27 = Galletitas("Porteñitas", "G009", "Bagley", 2400)

lista_galletitas = [p12, p13, p14, p15, p16, p17,p25, p26, p27]


#--------------------- PERFUMERIA ----------------------------------- 

p18 = Perfumeria("Shampoo Reparación Total", "PF001", "Elvive", 4800,  "Shampoo")
p19 = Perfumeria("Desodorante Aerosol", "PF002", "Rexona", 3500, "Desodorante")
p20 = Perfumeria("Jabón Líquido", "PF003", "Dove", 2900,  "Jabón")

perfu=[p18,p19,p20]

# ---------------------- LACTEOS --------------------------------------------

p21 = Lacteo("Leche Entera", "L001", "La Serenísima", 2500, "Leche")
p22 = Lacteo("Yogur de Frutilla", "L002", "Ser", 1800,"Yogur")
p23 = Lacteo("Queso Cremoso", "L003", "Casancrem", 4200, "Queso")

l1=[p21,p22, p23]


# ------------------------ PANADERIA -------------------------------






#------------------------- GOLOSINAS ---------------------------------

p28 = Golosinas("Gomitas Ácidas", "GO001", "Arcor", 1500, 120)
p29 = Golosinas("Alfajor Triple", "GO002", "Jorgito", 1800, 70)
p30 = Golosinas("Chupetín Pop", "GO003", "Topline", 500, 15)

gol=[p28,p29,p30]


# ---------------- GONDOLA --------------------------------
g1= Gondola("Galletitas", lista_galletitas,400,13 )
g2= Gondola("Bebidas", bebidas, 500,5)
g3=Gondola ("Carniceria", car, 4600, 5)
g4=Gondola("Golosinas", gol, 1500, 10)
g5=Gondola("Lacteos", l1, 4500, 10)
g6= Gondola("Perfumeria", perfu, 600, 10)
g7= Gondola("Verduleria", v1, 100, 12)

lista_gons=[g1,g2,g3,g4,g5,g6, g7]

GONDOLAS_MENU = {
    "1": g1,
    "2": g2,
    "3": g3,
    "4": g4,
    "5": g5,
    "6": g6,
}


# ---------------- PROVEEDORES --------------------------------
prov1=Proveedor("oreo", "ac1", "Galletitas", "151")
prov2=Proveedor("toddys", "sdvf4", "Galletitas", "15151")
prov3=Proveedor("gomidas", "ac1", "Golosinas", "1551")
prov4=Proveedor("Coca-Cola", "ac1", "Bebidas", "151")
prov5=Proveedor("Sprite", "ac1", "Bebidas", "151")
prov6=Proveedor("Shampoo", "ac1", "Perfumeria", "151")
prov7=Proveedor("Desodorante", "ac1", "Pefumeria", "151")
prov8=Proveedor("Jabon", "ac1", "Perfumeria", "151")

pedido1=Pedido(p13, 15)
pedido2= Pedido(p14, 50)
pedido3=Pedido(p15, 15)
pedido4= Pedido(p16, 50)


# ---------------- ALMACEN --------------------------------
Alm=Almacen()
Alm.agregar_prov(prov1)
Alm.agregar_prov(prov2)
Alm.agregar_prov(prov3)
Alm.agregar_prov(prov4)
Alm.agregar_prov(prov5)
Alm.agregar_prov(prov6)
Alm.agregar_prov(prov7)
Alm.agregar_prov(prov8)

# ---------------- INVENTARIO --------------------------------
inv=Inventario(lista_gons, Alm)


#------------------------ ARMO EL CARRITO Y SU PANTALLA -------------------------

c1=Carrito(Alm, inv)
Tab=Tablet
pantalla= PantallaCarrito(c1)

#----------------------------- MENU PRINCIPAL -------------------------------------

#menu de opciones


from interfaz_main import *


while True:

    print ("-----------BIENVENIDOS AL SUPERMERCADO NATI- AYLU -------------------")
    
    print ("-1) Recorrer las Gondolas ")
    print ("-2) Ver carrito ")
    print ("-3) Eliminar productos del carrito")
    print ("-4) Confirmar compra") 
    print ("-5) Ver Promociones")
    print ("-6) Salir ")
    separador()

    a=input("\n ----- Que desea hacer?-----: ").strip()

    match a:
        case '1': 
            print("\n" +"*" * 60)
            print("   GÓNDOLAS DEL SUPERMERCADO")
            print("*" * 60)
            # Recorremos la lista para mostrar todas las góndolas dinámicamente
            for idx, g in enumerate(lista_gons, start=1):
                print(f"  {idx}) Góndola: {g.tipo.title()}")
            
            b = input("\n¿Qué góndola querés visitar? (inserte índice): ").strip()

            # índice ingresado sea un número dentro del rango de la lista

            if b.isdigit() and 1 <= int(b) <= len(lista_gons):
                # seleccionamos el objeto góndola exacto 
                gondola_seleccionada = lista_gons[int(b) - 1] #restamos 1 porque el usuario ve de 1 a 6 y Python cuenta desde 0
                
                menu_gondola(gondola_seleccionada, c1, inv)
                
                
            else:
                print("\n✗ ERROR. Ingrese un número de índice válido.")



        case '2':
            pantalla.mostrar_productos()
            pantalla.mostrar_total ()
    
        case '3':

            #eliminar productos del carrito
            
            lista_removidos=eliminar_del_carrito(c1, Alm)
            inv.devolver_producto(lista_removidos)

        case "4":
            #confirmar la compra y visibiliza el ticket
            confirmar_compra(c1, Alm)
        case '5':
            pantalla.mostrar_promos()

        case '6':
            print ("\n Gracias por visitar el supermercado")
            break


        case _:  #en caso de error
            print("✗ Opción inválida. Ingresá un número del 1 al 6.")
        



    


