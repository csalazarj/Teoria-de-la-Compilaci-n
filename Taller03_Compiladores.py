import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from datetime import datetime, date 
from urllib.request import urlopen
from bs4 import BeautifulSoup

#1)----------------------------------------------------------------------------------------------------------------------------------

url1 = "https://www.grupoaval.com/wps/portal/grupo-aval/aval/portal-financiero/renta-variable/acciones-bolsa-colombia/datos-historicos"
html1 = urlopen(url1)
#print(html)

soup = BeautifulSoup(html1, 'lxml')

datos = soup.find_all("span",{"id": re.compile(r"\bviewns_Z7_8162H3G0K8RBE0AS52COFE0U64\w*\b")})
str_datos = []
for dato in datos:
    str_cells = str(dato)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    str_datos.append(cleantext)

str_datos = str_datos[7:]
#print(str_datos)

nombres = soup.find_all("a")
#print(nombres)
str_nombres = []
for nombre in nombres:
    str_cells = str(nombre)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    str_nombres.append(cleantext)

str_nombres = str_nombres[156:225]
#print(str_nombres)


mat = []
copia_datos = str_datos
for nombre in str_nombres:
    fila = [nombre]
    lb = []
    
    for dato in copia_datos:
        if(dato != '%'):
            fila.append(dato)
            lb.append(dato)     
            
        else:
            break
    
    for e in fila:
        if(e in lb):
            copia_datos.remove(e)
    copia_datos.remove('%')
            
    mat.append(fila)

#print(mat)


accionMax = 0
empresaA = ''
maxVaria = 0
empresaV = ''
fecha_antigua = datetime.strptime(mat[0][1],'%d/%m/%y')
fecha_reciente = datetime.strptime(mat[0][1],'%d/%m/%y')
lista_varia = []

for fila in range(len(mat)):
    
    str_accion = mat[fila][3]
    accion = []
    for n in str_accion:
        if (n != ','):
            accion.append(n)
            
    num_accion = ''.join(accion)
    num_accion = float(num_accion)
    if(num_accion > accionMax):
        accionMax = num_accion
        empresaA = mat[fila][0]
        
       
    num_varia = float(mat[fila][4])
    lista_varia.append(num_varia) 
    if(abs(num_varia) > maxVaria):
        maxVaria = abs(num_varia)
        empresaV = mat[fila][0]
        num_real = num_varia
        
        
    fecha = datetime.strptime(mat[fila][1],'%d/%m/%y')
    if(fecha < fecha_antigua):
        fecha_antigua = fecha
        fecha_salida = mat[fila][1]
        
    if(fecha > fecha_reciente):
        fecha_reciente = fecha
        fecha_salida2 = mat[fila][1]
        
        
prom_varia = round((sum(lista_varia)/len(lista_varia)),2)

print("Empresa con la acción de mayor valor: {}".format(empresaA))
print("Empresa con la mayor varianza: {} con un {}% de variación ".format(empresaV,num_real))
print("Fecha de actualización más antigua: {}".format(fecha_salida))
print("Fecha de actualización más reciente: {}".format(fecha_salida2))
print("Promedio de variación: {}%".format(prom_varia))



#2)--------------------------------------------------------------------------------------------------------

url2 = "http://www.imesaza.es/informacion-tecnica/tabla-aceros/"
html2 = urlopen(url2)
#print(html)

soup = BeautifulSoup(html2, 'lxml')

tablas = soup.find_all("tbody")
str_tablas = []

for tabla in tablas:
    str_tablas.append(tabla)


rows = soup.find_all("tr")
for tabla in str_tablas:
    









