"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv
import readline

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.replace("\t",",") for linea in datos]
        datos = [linea.split(",") for linea in datos]
        
    columna2 = [int(elemento) for linea in datos for elemento in linea[1]]
    return sum(columna2)

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.replace("\t",",") for linea in datos]
        datos = [linea.split(",") for linea in datos]

    lista_letras = [letra for linea in datos for letra in linea[0]]
    lista_tuplas = []
    x=[]
    for i in lista_letras:
        if i not in x:
            x.append(i)
    for i in sorted(x):
        conteo = lista_letras.count(i)
        tupla=(i,conteo)
        lista_tuplas.append(tupla) 
        
    return lista_tuplas

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.replace("\t",",") for linea in datos]
        datos = [linea.split(",") for linea in datos]

    lista_letras = [letra for linea in datos for letra in linea[0]]
    lista_numeros = [numero for linea in datos for numero in linea[1]]
    lista = list(zip(lista_letras,lista_numeros))
    diccionario = {}

    for key, value in lista:
        if key in diccionario:
            diccionario[key]+= int(value)
        else:
            diccionario[key]=int(value)
    resultado = [(key, diccionario[key]) for key in diccionario]
    
    return (sorted(resultado))

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.replace("\t",",") for linea in datos]
        datos = [linea.split(",") for linea in datos]

    fechas =[linea[2] for linea in datos]
    meses = [mes.split("-")[1] for mes in fechas]
    x=[]
    lista_tuplas=[]
    for i in meses:
        if i not in x:
            x.append(i)
    for i in sorted(x):
        conteo = meses.count(i)
        tupla=(i,conteo)
        lista_tuplas.append(tupla)         
        
    return (lista_tuplas)

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.replace("\t",",") for linea in datos]
        datos = [linea.split(",") for linea in datos]

    lista_letras = [letra for linea in datos for letra in linea[0]]
    lista_numeros = [numero for linea in datos for numero in linea[1]]
    lista = list(zip(lista_letras,lista_numeros))

    diccionario={}

    for key, value in lista:
        if key in diccionario:
            diccionario[key]+= [int(value)]
        else:
            diccionario[key]= [int(value)]
    resultado = [(key, diccionario[key]) for key in diccionario]
    resultado = sorted(resultado)

    lista_tuplas = []
    for key, value in resultado:
        tupla=(key, max(value), min(value))
        lista_tuplas.append(tupla)

    return lista_tuplas

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.split("\t") for linea in datos]

    dic={}
    columna5=[lista[4] for lista in datos]
    l=[elemento.split(",") for elemento in columna5]
    final=sorted([tuple(j.split(":")) for i in l for j in i])
    
    for key, value in final:
        if key not in dic:
            dic[key]=[int(value)]
        else:
            dic[key]+=[int(value)]
        
    resultado = [(key, min(dic[key]), max(dic[key])) for key in dic]

    return resultado
    
def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.split("\t") for linea in datos]
    
    diccionario={}

    columna_numeros =[int(numero) for linea in datos for numero in linea[1]]
    columna_letras =[letra for linea in datos for letra in linea[0]]

    nuevo = list(zip(columna_numeros, columna_letras))

    for key, value in nuevo:
        if key not in diccionario:
            diccionario[key]=[value]
        else:
            diccionario[key]+=[value]

    return sorted(diccionario.items())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    
    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.split("\t") for linea in datos]
    
    diccionario={}

    columna_numeros =[int(numero) for linea in datos for numero in linea[1]]
    columna_letras =[letra for linea in datos for letra in linea[0]]

    nuevo = list(zip(columna_numeros, columna_letras))

    for key, value in nuevo:
        if key not in diccionario:
            diccionario[key]=[value]
        else:
            diccionario[key]+=[value]

    resultado=[]
    for i,j in sorted(diccionario.items()):
        resultado.append((i, sorted(list(set(j)))))

    return resultado
    
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.split("\t") for linea in datos]

    dic={}
    columna5=[lista[4] for lista in datos]
    l=[elemento.split(",") for elemento in columna5]
    final=sorted([tuple(j.split(":")) for i in l for j in i])
    claves=[elemento[0] for elemento in final]
    lista=sorted(list(set(claves)))

    for clave in lista:
        dic[clave]=claves.count(clave)

    return dic
    

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.split("\t") for linea in datos]

    lista_tuplas=[(lista[0], len(lista[3].split(",")), len(lista[4].split(","))) for lista in datos]

    return lista_tuplas

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.split("\t") for linea in datos]
    
    dic = {}
    for lista in datos:
        l = lista[3].split(",")
        for i in l:
            if i not in dic:
                dic[i]=int(lista[1])
            else:
                dic[i]+=int(lista[1])

    return (dict(sorted(dic.items())))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv") as fichero_csv:
        datos = fichero_csv.readlines()
        datos = [linea.replace("\n","") for linea in datos]
        datos = [linea.split("\t") for linea in datos]
    
    dic = {}
    resultado=[]
    for linea in datos:
        l = linea[4].split(",")
        for i in l:
            x = i.split(":")
            y = (linea[0], int(x[1]))
            resultado.append(y)
    
    for letra in resultado:
        if letra[0] not in dic:
            dic[letra[0]] = int(letra[1])
        else:
            dic[letra[0]]+= int(letra[1])

    return dict(sorted(dic.items()))