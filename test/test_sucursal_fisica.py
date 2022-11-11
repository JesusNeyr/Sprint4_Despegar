from sucursales.sucursal_fisica import *
from producto.producto import *
import pytest

def reiniciar_lista_de_productos(sucursal):
    sucursal.productos.clear()


def test_ganancia_del_dia_sin_ventas():

    una_sucursal_fisica=SucursalFisica()

    reiniciar_lista_de_productos(una_sucursal_fisica)

    remera=Producto("remera","sport",1,2000)
    pantalon=Producto("pantalon","sport",2,2500)
    short=Producto("short","sport",3,3000)
    saco=Producto("saco","formal",4,3500)
    una_sucursal_fisica.registrar_producto(remera)
    una_sucursal_fisica.registrar_producto(pantalon)
    una_sucursal_fisica.registrar_producto(short)
    una_sucursal_fisica.registrar_producto(saco)

    with pytest.raises(ValueError) as exception_info:
        una_sucursal_fisica.ganancias_total_por_dia()
    assert str(exception_info.value)=="El valor de las ventas del dia son menores al gasto por dia"

def test_comprobar_la_ganancia_del_dia():

    una_sucursal_fisica=SucursalFisica()

    reiniciar_lista_de_productos(una_sucursal_fisica)

    remera=Producto("remera","sport",1,2000)
    pantalon=Producto("pantalon","sport",2,2500)
    short=Producto("short","sport",3,3000)
    saco=Producto("saco","formal",4,3500)
    una_sucursal_fisica.registrar_producto(remera)
    una_sucursal_fisica.registrar_producto(pantalon)
    una_sucursal_fisica.registrar_producto(short)
    una_sucursal_fisica.registrar_producto(saco)
    una_sucursal_fisica.recargar_stock(1,40)
    una_sucursal_fisica.recargar_stock(2,50)
    una_sucursal_fisica.recargar_stock(3,60)
    una_sucursal_fisica.recargar_stock(4,70)
    una_sucursal_fisica.realizar_compra(1,1,True)
    una_sucursal_fisica.realizar_compra(2,1,False)
    una_sucursal_fisica.realizar_compra(3,1,True)
    una_sucursal_fisica.realizar_compra(4,1,False)

    assert una_sucursal_fisica.ganancias_total_por_dia()==11760