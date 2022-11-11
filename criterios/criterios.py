class PorNombre:
    
    def __init__(self,expresion_del_nombre):

        self.expresion_del_nombre=f'/{expresion_del_nombre}'
    
    def corresponde_al_producto(self,producto):
        return producto.es_de_nombre(self.expresion_del_nombre)

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

class PorStock:
    
    def __init__(self, stock):
        self.stock = stock
    
    def corresponde_al_producto(self,producto):
        return producto.retornar_stock() < self.stock

class PorOposicion:

    def __init__(self,criterio):
        self.criterio=criterio
    
    def corresponde_al_producto(self,producto):
        return not self.criterio.corresponde_al_producto(producto)
