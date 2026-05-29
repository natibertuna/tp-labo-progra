
#importo las funciones necesarias

from CARRITO import *
from ALMACEN import *
from GONDOLA import *
from INVENTARIO import *
from prov_ped import *
from PANTALLA_CARRITO import *
from TABLET import *


import os
os.system('cls')



def separador(titulo=""):      #fin puramente estetico
    linea = "=" * 50
    if titulo:
        print(f"\n{linea}")
        print(f"  {titulo}")
        print(linea)
    else:
        print(linea)

def gondolas (gond_menu: dict[int, Gondola]):
    while True:

        print("\n" +"*" * 60)
        print("   GÓNDOLAS DEL SUPERMERCADO")
        print("*" * 60)
 
        # Mostrar cada góndola con sus productos únicos y stock
        
        for num, gondola in gond_menu.items():
            # Contar productos únicos con stock disponible
            total_stock = sum(gondola.dic.values())
 
            print(f"\n  [{num}] ── {gondola.tipo.upper()} ── ({total_stock} unidades disponibles)")
            print(f"  {'─'*54}")


        



def menu_gondola (gond: Gondola, carrito:Carrito, inventario:Inventario):
    # lista de productos únicos (sin repetidos)

    while True:

        print(f"\n{'*'*40}")
        print(f"  Góndola: {gond.tipo}")
        print(f"{'*'*40}")
        
        separador(f"Góndola: {gond.tipo}")

        gond.mostrar_productos()
        print("  0) Volver al menú de góndolas")
        print("*" * 40)

        #creamos el menu interactivo con el usuario


        opcion = input("Elegí un producto: ").strip()

        if opcion == "0" or opcion == "":
            print("\nVolviendo al menú principal...")
            return

        codigos_unicos = list(gond.dic.keys())

        # Validamos que el número ingresado corresponda a un producto de la lista
        if not opcion.isdigit() or not (1 <= float(opcion) <= len(codigos_unicos)):
            print("✗ Opción inválida. Intente de nuevo.")
            continue

        # Buscamos el producto real
        cod_elegido = codigos_unicos[int(opcion) - 1]
        prod_elegido = gond.buscar_producto(cod_elegido)
        if prod_elegido is None:
            print("producto no encontrado")
            continue

        # preguntamos cantidad
        if gond.tipo=="Carniceria":
            cant_str= input(f"¿Cuántos kilos de '{prod_elegido.nombre}' desea agregar?:   ").strip()
            if not cant_str.isdigit():
                print("Cantidad inválida.")
                return
            cantidad = float(cant_str)

        else:
            cant_str = input(f"¿Cuántas unidades de '{prod_elegido.nombre}' desea agregar?:   ").strip()
            if not cant_str.isdigit() or int(cant_str) < 1:
                print("Cantidad inválida.")
                return
            cantidad = int(cant_str)

        # agregamos al carrito tantas veces como el usuario decida  --> pero de a un producto a la vez
        
        agregados = 0

        stock = gond.dic[cod_elegido]
        if cantidad <= stock:
            for _ in range(cantidad):
                if inventario.verificar_stock(gond, prod_elegido)== True:
                    carrito.agregar_a_carrito(prod_elegido, gond)
                    agregados += 1

        else:

            for i in range (stock):
                 carrito.agregar_a_carrito(prod_elegido, gond)
                 agregados += 1

            gond.reponer_inventario(inventario, prod_elegido)
            print(f"Solo se pudieron agregar {agregados} unidades de {cantidad}.")
            continue


        if agregados > 0:
            print(f"\n  ✓ {agregados} x '{prod_elegido.nombre}' agregado/s al carrito.")
 
        # preguntar si sigue comprando en esta góndola
        seguir = input("  ¿Agregar otro producto de esta góndola? (s/n): ").strip().lower()

        while seguir not in ("s", "n"):
            seguir = input("  ¿Agregar otro producto de esta góndola? (s/n): ").lower().strip()

        
    

def _confirmar_compra(carrito:Carrito, alm:Almacen ):
    separador("TICKET DE COMPRA")
 
    resumen = {} #crea diccionario asi no se ven los repetidos

    for prod in carrito.list_prod:
        cod = prod.codigo_barras

        if cod not in resumen:
            resumen[cod] = {"prod": prod, "cant": 0, "subtotal": 0.0}

        resumen[cod]["cant"] += 1

        resumen[cod]["subtotal"] += prod.precio_final
 
    for datos in resumen.values():
        p = datos["prod"]
        print(f"  {p.nombre:<30} x{datos['cant']}   ${datos['subtotal']:>10.2f}")
 
    separador()
    print(f"  {'TOTAL A PAGAR':<30}      ${carrito.total:>10.2f}")

    separador()

    print("\n  ¡Gracias por su compra en Supermercado Nati-Aylu!")
 
    # Guardar carrito en historial y resetear
    alm.carritos_previos.append(list(carrito.list_prod))
    carrito.vaciar()
 
    input("\n  Presioná ENTER para continuar...")


def eliminar_del_carrito(c1:Carrito, alm:Almacen):
    
    productos_eliminados:list[Producto]=[]

    while True:
        if not c1.list_prod:
            print("\n  El carrito está vacío.")
            a= input("  Presioná ENTER para volver...")

            if a:
                print("  ✗ Opción inválida.")
            continue
 
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
            print(f"  {i}) {p.nombre} ({p.marca})  x{datos['cant']}  - ${p.precio:.2f} c/u")
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
                    productos_eliminados.append(prod_elegido)

                    print(f"  ✓ Se eliminó 1 unidad de '{prod_elegido.nombre}'.")

                case "2":
                    for _ in range(cant_actual):
                        c1.list_prod.remove(prod_elegido)
                        productos_eliminados.append(prod_elegido)
                    print(f"  ✓ Se eliminaron todas las unidades de '{prod_elegido.nombre}'.")

                case "0" | "":
                    continue
                case _:
                    print("  ✗ Opción inválida.")
        else:
            c1.list_prod.remove(prod_elegido)
            productos_eliminados.append(prod_elegido)
            print(f"  ✓ '{prod_elegido.nombre}' eliminado del carrito.")
 
        # Recalcular total
        alm.precio_final(c1)
        return productos_eliminados
 
def confirmar_compra(c1:Carrito, alm:Almacen):
    separador("TICKET DE COMPRA")
 
    if not c1.list_prod:
        print("  El carrito está vacío.")
        input("\n  Presioná ENTER para continuar…")
        return
 
    resumen: dict = {}
    for prod in c1.list_prod:
        cod = prod.codigo_barras
        if cod not in resumen:
            resumen[cod] = {"prod": prod, "cant": 0, "subtotal": 0.0}
        resumen[cod]["cant"]    += 1
        resumen[cod]["subtotal"] += prod.precio_final
 
    for datos in resumen.values():
        p = datos["prod"]
        print(f"  {p.nombre:<32} x{datos['cant']}   ${datos['subtotal']:>10.2f}")
 
    separador()
    print(f"  {'TOTAL A PAGAR':<32}      ${c1.total:>10.2f}")
    separador()
    print("\n  ¡Gracias por su compra en Supermercado Nati-Aylu!")
 
    alm.carritos_previos.append(list(c1.list_prod))
    c1.vaciar()
    input("\n  Presioná ENTER para continuar…")
 