from MacoWins import *

sucursal_palermo = SucursalFisica()

def reiniciar_lista_de_productos(sucursal):
    sucursal.productos.clear()

def test_actualizar_precio_segun_criterio_Porprecio():
    pantalon = Producto("jean", "ropa", 100 ,500)
    remera = Producto("chomba","ropa", 101,1000)
    sucursal_palermo = SucursalFisica()
    sucursal_palermo.registrar_producto(pantalon)
    sucursal_palermo.registrar_producto(remera)
    sucursal_palermo.actualizar_precio_segun(PorPrecio(1000),50)
    assert  pantalon.retornar_precio() == 750

def test_actualizar_precio_segun_criterio_PorStock():
    pantalon = Producto("jean", "ropa", 100 ,500)
    remera = Producto("chomba","ropa", 101,1000)
    sucursal_palermo = SucursalFisica()
    sucursal_palermo.registrar_producto(pantalon)
    sucursal_palermo.registrar_producto(remera)
    sucursal_palermo.actualizar_precio_segun(PorStock(101),50)
    assert remera.retornar_precio() == 1500
