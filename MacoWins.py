from ast import Raise
from datetime import date
from operator import itemgetter
import re

fecha_anio_actual=date.strftime(date.today(), "%Y")
dia =date.strftime(date.today(), "%Y-%m-%d")



class Producto:
    def __init__(self, nombre, categoria, codigo, precio_base):
        self.nombre = nombre
        self.categoria = [categoria]
        self.codigo = codigo
        self.precio_base = precio_base
        self.stock=0
        self.estado = Nueva()

    def precio(self):
        return self.estado.precio(self.precio_base)

    def cambiar_estado(self, estado):
        self.estado = estado

    def retornar_codigo(self):

        return self.codigo

    def retornar_precio(self):
        return self.precio_base

    def retornar_stock(self):

        return self.stock

    def calcular_precio_final(self,es_extranjero):
        if self.precio() > 70 and es_extranjero:
            
            return self.precio()
        
        else:
            
            return self.precio() + (self.precio() * 0.21)

    def actualizar_precio_por_porcentaje(self,porcentaje):
        self.precio_base +=self.precio_base*porcentaje/100
    
    def es_de_nombre(self,expresion_del_nombre):

        return re.search(expresion_del_nombre,self.nombre)

    def consultar_categoria(self,consultar_categoria):
        for categoria in self.categoria:
            if categoria.lower()== consultar_categoria.lower():
                return True
            else:
                return False
    
    def agregar_categoria(self,nueva_categoria):
        self.categoria.append(nueva_categoria)

    def recargar_stock(self,cantidad):
        
        self.stock = self.stock + int(cantidad)
class PorNombre:
    def __init__(self,expresion_del_nombre):
        self.expresion_del_nombre=f'{expresion_del_nombre}+[\s]?[a-zA-Z]?+'
    def corresponde_al_producto(self,producto):
        return producto.es_de_nombre(self.expresion_del_nombre.split())
class PorCategoria:
    def __init__(self,categoria):
        self.categoria=categoria
    def corresponde_al_producto(self,producto):
        return producto.consultar_categoria(self.categoria)

class PorPrecio:
    def __init__(self, precio):
        self.precio = precio
    def corresponde_al_producto(self,producto):
        return producto.retornar_precio() < self.precio



class Sucursal:
    
    def codigos_productos(self):
        codigos=[]
        if len(self.productos)==0:       
            codigos=[]
        else:
            [codigos.append(producto.codigo) for producto in self.productos if  producto.codigo and type(producto.codigo)==int and producto.codigo>0]
        return codigos
    
    def codigos_ordenados_decreciente_de_productos(self):
        return sorted(self.codigos_productos(),reverse=True)
    
    def lista_de_codigos_ventas(self):   
        codigos=[]
        if len(self.ventas)>0:
        
            [codigos.append(venta.codigo_producto) for venta in self.ventas]
            
        else:
            
            codigos=[]
        
        return codigos

    def codigo_de_producto_solicitado_en_productos(self,codigo):
        
        return codigo in self.codigos_productos()

    def posicion_de_codigo_en_productos(self,codigo_de_producto):

        if self.codigo_de_producto_solicitado_en_productos(codigo_de_producto):
                    return self.codigos_productos().index(codigo_de_producto)
        else:
            raise ValueError("Lo sentimos el producto consultado, no existe")

    def buscar_producto(self,codigo_de_producto):
        if self.codigo_de_producto_solicitado_en_productos(codigo_de_producto):
            for producto in self.productos:
                if codigo_de_producto ==producto.codigo:
                            return producto
        else:
            raise ValueError("No se encontro el producto")

    def registrar_producto(self,producto_nuevo):
     
        if len(self.productos)==0:
            self.productos.append(producto_nuevo)
        else:
       
            if (producto_nuevo.retornar_codigo() in self.codigos_productos()) :

                raise ValueError("producto registrado")

            else:
                
                self.productos.append(producto_nuevo)
            
    def recargar_stock(self,codigo_de_producto, cantidad):
    
        for producto in self.productos:
        
            if self.codigo_de_producto_solicitado_en_productos(codigo_de_producto):
            
                if producto.codigo == codigo_de_producto:
                
                    producto.recargar_stock(cantidad)
                
            else:
            
                raise ValueError("No se encuentra el producto")

    def hay_stock(self,codigo_de_producto):

        lista_de_codigos=self.codigos_productos()
    
        
        
        if self.codigo_de_producto_solicitado_en_productos(codigo_de_producto):
                    posicion= lista_de_codigos.index(codigo_de_producto)
            
        if codigo_de_producto in lista_de_codigos:

            return self.productos[posicion].codigo == codigo_de_producto and self.productos[posicion].stock > 0
    
    def mostrar(self):
        for i in self.productos:
            print(f'nombre del producto {i.nombre}, stock = {i.stock},codigo = {i.codigo},precio={i.precio_base}')
    
    def calcular_precio_final(self,codigo,es_extranjero):

        producto_encontrado=self.buscar_producto(codigo)

        return producto_encontrado.calcular_precio_final(es_extranjero)
    
    def agregar_categoria(self,codigo,categoria):

        for producto in self.productos:
            if producto.codigo==codigo:
                producto.agregar_categoria(categoria)
    


    def contar_categorias(self):
        
        categorias_unicas=[]

        for producto in self.productos:
            
            for categoria in producto.categoria:
                
                if categoria not in categorias_unicas:

                    categorias_unicas.append(categoria)

        return len(categorias_unicas)

    def realizar_venta(self,producto_vendido,cantidad,es_extranjero):
        
        if producto_vendido.stock>0 and producto_vendido.codigo>0:
            self.ventas.append( {
                
                        "codigo_producto": producto_vendido.codigo,
                        "cantidad": cantidad,       
                        "fecha": date.strftime(date.today(), "%Y-%m-%d"),
                        "precio": self.calcular_precio_final(producto_vendido.codigo,es_extranjero) * cantidad
                        })        
        
    def realizar_compra(self,codigo_de_producto, cantidad,es_extranjero):
        
        posicion=self.posicion_de_codigo_en_productos(codigo_de_producto)
        
        if self.hay_stock(codigo_de_producto) and cantidad <= self.productos[posicion].retornar_stock():
            
                self.productos[posicion].recargar_stock(cantidad)
                
                self.realizar_venta(self.productos[posicion],cantidad,es_extranjero)
                
        else:
                raise ValueError("No hay stock Disponible, cantidad dispoble de " + str(self.productos[posicion].stock))
        
    def discontinuar_productos(self):

        self.productos=[producto for producto in self.productos if producto.stock>0]
    
    def valor_ventas_del_dia(self):
    
        suma_ventas = 0
        
        for venta in self.ventas:
            
            if venta["fecha"]== dia:
                
                suma_ventas += venta["precio"]
                
        return suma_ventas

    def ventas_del_anio(self):

        lista_de_ventas_del_anio = []

        for venta in self.ventas:
            
            if venta["fecha"][0:4] == fecha_anio_actual:
                
                lista_de_ventas_del_anio.append(venta)
                
        return lista_de_ventas_del_anio

    def cantidad_de_codigo_con_ventas(self,codigos_ordenados_de_productos_decre):
        
        cantidad_repetida_de_codigo_vendidos={}
        
        for codigo in codigos_ordenados_de_productos_decre:
            
            for venta in self.ventas:
                
                if codigo == venta["codigo_producto"]:
                    
                    if codigo in cantidad_repetida_de_codigo_vendidos:
                        
                        cantidad_repetida_de_codigo_vendidos[codigo] += venta["cantidad"]
                        
                    else:
                        
                        cantidad_repetida_de_codigo_vendidos[codigo] = venta["cantidad"]
                        
        return cantidad_repetida_de_codigo_vendidos

    def codigos_ordenados_de_las_ventas(self):

        codigos_ordenados_de_productos_decre=self.codigos_ordenados_decreciente_de_productos()
        
        cantidad_repetida_de_codigo_vendidos= self.cantidad_de_codigo_con_ventas(codigos_ordenados_de_productos_decre)

        lista_ordenada = sorted(cantidad_repetida_de_codigo_vendidos.items(), key=itemgetter(1),reverse=True)

        return lista_ordenada

    def productos_mas_vendidos_ordenados(self,codigos_ordenados_por_ventas):
        
        nombre_productos = []
        

        for codigo in codigos_ordenados_por_ventas:
            
            for producto in self.productos:
                
                if codigo[0] == producto.codigo:
                    
                    nombre_productos.append(producto.nombre)
                    
        return nombre_productos

    def productos_mas_vendidos(self,hasta = -1):
               
        if len(self.ventas) <= hasta:
            
            raise ValueError("cantidad solicitada excedida")

        codigos_ordenados_por_ventas=self.codigos_ordenados_de_las_ventas()

        nombre_productos=self.productos_mas_vendidos_ordenados(codigos_ordenados_por_ventas)
        
        if hasta!=-1:
            return nombre_productos[:hasta]
        else:
            return nombre_productos

    def actualizar_precio_segun(self,criterio,porcentaje):
        for producto in self.productos:
            if criterio.corresponde_al_producto(producto):
                producto.actualizar_precio_por_porcentaje(porcentaje)

    

   
class Sucursalvirtual(Sucursal):
    def __init__(self) :
        self.productos = []
        self.ventas = [] 
        self.gastos_fijo_por_dia = 0

    def cantidad_de_ventas_del_dia(self):
        self.ventas
        ventas_por_dia= [venta for venta in self.ventas if dia in venta["fecha"]]
        return len(ventas_por_dia)

    def gastos_por_dia(self):
        if self.cantidad_de_ventas_del_dia() > 100:
            return self.cantidad_de_ventas_del_dia() * self.gastos_fijo_por_dia
        else:
            return self.gastos_fijo_por_dia

    def ganancias_total_por_dia(self):
        return self.valor_ventas_del_dia() - self.gastos_por_dia()

    def asignar_valor_gastos_fijo_por_dia(self,valor):
        self.gastos_fijo_por_dia = valor

class Sucursalfisica(Sucursal):
    def __init__(self):
        self.productos = []
        self.ventas = [] 
        self.valor_fijo_diario = 500

def ganancias_total_por_dia(self):
        return self.valor_ventas_del_dia() - self.valor_fijo_diario



class Nueva:
    def precio(self, precio_base):
        return precio_base

class Liquidacion:
    def precio(self, precio_base):
        return precio_base / 2

class Promocion:
    def __init__(self, valor_fijo):
        self.valor_fijo = valor_fijo

    def precio(self, precio_base):
        return precio_base - self.valor_fijo

