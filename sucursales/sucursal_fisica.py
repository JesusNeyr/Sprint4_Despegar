from sucursales.sucursal import *

class SucursalFisica(Sucursal):
    def __init__(self):
        self.productos = []
        self.ventas = [] 
        self.valor_fijo_diario = 500

    def ganancias_total_por_dia(self):
        if self.valor_ventas_del_dia()>=self.valor_fijo_diario:

            return self.valor_ventas_del_dia() - self.valor_fijo_diario
        else:
            raise ValueError("El valor de las ventas del dia son menores al gasto por dia")