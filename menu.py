# -*- coding: iso-8859-15 -*-
from registroarticulos import *
from registroventas import *
import pickle
import os
while True:
    try:
        print
        print "           MENÚ PRINCIPAL"
        print
        print "1. Registro de datos de artículos"
        print "2. Venta de artículos"
        print "3. Salir"
        print
        op=input("Elija una opción <1-3>: ")
    except NameError:
        raw_input("Dato no válido. Pulse ENTER")
        continue
    except:
        raw_input("Ha ocurrido un error. Pulse ENTER")
        continue
    if op==1:
        while True:
            try:
                print
                print "       MENÚ DE DATOS DE ARTÍCULOS"
                print
                print "1. Agregar registros de Artículos"
                print "2. Modificar registros de Artículos"
                print "3. Borrar registros de Artículos"
                print "4. Consultar registros de Artículos"
                print "5. Regresar al menú principal"
                print
                opc=input("Elija una opción <1-5>: ")
            except NameError:
                raw_input("Dato no válido. Pulse ENTER")
                continue
            except:
                raw_input("Ha ocurrido un error. Pulse ENTER")
                continue
            if opc==1:
                agregararticulo()
            elif opc==2:
                modificararticulos()
            elif opc==3:
                borrararticulos()
            elif opc==4:
                listaarticulos()
            elif opc==5:
                break
            else:
                print
                raw_input("Opción no válida. Pulse ENTER para mostrar el menú")            
    elif op==2:
        while True:
            try:
                print
                print "      MENÚ DE VENTAS DE ARTÍCULOS"
                print
                print "1. Agregar registros de VENTAS"
                print "2. Modificar registros de VENTAS"
                print "3. Borrar registros de VENTAS"
                print "4. Consultar registros de VENTAS"
                print "5. Consultar registro de VENTA" 
                print "6. Regresar al menú principal"
                print
                opc=input("Elija una opción <1-5>: ")
            except NameError:
                raw_input("Dato no válido. Pulse ENTER")
                continue
            except:
                raw_input("Ha ocurrido un error. Pulse ENTER")
                continue
            if opc==1:
                agregarventa()
            elif opc==2:
                modificarventas()
            elif opc==3:
                borrarventas()
            elif opc==4:
                listarventas()
            elif opc==5:
                listarfactura()
            elif opc==6:
                break
            else:
                print
                raw_input("Opción no válida. Pulse ENTER para mostrar el menú")
    elif op==3:
        print
        raw_input("Salida del programa. Pulse ENTER")
        break
    else:
        print
        raw_input("Opción no válida. Pulse ENTER para mostrar el menú")

        
            
