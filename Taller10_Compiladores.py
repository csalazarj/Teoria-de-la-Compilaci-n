'''

Analizador sintáctico (parser) básico, no reconoce paréntesis, solo operaciones básicas.

@author: Fernan Alonso Villa - Universidad Nacional de Colombia

@integrantes_grupo:
    Estudiante 1:
    Estudiante 2:
        
'''

import re

#Definimos para los tokens 
'''
Para Token tipo literal
'''
class Literal_Token:
    def __init__(self, value):
        self.value = value
    def getParte(self):
        return self.value

'''
Token tipo operador

Tradicionalmente se denota como "nud" --> "getParte", para obtener un elemento
literal o para representar la notación prefija, por ejemplo -4. 

Mientras que "getOperacion" --> "getOperacion", para la denotación infija , 
cuando el token de operador aparece dentro de la frase.

El valor de "peso" permite controlar la precedencia del operador; 
cuanto mayor sea el valor, más precedencia tendrá el operador
'''

class Operador_Suma_Token:
    peso = 10
    def getParte(self):
        return expresion(100)
    def getOperacion(self, parte):
        return parte + expresion(10)

class Operador_Resta_Token:
    peso = 10
    def getParte(self):
        return -expresion(100)
    def getOperacion(self, parte):
        return parte - expresion(10)

class Operador_Multiplicacion_Token:
    peso = 20
    def getOperacion(self, parte):
        return parte * expresion(20)

class operador_Division_Token:
    peso = 20
    def getOperacion(self, parte):
        return parte / expresion(20)

class Operador_Potencia_Token:
    peso = 30
    def getOperacion(self, parte):
        return parte ** expresion(30-1)
    
class Operador_Modulo_Token:
    peso = 40
    def getOperacion(self,parte):
        return parte % expresion(40)
    
class Operador_DivisonEntera_Token:
    peso = 30
    def getOperacion(self,parte):
        return parte // expresion(30)
    
class Operador_RaizEnesima_Token:
    peso = 30
    def getOperacion(self,parte):
        return parte**(1/expresion(30))
    
class Operador_MenorQue_Token():
    peso = 5
    def getOperacion(self,parte):
        return parte < expresion(5)

class Fin_Token:
    peso = 0

#separar los tokens conforme a la expresión regular
def tokenize(programa):
    # Separa los componentes si la expresion es 3 + 4, 
    # Se descompone en [('3', ''), ('', '+'), ('4', '')]
    for numero, operador in re.findall("\s*(?:(\d+\.?\d*)|(\*\*|\%|//|$|<|.))", programa):
        if numero:
            if '.' not in numero:
                yield Literal_Token(int(numero))
            else:
                yield Literal_Token(float(numero))
        elif operador == "+":
            yield Operador_Suma_Token()
        elif operador == "-":
            yield Operador_Resta_Token()
        elif operador == "*":
            yield Operador_Multiplicacion_Token()
        elif operador == "/":
            yield operador_Division_Token()
        elif operador == "**":
            yield Operador_Potencia_Token()
        elif operador == "%":
            yield Operador_Modulo_Token()
        elif  operador == "//":
            yield Operador_DivisonEntera_Token()
        elif  operador == "$":
            yield Operador_RaizEnesima_Token()
        elif  operador == ">":
            yield Operador_MenorQue_Token()
        else:
            raise SyntaxError("Error en '{0}' Operador Desconocido!!!: '{1}'".format(programa, operador))
    yield Fin_Token()

'''
El analizador debe verificar (sgt_peso < token.peso) tiene menos peso con el fin de
resolver la expresión y continuar con el siguiente token
'''
def expresion(sgt_peso=0):
    try:   
        global token
        t = token
        token = next()
        parte = t.getParte()
        while sgt_peso < token.peso:
            t = token
            token = next()
            parte = t.getOperacion(parte)
        return parte
    except AttributeError as err:
        raise SyntaxError('Ha ocurrido un error Sintaxis no Válida, atributo desconocido')
        
def parse(programa):
    global token, next
    next = tokenize(programa).__next__
    token = next()
    print (programa, " es ", expresion())

if __name__ == '__main__':
    
    try: 
        parse('-10**-2')
        parse("3.1**4")
        parse("+1")        
        parse("1")
        parse("+1")
        parse("-1")
        #Prueba error de Operador Desconocido una vez lanzada la excepcion 
        #se suspende evidentemente la ejecución de las demás lineas        
        #parse("1#2")
        #parse("2^2^3")
        parse("1+2+3")
        parse("1+2*3")
        parse("1*2/3")
        #Error de Sintaxis no válida
        #parse("*1") 
        parse("22--1")
        parse("22+*5")
        parse("10%9")
        parse("19//10")
        parse("10$10")
        parse("10<20")
        
    except SyntaxError as err:
        print(err)
