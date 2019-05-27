# 1)

N = int(input("Ingrese un numero entero \n"))
M = int(input("Ingrese un numero entero \n"))
W = int(input("Ingrese un numero entero \n"))

l1 = []
l1.append(N)
l1.append(M)
l1.append(W)


l1.sort()

for e in l1:
    print(e)

# ---------------------------------------
# 2)


N = float(input("Ingrese un numero \n"))
V = 25
D = N*V

if(D > 350):
    print(round(D,2))
    
else:
    S = N+D
    print(round(S,2))
    
# ------------------------------------------   
# 3)
    
    
N = int(input("Ingrese un numero entero \n"))
s = 0

for i in range(1,N+1,1):
    s = s + i**3
    
print(s)

# ------------------------------------------
# 4)

N = int(input("Ingrese un numero entero \n"))
s = 1

for i in range(1,N+1,1):
    s = s * i**2
    
print(s)


#------------------------------------------
# 5)

m = eval(input("Ingrese una matriz \n"))
long = len(m[0])
dp = 0
ds = 0

for fila in range(0,long,1):
    for col in range (0,long,1):
        
        if (fila == col):
            dp = dp + m[fila][col]
            
        if (fila + col == long-1):
            ds = ds + m[fila][col]

print(ds+dp)

# ----------------------------------------
# 6)

N = input("Ingrese una palabra \n")

if (N[0].isupper()):
    print("Upper")

else:
    print("Lower")


#- -------------------------------------------
# 7)  TERMINAR!!!


N = int(input("Ingrese un numero entero \n"))
M = (25*N)/75
print(round(M,2))


# -------------------------------------------
# 8)


W = int(input("Ingrese un numero entero \n"))
N = int(input("Ingrese un numero entero \n"))
M = int(input("Ingrese un numero entero \n"))


p = (120*W*240)/(7*N*M)
print(round(p,1))


# ------------------------------------------
# 9)


l1= eval(input("Ingrese una lista \n"))
l2 = []
for i in l1:
    if(l1.count(i) == 1):
        l2.append(i)
        
    else:
        l2.append(i)
        l1.remove(i)
l2.sort()
print(l2)

# ---------------------------------------------
# 10) 


m = eval(input("Ingrese una matriz \n"))

long = len(m[0])
con = 0

for fila in range(0,long,1):
    for col in range (0,long,1):
        
        con += (m[fila][col])**2

con = con**(1/2)
print(round(con,2))


# ---------------------------------------------
# 11)


n1 = float(input("Ingrese un numero real \n"))
n2 = float(input("Ingrese un numero real \n"))

a = (n1*n2)/2
print(a)


#-----------------------------------------------
# 12)


m = eval(input("Ingrese una matriz \n"))

long = len(m[0])
dp = 1
ds = 1

for fila in range(0,long,1):
    for col in range (0,long,1):
        
        if (fila == col):
            dp = dp * m[fila][col]
            
        if (fila + col == long-1):
            ds = ds * m[fila][col]

r = dp*ds
print(r)


# ---------------------------------------------
# 13)


dic = eval(input("Ingrese un diccionario \n"))

if (dic["Marta"] % 2 == 0):
    dic["Madre"] = (dic["Marta"] * 2)

    if (dic["Madre"] % 5 == 0):
        dic["Padre"] = (dic["Juan"] * 2)
        print(dic)

    else:
        print(dic)
    
else:
    dic["Marcos"] = (dic["Monica"] * 3)
    print(dic)

# -----------------------------------------------
# 14) 
    

l1= eval(input("Ingrese una lista \n"))

l1.sort()

print(l1[0])
l1.remove(l1[0])

con = 0
for i in l1:
    con += i

final = con/len(l1)
print(round(final,1))

if (final >= 3):
    print("Pasa")
else:
    print("Repite")



# -----------------------------------------------
# 15)
    
    
m = eval(input("Ingrese una matriz \n"))
long = len(m[0])


for fila in range(0,long):
    l = []
    mayor = len(m[fila])-1
    
    m[fila].sort()
    l.append(m[fila][mayor])
    l.append(m[fila][0])
    

    print(l)      
        

# -------------------------------------------------
# 16
    
    
m = eval(input("Ingrese una matriz \n"))

long = len(m[0])
con = 0

for fila in range(0,long,1):
    for col in range (0,long,1):
        
        con += (m[fila][col])**2

con = con**(1/2)
print(round(con,2))

# -------------------------------------------------
# 17)


def Clima(lista):
    
    con= 0
    for t in lista:
        con += t
        
    prom = con/len(lista)
    
    if(prom > 25.6):
        print("Calor")

    else:
        print("Frio")

# -------------------------------------------------
# 18)
        
        
def Resultados(lista):
    
    l = []
    con = 0
    
    for r in lista:
        
        if (r == "G"):
            con += 3
            
        elif (r == "E"):
            con += 1
            
        else:
            con = con
            
    
    if(con < 12):
        l.append(con)
        l.append("Desciende")
        
        
    else:
        l.append(con)
        l.append("Permanece")


    print(l)


e = eval(input("Ingrese lista: "))
Resultados(e)

# ---------------------------------------------
# 19)


def Ventas(matriz):
    
    dias = len(matriz[0])
    semana = len(matriz)
    ventas = 0
    
    for fila in range(0,semana):
        for col in range(0,dias):
            
            ventas += matriz[fila][col]
        
    if (ventas > 100000):
        print(matriz[0])
        
    else:
        print(matriz[semana-1])
    
    
    
m = eval(input("matriz: "))
Ventas(m)
    
    
# -----------------------------------------------
# 20)


N = eval(input("Ingrese una lista \n"))
    
long = len(N)
    
if (long >= 4):
    s = N[0] + N[1]
    N.append(s)
    print(N)
else:
    
    N.reverse()
    print(N)
    
    
# ---------------------------------------------
# 21)
    

def Resta(m1, m2):
    
    if (len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
        print("No se pueden restar estas matrices")
    
    else:
        x = len(m1[0])
        y = len(m1)
        
        mr = m1
    
        for fila in range(0,y,1):
            for col in range (0,x,1):
                
                mr[fila][col] = m1[fila][col] - m2[fila][col] 
        
        print(mr)
    
m1 = eval(input("m1: "))
m2 = eval(input("m2: "))
    
Resta(m1,m2)
    
# ----------------------------------------------
# 22)

def Suma(m1, m2):
    
    if (len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
        print("No se pueden sumar estas matrices")
    
    else:
        x = len(m1[0])
        y = len(m1)
        
        mr = m1
    
        for fila in range(0,y,1):
            for col in range (0,x,1):
                
                mr[fila][col] = m1[fila][col] + m2[fila][col] 
        
        print(mr)
    
m1 = eval(input("m1: "))
m2 = eval(input("m2: "))
    
Suma(m1,m2)
    
# -------------------------------------------------
# 23)

n1 = int(input("Ingrese un numero entero \n"))
n2 = int(input("Ingrese un numero entero \n"))
    
def max_divisor(x,y):
    if (y==0):
       return x

    else:
        return max_divisor(y,x%y)
    
    
# ------------------------------------------------
# 24)

n1 = int(input("Ingrese un numero entero \n"))
n2 = int(input("Ingrese un numero entero \n"))
    

    
# ------------------------------------------------
# 25)
    
N = eval(input("Ingrese un diccionario \n"))
M = eval(input("Ingrese una lista \n"))
val = N.values()
contD = 0
contL = 0

for e in range(len(M)):
    contL += contL


for i in range(len(val)):
    contD += val[i]

if(contD == contL):
    

    if(con > 100000):
        N.setdefault("Costo",100000)
        print(N)
    
    else:
        N.setdefault("CostoTotal",contD)
        print(N)

else:
    N.setdefault("Lista",M)
    print(N)


# ------------------------------------------------
# 26)  

N = int(input("Ingrese un numero entero \n"))
M = int(input("Ingrese un numero entero \n"))

V = (N*M*792)/(12*6)
print(V)


# ------------------------------------------------
# 27)  

N = int(input("Ingrese un numero entero \n"))
M = int(input("Ingrese un numero entero \n"))

try:
    r = M/N
    
    
except ZeroDivisionError:
    print("No se puede dividir por cero")
    print(M)
    
else:
    print(round(r))


# ------------------------------------------------
# 28)  NO HAY TABLA

N = int(input("Ingrese un numero entero \n"))
M = int(input("Ingrese un numero entero \n"))



# ------------------------------------------------
# 29)

N = input("Ingrese un string \n")
M = input("Ingrese un string \n")
con = 0

for c in M:
    if(c == N):
        con += 1
        
if(con > 0):
    
    if(con % 2 == 0):
        Mt = M.replace(N,"5")
    
    else:
        Mt = M.replace(N,str(con))
        
    print(Mt)
    
else:
    print(M[::-1])


# ----------------------------------------





























