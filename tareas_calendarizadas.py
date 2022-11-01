from MacoWins import *

from persistencia import *

for una_sucursal in cargar_todos():
    print(una_sucursal.productos())
    # una_sucursal.discontinuar_productos()
# if __name__=="__main__":
#     print("discontinuando productos")
#     print("------------------------------")
#     print(una_sucursal.productos())