from GONDOLA import Gondola
from PRODUCTOS.producto import Producto
from PRODUCTOS.verduleria import Verduleria
from PRODUCTOS.panaderia import Panaderia
from PRODUCTOS.carniceria import Carniceria
from PRODUCTOS.galletitas import Galletitas
from PRODUCTOS.bebidas import Bebidas



#me creo 3 productos de cada gondola
g= Gondola("verduleria")
zanahoria = Verduleria("zanahoria",5000,"verduleria",True,"334",2,5000)
#morron= Verduleria(4500, "morron", )

g.agregar_producto(zanahoria)

g.mostrar_productos()

print(type(zanahoria))
print(zanahoria.__str__())