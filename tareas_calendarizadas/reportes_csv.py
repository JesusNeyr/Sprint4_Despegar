from asyncore import write
import csv
from MacoWins import *
from persistencia.persistencia import *
fecha_anio_actual=date.strftime(date.today(), "%Y")
dia =date.strftime(date.today(), "%Y-%m-%d")
sucursales_guardadas=cargar_todos()

lista_de_sucursales=[]

for una_sucursal in sucursales_guardadas.values():
   lista_de_sucursales.append(una_sucursal)


if __name__=="__main__":
    
    with open('reportes.csv','w',newline='') as file:

        writer=csv.writer(file,delimiter=";")
        writer.writerow(["Fecha",  " ventas al dia", " monto de las ventas"])
        
        for sucursal in lista_de_sucursales:
            dia_actual=dia
            ventas_del_dia=len(sucursal.ventas)
            monto_de_las_ventas_del_dia=sucursal.valor_ventas_del_dia()
            rows=[str(dia_actual), str(ventas_del_dia),str(monto_de_las_ventas_del_dia)]
           
            writer.writerow(rows)


      