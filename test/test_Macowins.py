from MacoWins import *

def reiniciar_lista_de_productos(sucursal):
    sucursal.productos.clear()

def test_actualizar_precio_segun_criterio_Porprecio():
    pantalon = Producto("jean", "ropa", 100 ,500)
    remera = Producto("chomba","ropa", 101,1000)
    
    sucursal_palermo = SucursalFisica()

    reiniciar_lista_de_productos(sucursal_palermo)
    
    sucursal_palermo.registrar_producto(pantalon)
    sucursal_palermo.registrar_producto(remera)
    sucursal_palermo.actualizar_precio_segun(PorPrecio(1000),50)
    assert  pantalon.retornar_precio() == 750

def test_actualizar_precio_segun_criterio_PorStock():
    pantalon = Producto("jean", "ropa", 100 ,500)
    remera = Producto("chomba","ropa", 101,1000)
    
    sucursal_palermo = SucursalFisica()
    
    reiniciar_lista_de_productos(sucursal_palermo)
    
    sucursal_palermo.registrar_producto(pantalon)
    sucursal_palermo.registrar_producto(remera)
    sucursal_palermo.actualizar_precio_segun(PorStock(101),50)
    assert remera.retornar_precio() == 1500

def test_actualizar_precio_segun_criterio_por_oposicion_de_PorPrecio():
    
    sucursal_palermo = SucursalFisica()

    reiniciar_lista_de_productos(sucursal_palermo)

    pantalon = Producto("jean", "ropa", 100 ,500)
    remera = Producto("chomba","ropa", 101,1000)
    sucursal_palermo.registrar_producto(pantalon)
    sucursal_palermo.registrar_producto(remera)
    sucursal_palermo.actualizar_precio_segun(PorOposicion(PorPrecio(300)),50)

    assert pantalon.retornar_precio() == 750

def test_actualizar_precio_segun_criterio_por_oposicion_de_PorStock_con_stock_0():
    
    sucursal_palermo = SucursalFisica()

    reiniciar_lista_de_productos(sucursal_palermo)

    pantalon = Producto("jean", "ropa", 100 ,500)
    remera = Producto("chomba","ropa", 101,1000)
    sucursal_palermo.registrar_producto(pantalon)
    sucursal_palermo.registrar_producto(remera)
    sucursal_palermo.actualizar_precio_segun(PorOposicion(PorStock(20)),50)

    assert pantalon.retornar_precio() == 500

def test_actualizar_precio_segun_criterio_por_oposicion_de_PorStock_con_stock_mayor_al_criterio():
    
    sucursal_palermo = SucursalFisica()

    reiniciar_lista_de_productos(sucursal_palermo)

    pantalon = Producto("jean", "ropa", 100 ,500)
    remera = Producto("chomba","ropa", 101,1000)
    sucursal_palermo.registrar_producto(pantalon)
    sucursal_palermo.registrar_producto(remera)
    sucursal_palermo.recargar_stock(100,300)
    sucursal_palermo.actualizar_precio_segun(PorOposicion(PorStock(20)),50)

    assert pantalon.retornar_precio() == 750