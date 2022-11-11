from estados.estados import *
import re
class Producto:
    def __init__(self, nombre, categoria, codigo, precio_base):
        self.nombre = nombre
        self.categoria = [categoria]
        self.codigo = codigo
        self.precio_base = precio_base
        self.stock=0
        self.estado = Nueva()


    def retornar_codigo(self):

        return self.codigo

    def retornar_precio(self):
        return self.precio_base

    def retornar_stock(self):

        return self.stock
        
    def retornar_estado(self):
        return self.estado  

    def precio(self):
        return self.estado.precio(self.precio_base)

    def cambiar_estado(self, estado):
        self.estado = estado

    def calcular_precio_final(self,es_extranjero):
        if self.precio() > 70 and es_extranjero:
            
            return self.precio()
        
        else:
            
            return self.precio() + (self.precio() * 0.21)

    def actualizar_precio_por_porcentaje(self,porcentaje):
        self.precio_base +=self.retornar_precio()*porcentaje/100
    
    def es_de_nombre(self,expresion_del_nombre):

        if re.search(expresion_del_nombre,self.nombre):

            return True
        else:
            return False

    def consultar_categoria(self,consultar_categoria):
        es_de_categoria=False
        for categoria in self.categoria:
            if categoria.lower() == consultar_categoria.lower():
                es_de_categoria=True
        if es_de_categoria==True:
            return True
        return es_de_categoria
    
    def agregar_categoria(self,nueva_categoria):
        self.categoria.append(nueva_categoria)

    def recargar_stock(self,cantidad):
        
        self.stock = self.stock + int(cantidad)