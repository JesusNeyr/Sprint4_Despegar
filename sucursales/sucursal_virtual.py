from sucursales.sucursal import *


class Sucursalvirtual(Sucursal):
    def __init__(self) :
        self.productos = []
        self.ventas = [] 
        self.gastos_fijo_por_dia = 0

    def cantidad_de_ventas_del_dia(self):

        ventas_del_dia=0

        for venta in self.ventas:
            if dia in venta["fecha"]:
                ventas_del_dia +=venta["cantidad"]
        return ventas_del_dia

    def gastos_por_dia(self):
        
        if self.cantidad_de_ventas_del_dia() > 100:
            return self.cantidad_de_ventas_del_dia() * self.gastos_fijo_por_dia
        else:
            return self.gastos_fijo_por_dia

    def ganancias_total_por_dia(self):
        return self.valor_ventas_del_dia() - self.gastos_por_dia()

    def asignar_valor_gastos_fijo_por_dia(self,valor):
        self.gastos_fijo_por_dia = valor