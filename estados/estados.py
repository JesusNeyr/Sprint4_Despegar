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
