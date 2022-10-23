# -*- coding: iso-8859-15 -*-
from registroarticulos import *
from registroventas import *
import pickle
import os
while True:
    try:
        print
        print "           MEN� PRINCIPAL"
        print
        print "1. Registro de datos de art�culos"
        print "2. Venta de art�culos"
        print "3. Salir"
        print
        op=input("Elija una opci�n <1-3>: ")
    except NameError:
        raw_input("Dato no v�lido. Pulse ENTER")
        continue
    except:
        raw_input("Ha ocurrido un error. Pulse ENTER")
        continue
    if op==1:
        while True:
            try:
                print
                print "       MEN� DE DATOS DE ART�CULOS"
                print
                print "1. Agregar registros de Art�culos"
                print "2. Modificar registros de Art�culos"
                print "3. Borrar registros de Art�culos"
                print "4. Consultar registros de Art�culos"
                print "5. Regresar al men� principal"
                print
                opc=input("Elija una opci�n <1-5>: ")
            except NameError:
                raw_input("Dato no v�lido. Pulse ENTER")
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
                raw_input("Opci�n no v�lida. Pulse ENTER para mostrar el men�")            
    elif op==2:
        while True:
            try:
                print
                print "      MEN� DE VENTAS DE ART�CULOS"
                print
                print "1. Agregar registros de VENTAS"
                print "2. Modificar registros de VENTAS"
                print "3. Borrar registros de VENTAS"
                print "4. Consultar registros de VENTAS"
                print "5. Consultar registro de VENTA" 
                print "6. Regresar al men� principal"
                print
                opc=input("Elija una opci�n <1-5>: ")
            except NameError:
                raw_input("Dato no v�lido. Pulse ENTER")
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
                raw_input("Opci�n no v�lida. Pulse ENTER para mostrar el men�")
    elif op==3:
        print
        raw_input("Salida del programa. Pulse ENTER")
        break
    else:
        print
        raw_input("Opci�n no v�lida. Pulse ENTER para mostrar el men�")

        
            
