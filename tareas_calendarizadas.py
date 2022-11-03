from MacoWins import *

from persistencia import *

# alamacenar_datos_de_una_sucursal("sucursal_virtual",una_sucursal_virtual)
alamacenar_datos_de_una_sucursal("sucursal_fisica",una_sucursal_fisica)

sucursales_guardadas=cargar_todos()

lista_de_sucursales=[]

for una_sucursal in sucursales_guardadas.values():
   lista_de_sucursales.append(una_sucursal)

if __name__=="__main__":
    print("discontinuando productos")
    for sucursal in lista_de_sucursales:
        sucursal.discontinuar_productos()   