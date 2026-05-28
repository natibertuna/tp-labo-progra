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
v1=[p1,p2,p3]

# ----------------------------- BEBIDAS----------------------------

p4 = Bebidas("Sprite Lima-Limón", "B001", "Coca-Cola", 3200, 10, 2.25)
p5 = Bebidas("Fanta Naranja", "B002", "Coca-Cola", 3100, 8, 2.25)
p6 = Bebidas("Manaos Cola", "B003", "Manaos", 2100, 15, 2.25)
p7 = Bebidas("Manaos Uva", "B004", "Manaos", 2200, 12, 2.25)
p8 = Bebidas("Aquarius Pera", "B005", "Coca-Cola", 2800, 7, 1.5)
p31 = Bebidas("Aquarius Naranja", "B006", "Coca-Cola", 2800, 7, 1.5)
p32 = Bebidas("Agua Mineral", "B007", "Villavicencio", 1700, 20, 2)
p33 = Bebidas("Cunnington Cola", "B008", "Cunnington", 1900, 10, 2.25)

bebidas=[p4,p5,p6,p7,p8,p31, p32, p33]


#---------------------------- CARNICERIA --------------------------

p9 = Carniceria("Vacío", "C001", "Swift", 9500, 5, "Vacuno", 2.5)
p10 = Carniceria("Asado", "C002", "Coto", 8700, 4, "Vacuno", 3.0)
p11 = Carniceria("Chorizo", "C003", "Paladini", 3200, 10, None, None)
p24 = Carniceria("Morcilla", "C004", "Paladini", 2800, 8, None, None)

car=[p9,p10,p11,p24]


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

lista_galletitas = [p12, p13, p14, p15, p16, p17,p25, p26, p27]


#--------------------- PERFUMERIA ----------------------------------- 

p18 = Perfumeria("Shampoo Reparación Total", "PF001", "Elvive", 4800, 6, "Shampoo")
p19 = Perfumeria("Desodorante Aerosol", "PF002", "Rexona", 3500, 8, "Desodorante")
p20 = Perfumeria("Jabón Líquido", "PF003", "Dove", 2900, 5, "Jabón")

perfu=[p18,p19,p20]

# ---------------------- LACTEOS --------------------------------------------

p21 = Lacteo("Leche Entera", "L001", "La Serenísima", 2500, 10, "Leche")
p22 = Lacteo("Yogur de Frutilla", "L002", "Ser", 1800, 5, "Yogur")
p23 = Lacteo("Queso Cremoso", "L003", "Casancrem", 4200, 3, "Queso")

l1=[p21,p22, p23]


# ------------------------ PANADERIA -------------------------------






#------------------------- GOLOSINAS ---------------------------------

p28 = Golosinas("Gomitas Ácidas", "GO001", "Arcor", 1500, 10, 120)
p29 = Golosinas("Alfajor Triple", "GO002", "Jorgito", 1800, 8, 70)
p30 = Golosinas("Chupetín Pop", "GO003", "Topline", 500, 20, 15)

gol=[p28,p29,p30]


# ---------------- GONDOLA --------------------------------

g1= Gondola("Galletitas", lista_galletitas, 40, 15)
g2= Gondola("Bedidas", bebidas, 50,5)
g3=Gondola ("Carniceria", car, 46, 5)
g4=Gondola("Golosinas", gol, 150, 10)
g5=Gondola("Lacteos", l1, 400, 10)
g6= Gondola("Perfumeria", perfu, 600, 10)

lista_gons=[g1,g2,g3,g4,g5, g6]

GONDOLAS_MENU = {
    "1": g1,
    "2": g2,
    "3": g3,
    "4": g4,
    "5": g5,
    "6": g6,
}

# ---------------- ALMACEN --------------------------------
Alm=Almacen()

# ---------------- DEPOSITO --------------------------------
d1= Deposito(g1,400,Alm)
d2= Deposito(g2, 500, Alm)
d3 = Deposito(g3, 4000, Alm)
d4= Deposito(g4, 4650, Alm)
d5 =  Deposito(g5, 478, Alm)

DEPO = [d1, d2, d3, d4, d5]




# ---------------- INVENTARIO --------------------------------
inv=Inventario(DEPO)

#------------------------ ARMO EL CARRITO Y SU PANTALLA -------------------------

c1=Carrito(Alm, inv)
Tab=Tablet
pantalla= PantallaCarrito(c1)







#----------------------------- MENU PRINCIPAL -------------------------------------

#menu de opciones

def separador(titulo=""):      #fin puramente estetico
    linea = "=" * 50
    if titulo:
        print(f"\n{linea}")
        print(f"  {titulo}")
        print(linea)
    else:
        print(linea)

def menu_gondola(gondola: Gondola):
    # lista de productos únicos (sin repetidos)

    while True:

        print("\n" + "=" * 60)
        print("   GÓNDOLAS DEL SUPERMERCADO")
        print("=" * 60)
 
        # Mostrar cada góndola con sus productos únicos y stock
        
        for num, gondola in GONDOLAS_MENU.items():
            # Contar productos únicos con stock disponible
            total_stock = sum(gondola.dic.values())
 
            print(f"\n  [{num}] ── {gondola.tipo.upper()} ── ({total_stock} unidades disponibles)")
            print(f"  {'─'*54}")

        vistos = {}  #diccionario que filtra duplicados

        for prod in gondola.productos:
            if prod.codigo_barras not in vistos:
                vistos[prod.codigo_barras] = prod

        productos_unicos = list(vistos.values())

        #menu enumerado

        print(f"\n{'='*40}")
        print(f"  Góndola: {gondola.tipo}")
        print(f"{'='*40}")
        
        separador(f"Góndola: {gondola.tipo}")
        for i, prod in enumerate(productos_unicos, start=1):
            stock = gondola.dic.get(prod.codigo_barras, 0)
            sin_stock = "  ✗ SIN STOCK" if stock == 0 else f"  (stock: {stock})"
            print(f"  {i}) {prod.nombre} ({prod.marca}) - ${prod.precio:.2f}{sin_stock}")

        print(f"\n  0) Volver al menú de góndolas")
        separador()
        
        print(f"{'='*40}")


        #creamos el menu interactivo con el usuario

        opcion = input("Elegí un producto: ").strip()

        if opcion == "0" or opcion == "":
            print("Opcion invalida")
            return

        if not opcion.isdigit() or not (1 <= int(opcion) <= len(productos_unicos)):  #valida que no ingresen letras antes de convertirlo a nro
            print("Opción inválida.")
            return

        prod_elegido = productos_unicos[int(opcion) - 1]


        # preguntamos cantidad

        cant_str = input(f"¿Cuántas unidades de '{prod_elegido.nombre}' desea agregar?:   ").strip()

        if not cant_str.isdigit() or int(cant_str) < 1:
            print("Cantidad inválida.")
            return

        cantidad = int(cant_str)

        # agregamos al carrito tantas veces como el usuario decida  --> pero de a un producto a la vez
        
        agregados = 0

        for _ in range(cantidad):
            if gondola.dic.get(prod_elegido.codigo_barras, 0) > 0:
                c1.agregar_a_carrito(prod_elegido, gondola)
                agregados += 1
            else:
                print(f"Solo se pudieron agregar {_ } unidades (sin más stock).")
                break

        if agregados > 0:
            print(f"\n  ✓ {agregados} x '{prod_elegido.nombre}' agregado/s al carrito.")
 
        # preguntar si sigue comprando en esta góndola
        seguir = input("  ¿Agregar otro producto de esta góndola? (s/n): ").strip().lower()
        if seguir != "s":
            return

def _confirmar_compra():
    separador("TICKET DE COMPRA")
 
    resumen = {} #crea diccionario asi no se ven los repetidos

    for prod in c1.list_prod:
        cod = prod.codigo_barras

        if cod not in resumen:
            resumen[cod] = {"prod": prod, "cant": 0, "subtotal": 0.0}

        resumen[cod]["cant"] += 1

        resumen[cod]["subtotal"] += prod.precio_final
 
    for datos in resumen.values():
        p = datos["prod"]
        print(f"  {p.nombre:<30} x{datos['cant']}   ${datos['subtotal']:>10.2f}")
 
    separador()
    print(f"  {'TOTAL A PAGAR':<30}      ${c1.total:>10.2f}")
    separador()
    print("\n  ¡Gracias por su compra en Supermercado Estrella!")
 
    # Guardar carrito en historial y resetear
    Alm.carritos_previos.append(list(c1.list_prod))
    c1.vaciar()
 
    input("\n  Presioná ENTER para continuar...")


def eliminar_del_carrito():
 
    while True:
        if not c1.list_prod:
            print("\n  El carrito está vacío.")
            input("  Presioná ENTER para volver...")
            return
 
        # agrupar por código para mostrar sin repetir
        resumen = {}
        for prod in c1.list_prod:
            cod = prod.codigo_barras
            if cod not in resumen:
                resumen[cod] = {"prod": prod, "cant": 0}
            resumen[cod]["cant"] += 1
 
        items = list(resumen.items())
 
        separador("Eliminar productos del carrito")

        for i, (cod, datos) in enumerate(items, start=1):
            p = datos["prod"]
            print(f"  {i}) {p.nombre} ({p.marca})  x{datos['cant']}  - ${p.precio_final:.2f} c/u")
        print(f"\n  0) Volver sin eliminar")

        separador()

        opcion = input("  ¿Qué producto querés eliminar? ").strip()
 
        if opcion == "0" or opcion == "":
            return
 
        if not opcion.isdigit() or not (1 <= int(opcion) <= len(items)):
            print("  ✗ Opción inválida.")
            continue
 
        cod_elegido, datos = items[int(opcion) - 1]
        prod_elegido = datos["prod"]
        cant_actual  = datos["cant"]
 
        if cant_actual > 1:
            separador()
            print(f"  Tenés {cant_actual} unidades de '{prod_elegido.nombre}'.")
            print(f"  1) Eliminar una unidad")
            print(f"  2) Eliminar todas ({cant_actual})")
            print(f"  0) Cancelar")
            separador()
            sub = input("  ¿Qué querés hacer? ").strip()

            match sub:
                case "1":
                    c1.list_prod.remove(prod_elegido)
                    print(f"  ✓ Se eliminó 1 unidad de '{prod_elegido.nombre}'.")
                case "2":
                    for _ in range(cant_actual):
                        c1.list_prod.remove(prod_elegido)
                    print(f"  ✓ Se eliminaron todas las unidades de '{prod_elegido.nombre}'.")
                case "0" | "":
                    continue
                case _:
                    print("  ✗ Opción inválida.")
        else:
            c1.list_prod.remove(prod_elegido)
            print(f"  ✓ '{prod_elegido.nombre}' eliminado del carrito.")
 
        # Recalcular total
        c1.total = sum(p.precio_final for p in c1.list_prod)
 

print ("-----------BIENVENIDOS AL SUPERMERCADO ESTRELLA-------------------")

print ("-1) Recorrer las Gondolas ")
print ("-2) Ver carrito ")
print ("-3) Eliminar productos del carrito")
print ("-4) Confirmar compra") 
print ("-5) Salir ")

a=input(print("----- Que desea hacer?-----: "))

match a:
    case '1': 
        print("Gondola 1: Verduleria ")
        print("Gondola 2: Bebidas ")
        print("Gondola 3: Carniceria ")
        print("Gondola 4: Golosinas ")
        print("Gondola 5: Lacteos ")
        print("Gondola 6: Panaderia ")
        print("Gondola 7: Perfumeria ")

        b=input(print("\n¿Qué góndola querés visitar? (inserte indice): ")).strip()

        if b==1:
            menu_gondola(g1)
        elif b==2:
            menu_gondola(g2)
        elif b==3:
            menu_gondola(g3)
        elif b==4:
            menu_gondola(g4)
        elif b==5:
            menu_gondola(g5)
        elif b==6:
            menu_gondola(g6)
        elif b==7:
            menu_gondola(g7)
        else:
            print ("ERROR. \n Ingrese un nro valido")

    case '2':
        pantalla.mostrar_productos()
        pantalla.mostrar_total ()
        pantalla.mostrar_promos
    
    case '3':

        #eliminar productos del carrito
        eliminar_del_carrito()

    case "4":
        #confirmar la compra y visibiliza el ticket
        _confirmar_compra()

    case '5':
        print ("\n Gracias por visitar el supermercado")

    case _:  #en caso de error
        print("✗ Opción inválida. Ingresá un número del 1 al 5.")
        



    



