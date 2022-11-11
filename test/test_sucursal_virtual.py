from sucursales.sucursal_virtual import *
from producto.producto import *
import pytest

def reiniciar_lista_de_productos(sucursal):
    sucursal.productos.clear()

def test_cantidad_ventas_del_dia_sin_ventas():
    una_sucursal_virtual=Sucursalvirtual()

    reiniciar_lista_de_productos(una_sucursal_virtual)

    remera=Producto("remera","sport",1,2000)
    pantalon=Producto("pantalon","sport",2,2500)
    short=Producto("short","sport",3,3000)
    saco=Producto("saco","formal",4,3500)
    una_sucursal_virtual.registrar_producto(remera)
    una_sucursal_virtual.registrar_producto(pantalon)
    una_sucursal_virtual.registrar_producto(short)
    una_sucursal_virtual.registrar_producto(saco)

    assert una_sucursal_virtual.cantidad_de_ventas_del_dia()==0

def test_cantidad_ventas_del_dia_con_ventas():
    una_sucursal_virtual=Sucursalvirtual()

    reiniciar_lista_de_productos(una_sucursal_virtual)

    remera=Producto("remera","sport",1,2000)
    pantalon=Producto("pantalon","sport",2,2500)
    short=Producto("short","sport",3,3000)
    saco=Producto("saco","formal",4,3500)
    una_sucursal_virtual.registrar_producto(remera)
    una_sucursal_virtual.registrar_producto(pantalon)
    una_sucursal_virtual.registrar_producto(short)
    una_sucursal_virtual.registrar_producto(saco)
    una_sucursal_virtual.recargar_stock(1,40)
    una_sucursal_virtual.recargar_stock(2,50)
    una_sucursal_virtual.recargar_stock(3,60)
    una_sucursal_virtual.recargar_stock(4,70)
    una_sucursal_virtual.realizar_compra(1,1,True)
    una_sucursal_virtual.realizar_compra(2,1,False)
    una_sucursal_virtual.realizar_compra(3,1,True)
    una_sucursal_virtual.realizar_compra(4,4,False)

    assert una_sucursal_virtual.cantidad_de_ventas_del_dia()==7

def test_gastos_por_dia_con_gasto_fijo_en_0():
    una_sucursal_virtual=Sucursalvirtual()

    reiniciar_lista_de_productos(una_sucursal_virtual)

    remera=Producto("remera","sport",1,2000)
    pantalon=Producto("pantalon","sport",2,2500)
    short=Producto("short","sport",3,3000)
    saco=Producto("saco","formal",4,3500)
    una_sucursal_virtual.registrar_producto(remera)
    una_sucursal_virtual.registrar_producto(pantalon)
    una_sucursal_virtual.registrar_producto(short)
    una_sucursal_virtual.registrar_producto(saco)
    una_sucursal_virtual.recargar_stock(1,40)
    una_sucursal_virtual.recargar_stock(2,50)
    una_sucursal_virtual.recargar_stock(3,60)
    una_sucursal_virtual.recargar_stock(4,70)
    una_sucursal_virtual.realizar_compra(1,20,True)
    una_sucursal_virtual.realizar_compra(2,20,False)
    una_sucursal_virtual.realizar_compra(3,20,True)
    una_sucursal_virtual.realizar_compra(4,20,False)

    una_sucursal_virtual.asignar_valor_gastos_fijo_por_dia(0)
    assert una_sucursal_virtual.gastos_por_dia()==0

def test_gastos_por_dia_con_gasto_fijo_en_100_y_ventas_mayores_a_100():
    una_sucursal_virtual=Sucursalvirtual()

    reiniciar_lista_de_productos(una_sucursal_virtual)

    remera=Producto("remera","sport",1,2000)
    pantalon=Producto("pantalon","sport",2,2500)
    short=Producto("short","sport",3,3000)
    saco=Producto("saco","formal",4,3500)
    una_sucursal_virtual.registrar_producto(remera)
    una_sucursal_virtual.registrar_producto(pantalon)
    una_sucursal_virtual.registrar_producto(short)
    una_sucursal_virtual.registrar_producto(saco)
    una_sucursal_virtual.recargar_stock(1,40)
    una_sucursal_virtual.recargar_stock(2,50)
    una_sucursal_virtual.recargar_stock(3,60)
    una_sucursal_virtual.recargar_stock(4,70)
    una_sucursal_virtual.realizar_compra(1,30,True)
    una_sucursal_virtual.realizar_compra(2,20,False)
    una_sucursal_virtual.realizar_compra(3,40,True)
    una_sucursal_virtual.realizar_compra(4,20,False)

    una_sucursal_virtual.asignar_valor_gastos_fijo_por_dia(100)
    assert una_sucursal_virtual.gastos_por_dia()==11000
    
def test_gastos_por_dia_con_gasto_fijo_en_100_y_ventas_menores_a_100():
    una_sucursal_virtual=Sucursalvirtual()

    reiniciar_lista_de_productos(una_sucursal_virtual)

    remera=Producto("remera","sport",1,2000)
    pantalon=Producto("pantalon","sport",2,2500)
    short=Producto("short","sport",3,3000)
    saco=Producto("saco","formal",4,3500)
    una_sucursal_virtual.registrar_producto(remera)
    una_sucursal_virtual.registrar_producto(pantalon)
    una_sucursal_virtual.registrar_producto(short)
    una_sucursal_virtual.registrar_producto(saco)
    una_sucursal_virtual.recargar_stock(1,40)
    una_sucursal_virtual.recargar_stock(2,50)
    una_sucursal_virtual.recargar_stock(3,60)
    una_sucursal_virtual.recargar_stock(4,70)
    una_sucursal_virtual.realizar_compra(1,20,True)
    una_sucursal_virtual.realizar_compra(2,20,False)
    una_sucursal_virtual.realizar_compra(3,20,True)
    una_sucursal_virtual.realizar_compra(4,20,False)

    una_sucursal_virtual.asignar_valor_gastos_fijo_por_dia(100)
    assert una_sucursal_virtual.gastos_por_dia()==100

def test_ganancia_total_por_dia_con_ventas_mayores_a_100():

    una_sucursal_virtual=Sucursalvirtual()

    reiniciar_lista_de_productos(una_sucursal_virtual)

    remera=Producto("remera","sport",1,2000)
    pantalon=Producto("pantalon","sport",2,2500)
    short=Producto("short","sport",3,3000)
    saco=Producto("saco","formal",4,3500)
    una_sucursal_virtual.registrar_producto(remera)
    una_sucursal_virtual.registrar_producto(pantalon)
    una_sucursal_virtual.registrar_producto(short)
    una_sucursal_virtual.registrar_producto(saco)
    una_sucursal_virtual.recargar_stock(1,40)
    una_sucursal_virtual.recargar_stock(2,50)
    una_sucursal_virtual.recargar_stock(3,60)
    una_sucursal_virtual.recargar_stock(4,70)
    una_sucursal_virtual.realizar_compra(1,30,True)
    una_sucursal_virtual.realizar_compra(2,20,False)
    una_sucursal_virtual.realizar_compra(3,40,True)
    una_sucursal_virtual.realizar_compra(4,20,False)

    una_sucursal_virtual.asignar_valor_gastos_fijo_por_dia(100)
    assert una_sucursal_virtual.ganancias_total_por_dia()== 314200