from producto.producto import *
from estados.estados import *
from criterios.criterios import *


def test_creando_producto():

    remera=Producto("remera","sport",1,2300)

    assert remera.codigo==1
    assert remera.nombre=="remera"
    assert remera.categoria==["sport"]
    assert remera.precio_base==2300
    assert remera.retornar_estado()

def test_consultar_precio():

    remera=Producto("remera","sport",1,2300)

    assert remera.retornar_precio()==2300

def test_cambiar_estado_a_liquidacion():
    remera=Producto("remera","sport",1,2300)
    remera.cambiar_estado(Liquidacion())
    assert remera.precio()==1150

def test_cambiar_estado_a_promocion():
    remera=Producto("remera","sport",1,2300)
    remera.cambiar_estado(Promocion(300))
    assert remera.precio()==2000

def test_calcular_precio_final_extranjero_igual_a_false():
    
    remera=Producto("remera","sport",1,2300)
    

    assert remera.calcular_precio_final(False) == 2783

def test_calcular_precio_final_extranjero_igual_a_true():
    
    remera=Producto("remera","sport",1,2300)

    assert  remera.calcular_precio_final(True) == 2300

def test_actualizar_precio_final_por_porcentaje():
    remera=Producto("remera","sport",1,2300)
    remera.actualizar_precio_por_porcentaje(100)
    assert remera.precio_base==4600

def test_pertenece_al_criterio_nombre_true():

    remera=Producto("remera","sport",1,2300)

    expresion_del_nombre= "remera" 

    assert remera.es_de_nombre(f'{expresion_del_nombre}')==True

def test_pertenece_al_criterio_nombre_false():

    remera=Producto("remera","sport",1,2300)

    expresion_del_nombre= "remera90" 

    assert remera.es_de_nombre(f'{expresion_del_nombre}')==False

def test_agregar_categoria():
    remera=Producto("remera","sport",1,2300)
    remera.agregar_categoria("casual")
    assert len(remera.categoria)==2

def test_consultar_categoria_existente():
    remera=Producto("remera","sport",1,2300)

    assert remera.consultar_categoria("sport")==True

def test_consultar_categoria_inexistente():
    remera=Producto("remera","sport",1,2300)

    assert remera.consultar_categoria("casual")==False

def test_consultar_categoria_existente_en_lista_de_categorias():
    remera=Producto("remera","sport",1,2300)
    remera.agregar_categoria("casual")
    remera.agregar_categoria("verano")
    assert remera.consultar_categoria("casual")==True

def test_consultar_categoria_inexistente_en_lista_de_categorias():
    remera=Producto("remera","sport",1,2300)
    remera.agregar_categoria("casual")
    remera.agregar_categoria("verano")
    assert remera.consultar_categoria("Formal")==False

def test_comprobar_stock_igual_a_cero():
    remera=Producto("remera","sport",1,2300)
    assert remera.stock==0

def test_recargar_stock():
    remera=Producto("remera","sport",1,2300)
    remera.recargar_stock(30)
    assert remera.stock==30