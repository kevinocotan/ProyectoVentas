# -*- coding: iso-8859-15 -*-
import pickle; import os # Importar las librerias pickle y os
def abrir(ar): #Declarar la funcion abrir, recibe el parámetro ar (archivo)
    m=[] #Declarar una lista vacia
    if os.path.exists(ar): # ar, es una variable que contiene el nombre del archivo
        m=pickle.load(open(ar))
        raw_input("EL ARCHIVO %s EXISTE.  PULSE ENTER"%ar)
        return m
    else:
        raw_input("EL ARCHIVO %s NO EXISTE. PULSE ENTER"%ar)
        return m

def guardar(matrix,ar):
    pickle.dump(matrix,open(ar,"w"))
    raw_input("LOS DATOS SE HAN GUARDADO EN EL ARCHIVO %s PULSE ENTER"%ar)
