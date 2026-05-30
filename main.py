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
from PRODUCTO.facturas import *

#importo las funciones necesarias1


from carrito import *
from almacen import *
from gondola import *
from inventario import *
from prov_ped import *
from pantalla_carrito import *
from tablet import *


import os
os.system('cls')


#me creo 3 productos de cada clase

# ----------------------------- VERDULERIA -----------------------

ve1 = Verduleria("Zanahoria "," V001","Genérica", 1200 ,4.5)
v2 = Verduleria("Cebolla", "V002", "Genérica", 980, 12.2)
v3 = Verduleria("Lechuga", "V003", "Huerta Orgánica", 2500, 2.8)
v4 = Verduleria("Zanahoria "," V001","Genérica", 1200 ,4.5)
v5 = Verduleria("Cebolla", "V002", "Genérica", 980, 12.2)
v6 = Verduleria("Lechuga", "V003", "Huerta Orgánica", 2500, 2.8)
v7 = Verduleria("Zanahoria "," V001","Genérica", 1200 ,4.5)
v8 = Verduleria("Cebolla", "V002", "Genérica", 980, 12.2)
v9 = Verduleria("Lechuga", "V003", "Huerta Orgánica", 2500, 2.8)
v10 = Verduleria("Zanahoria "," V001","Genérica", 1200 ,4.5)
v11 = Verduleria("Cebolla", "V002", "Genérica", 980, 12.2)
v12 = Verduleria("Lechuga", "V003", "Huerta Orgánica", 2500, 2.8)

v1=[ve1, v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12]

# ----------------------------- BEBIDAS----------------------------

b1 = Bebidas("Sprite Lima-Limón", "B001", "Coca-Cola", 3200, 2.25)
b2 = Bebidas("Fanta Naranja", "B002", "Coca-Cola", 3100, 2.25)
b3 = Bebidas("Manaos Cola", "B003", "Manaos", 2100, 2.25)
b4 = Bebidas("Manaos Uva", "B004", "Manaos", 2200, 2.25)
b5 = Bebidas("Aquarius Pera", "B005", "Coca-Cola", 2800, 1.5)
b6 = Bebidas("Aquarius Naranja", "B006", "Coca-Cola", 2800, 1.5)
b7 = Bebidas("Agua Mineral", "B007", "Villavicencio", 1700, 2)
b8 = Bebidas("Cunnington Cola", "B008", "Cunnington", 1900, 2.25)
b9 = Bebidas("Sprite Lima-Limón", "B001", "Coca-Cola", 3200, 2.25)
b10 = Bebidas("Fanta Naranja", "B002", "Coca-Cola", 3100, 2.25)
b11= Bebidas("Manaos Cola", "B003", "Manaos", 2100, 2.25)
b12= Bebidas("Manaos Uva", "B004", "Manaos", 2200, 2.25)
b13= Bebidas("Aquarius Pera", "B005", "Coca-Cola", 2800, 1.5)
b14= Bebidas("Aquarius Naranja", "B006", "Coca-Cola", 2800, 1.5)
b15= Bebidas("Agua Mineral", "B007", "Villavicencio", 1700, 2)
b16= Bebidas("Cunnington Cola", "B008", "Cunnington", 1900, 2.25)

bebidas=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]


#---------------------------- CARNICERIA --------------------------

c1 = Carniceria("Asado", "3001", "La Hacienda", 12000, "Vacuno", 1.5)
c2 = Carniceria("Costillitas", "3002", "La Hacienda", 10000, "Cerdo", 1.2)
c3 = Carniceria("Pechito de cerdo", "3003", "Swift", 9500, "Cerdo", 1.0)
c4 = Carniceria("Chorizo", "3004", "Paladini", 800, None, None)

car=[c1,c2,c3,c4]


#----------------------- GALLETITAS ------------------------------

ga1 = Galletitas("Toddy Chocolatadas", "G001", "Toddy", 2500)
ga2 = Galletitas("Toddy Rellenas", "G002", "Toddy", 2700)
ga3 = Galletitas("Oreo Clásicas", "G003", "Oreo", 3000)
ga4 = Galletitas("Oreo Golden", "G004", "Oreo", 3100)
ga5 = Galletitas("Pitusas", "G005", "Terrabusi", 1800)
ga6 = Galletitas("Vainillas", "G006", "9 de Oro", 2200)
ga7 = Galletitas("Sonrisa Chocolate", "G007", "Bagley", 2000)
ga8 = Galletitas("Sonrisa Frutilla", "G008", "Bagley", 2000)
ga9 = Galletitas("Porteñitas", "G009", "Bagley", 2400)
ga10 = Galletitas("Toddy Chocolatadas", "G001", "Toddy", 2500)
ga11 = Galletitas("Toddy Rellenas", "G002", "Toddy", 2700)
ga12 = Galletitas("Oreo Clásicas", "G003", "Oreo", 3000)
ga13= Galletitas("Oreo Golden", "G004", "Oreo", 3100)
ga14= Galletitas("Pitusas", "G005", "Terrabusi", 1800)
ga15= Galletitas("Vainillas", "G006", "9 de Oro", 2200)
ga16= Galletitas("Sonrisa Chocolate", "G007", "Bagley", 2000)
ga17= Galletitas("Sonrisa Frutilla", "G008", "Bagley", 2000)
ga18= Galletitas("Porteñitas", "G009", "Bagley", 2400)

lista_galletitas = [ga1,ga2,ga3,ga4,ga5,ga6,ga7,ga8,ga9,ga10,ga11,ga12,ga13,ga14,ga15,ga16,ga17,ga18]


#--------------------- PERFUMERIA ----------------------------------- 

p1 = Perfumeria("Shampoo Reparación Total", "PF001", "Elvive", 4800,  "Shampoo")
p2 = Perfumeria("Desodorante Aerosol", "PF002", "Rexona", 3500, "Desodorante")
p3 = Perfumeria("Jabón Líquido", "PF003", "Dove", 2900,  "Jabón")
p4 = Perfumeria("Shampoo Reparación Total", "PF001", "Elvive", 4800,  "Shampoo")
p5 = Perfumeria("Desodorante Aerosol", "PF002", "Rexona", 3500, "Desodorante")
p6 = Perfumeria("Jabón Líquido", "PF003", "Dove", 2900,  "Jabón")
perfu=[p1,p2,p3,p4,p5,p6]

# ---------------------- LACTEOS --------------------------------------------

la1 = Lacteo("Leche Entera", "L001", "La Serenísima", 2500, "Leche")
la2 = Lacteo("Yogur de Frutilla", "L002", "Ser", 1800,"Yogur")
la3 = Lacteo("Queso Cremoso", "L003", "Casancrem", 4200, "Queso")
la4 = Lacteo("Leche Entera", "L001", "La Serenísima", 2500, "Leche")
la5 = Lacteo("Yogur de Frutilla", "L002", "Ser", 1800,"Yogur")
la6 = Lacteo("Queso Cremoso", "L003", "Casancrem", 4200, "Queso")

l1=[la1,la2,la3,la4,la5,la6]


# ------------------------ PANADERIA -------------------------------

pan1 = Panaderia("Pan lactal blanco", "2001", "Bimbo", 2500, "Lactal")
pan2 = Panaderia("Pan de hamburguesa", "2002", "Fargo", 1800, "Hamburguesa")
pan3 = Panaderia("Pan pebete", "2003", "Fargo", 1500, "Pebete")
pan4 = Panaderia("Pan integral", "2004", "Bimbo", 2800, "Integral")
pan5 = Panaderia("Pan de molde", "2005", "Lactal", 2300, "Molde")

lista_panaderia=[pan2, pan3, pan4, pan5, pan1]

#----------------------- FACTURAS ----------------------------------
f1 = Factura("Medialuna de manteca", "1001", "La Panadería", 500, "Medialuna")
f2 = Factura("Vigilante", "1002", "La Panadería", 650, "Vigilante")
f3 = Factura("Torta negra", "1003", "Dulce Hogar", 800, "Torta Negra")
f4 = Factura("Cañoncito de dulce de leche", "1004", "Dulce Hogar", 900, "Cañoncito")
f5 = Factura("Bola de fraile", "1005", "Panificados SRL", 750, "Bola de Fraile")

list_facturas=[f1,f2,f3,f4,f5]


#------------------------- GOLOSINAS ---------------------------------

gol1 = Golosinas("Gomitas Ácidas", "GO001", "Arcor", 1500, 120)
gol2 = Golosinas("Alfajor Triple", "GO002", "Jorgito", 1800, 70)
gol3 = Golosinas("Chupetín Pop", "GO003", "Topline", 500, 15)
gol4 = Golosinas("Gomitas Ácidas", "GO001", "Arcor", 1500, 120)
gol5 = Golosinas("Alfajor Triple", "GO002", "Jorgito", 1800, 70)
gol6 = Golosinas("Chupetín Pop", "GO003", "Topline", 500, 15)
gol=[gol1,gol2,gol3,gol4,gol5,gol6]


# ---------------- GONDOLA --------------------------------
g1= Gondola("Galletitas", lista_galletitas,400,3 )
g2= Gondola("Bebidas", bebidas, 500,5)
g3=Gondola ("Carniceria", car, 4600, 5)
g4=Gondola("Golosinas", gol, 1500, 10)
g5=Gondola("Lacteos", l1, 4500, 10)
g6= Gondola("Perfumeria", perfu, 600, 10)
g7= Gondola("Verduleria", v1, 100, 2)
g8= Gondola("Panaderia", lista_panaderia, 450, 4)
g9= Gondola("Facturas", list_facturas, 450, 2)

lista_gons=[g1,g2,g3,g4,g5,g6,g7, g8, g9]

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

pedido1=Pedido(b2, 15)
pedido2= Pedido(b3, 50)
pedido3=Pedido(gol1, 15)
pedido4= Pedido(b1, 50)
pedido5=Pedido(gol5,150)


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
Tab=Tablet()
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

            # se recorre la lista para mostrar todas las góndolas dinámicamente
            for idx, g in enumerate(lista_gons, start=1):
                print(f"  {idx}) Góndola: {g.tipo.title()}")
            
            b = input("\n¿Qué góndola querés visitar? (inserte índice): ").strip()

            # índice ingresado --> un número dentro del rango de la lista

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
        



    


