# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:14:10 2019

@author: Cristhian Salazar Jaramillo cc.1193522656
"""
#1)---------------------------------------
def Acumulado(l):
    
    nuevaLista = []
    nuevaLista.append(l[0])
    
    for i in range(len(l)):
        if(i+1 < len(l)):
            nuevaLista.append(nuevaLista[i] + l[i+1])
    
    return nuevaLista
    
    
lista = eval(input("Ingrese lista: "))
print(Acumulado(lista))

#2) ----------------------------------------
def ordenada(l):
 
    f = True
    for i in range(len(l)-1):
        if(l[i+1] <= l[i]):
            f = False
            break
    return(f)
    
lista = eval(input("Ingrese lista: "))
print(ordenada(lista))

#3)------------------------------------------
dic = eval(input("Ingrese diccionario: "))

if(dic["Marta"]%2 == 0):
    dic["Madre"] = dic["Marta"]*2
    
    if(dic["Madre"]%5 == 0):
        dic["Padre"] = dic["Juan"]*2
        print(dic)
    
    else:
        print(dic)

else:
    dic["Marcos"] = dic["Monica"]*3
    print(dic)
    
#4)------------------------------------------

N = eval(input("Ingrese diccionario: "))
M = eval(input("Ingrese diccionario: "))

datos = ['Nombre','Telefono', 'Cedula']

for k in datos:
    if(N.get(k) is None):
        print(k,"Dato no proporcionado")
    else:
        print(k, N[k])
        
        
for k in datos:
    if(M.get(k) is None):
        print(k,"Dato no proporcionado")
    else:
        print(k, M[k])
#5)--------------------------------------
    
N = eval(input("Ingrese un diccionario: "))
M = eval(input("Ingrese una lista: "))

acumulaM = 0
acumulaN = 0
for i in M:
    acumulaM += i

for key in N:
    acumulaN += N[key]

if(acumulaM == acumulaN):
    if(acumulaM > 100000):
        N.setdefault("Costo",100000)
        print(N)
    
    else:
        N.setdefault("CostoTotal",acumulaN)
        print(N)

else:
    N.setdefault("Lista",M)
    print(N)

#6)-----------------------------------------
T = (1,1,2,3,5,8,13,21,34)
n = eval(input("Ingrese numero: "))

print(T.count(n))

#7)-------------------------------------------
T = (1,1,2,3,5,8,13,21,34)

print("Mayor:  %d" % (max(T)))
print("Menor: %s" % (min(T)))

#8)-------------------------------------------
meses = (0,'enero','febrero','marzo','abril',
         'mayo','junio','julio','agosto',
         'septiembre','octubre','noviembre','diciembre')
f = True
while(f):
    n = int(input("Ingrese numero: "))
    
    if(n == 0):
        print("Fin del Programa")
        f = False
    
    else:
        if(n not in range(1,len(meses))):
            print ("Error! número fuera del rango.")

        else:
            print(meses[n])


#9)----------------------------------------------
import numpy as np

M = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
a = np.array([1,0,0]).reshape(1,3)
b = np.array([1,0,1,0,1]).reshape(5,1)


print("Dimension de M:")
print(M.shape)
print("Dimension de a:") 
print(a.shape)
print("Dimension de b:")
print(b.shape)

#10)-----------------------------------------------
import numpy as np

M = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
N = np.identity(3)

print("Suma:")
print(M+N)

print("Resta:")
print(M-N)

print("Multiplicacion:")
print(np.multiply(M,N))

print("Division:")
print(M/N)


#11)---------------------------------------------------
import numpy as np

c = np.array([1,0,1])
d = np.array([3,0,7])

print("Producto punto:")
print(np.dot(c,d))

print("Producto cruz:")
print(np.cross(c,d))

#12)---------------------------------------------------
import numpy as np

c = np.array([1,0,1])

print(np.linalg.norm(c))

#13)----------------------------------------------------
import math

for n in range(11):
    print("Factorial de %s: %d" % (n, math.factorial(n)))



#14)----------------------------------------------------
import math

def MCD(n1,n2):
    if(n1 < n2):
        return MCD(n2,n1)
    
    elif(n2==0):
        return n1
    else:
        return MCD(n2, math.fmod(n1,n2))
    
    
print("El máximo común divisor de  2380  y  1550 es %d" % (MCD(2380,1550)))
print("El máximo común divisor de  744 y 847 es %s" % (MCD(744,847)))
print("El máximo común divisor de  115238 y 10561 es %s" %  (MCD(115238,10561)))
    
    
#15)--------------------TERMINAR--------------------------------

p = 15
LF= []
LF.append(0)
LF.append(1)
i = 0    
while(p>0):
    LF.append(LF[i]+LF[i+1])
    i+=1
    p-=1
def primo(n):
    
    if n<2:
        return False
    elif n==2:
        return True
    
    for i in range(2,n,1):
        if(n%i == 0):
            return False
            break
    return True
        
l1 = []
for i in range(1,151,1):
    if(i not in LF):
        l1.append(i)

l2 = []
for e in range(len(l1)):
    if(not primo(l1[e])):
        l2.append(l1[e])
    
def afortunado(lista):
    temp = []
    for x in lista:
        if(lista.index(x)%2 != 0):
            temp.append(x)
    return temp
    
#    for y in range(len(temp)):
#        if(temp[y]%temp.index(y))
print(afortunado(l2))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









