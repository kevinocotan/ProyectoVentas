# -*- coding: iso-8859-15 -*-
#print "REGISTRO DE VENTAS DE COMPUTADORAS Y SUS ACCESORIOS"
import pickle; import os
from validaciones import *
from abrirguardar import *
from registroarticulos import *
ventas=[] #SE DECLARA UNA LISTA VACÍA 
ventas=abrir("ventas.dat")
def agregarventa():
    factura=codigo=" "
    while True:
        try:
            print
            factura=raw_input("Ingrese la factura del producto o ENTER para salir: ") #SOLICITA EL INGRESO DE UNA FACTURA LA CUAL DEBE SER ÚNICA
            if factura=="":
                break
            encontrado=False
            for i in range(len(ventas)): #RECORRE LA MATRIZ VENTAS 
                if ventas[i][0]==factura: #VERIFICA SI LA FACTURA INGRESADA EXISTE
                    encontrado=True
                    raw_input("La FACTURA ingresada ya existe. PULSE ENTER")
            if not encontrado: #EN CASO DE QUE NO SE REPITA CONTINÚA LA EJECUCIÓN
                while True:
                    try:
                        codigo=raw_input("Ingrese el código del artículo o ENTER para salir: ") #PIDE UN CÓDIGO EL CUAL DEBE ESTAR RESGISTRADO EN EL ARCHIVO ARTÍCULOS
                        if codigo=="":
                            break
                        codigo=int(codigo)
                        encontrado2=False
                        for i in range(len(articulos)): #RECORRE LA MATRIZ ARTÍCULOS Y MUESTRA EL REGISTRO QUE HA SIDO REGISTRADO CON EL CÓDIGO ANTES INGRESADO
                            if articulos[i][0]==codigo:
                                encontrado2=True
                                print
                                print "CÓDIGO   DESCRIPCIÓN DEL ARTÍCULO"
                                print "%2d      "%(articulos[i][0]),articulos[i][1].ljust(25),
                                print
                                while True:
                                    try:
                                        print
                                        cantidad=input("Ingrese la cantidad del artículo: ")
                                        precio=float(raw_input("Ingrese el precio de venta del artículo: "))
                                        ventas.append([factura,codigo,cantidad,precio]) #GUARDA LOS REGISTROS EN LA MATRIZ VENTAS
                                        break
                                    except ValueError:
                                        print "Los datos son incorrectos. Vuelva a intentarlo."
                                        print
                                    except:
                                        print "Ha ocurrido un error"
                                        print
                        if not encontrado2:
                            print
                            raw_input("EL REGISTRO SOLICITADO NO FUE ENCONTRADO. Pulse ENTER")
                    except ValueError:
                        print "Los datos son incorrectos. Vuelva a intentarlo"
                        print
                    except:
                        print "Ha ocurrido un error"
                        print
        except:
            print "Ha ocurrido un error"
            print
    if len(ventas)>0:   
        pickle.dump(ventas,open("ventas.dat","w")) #SE GUARDA LA MATRIZ VENTAS EN UN ARCHIVO CON EL NOMBRE VENTAS
        print "Archivo guardado."
#######################################################    
def listarventas():
    totalc=totalp=total=totalb=inv=invt=totalu=u=0
    print
    print "CÓDIGO   DESCRIPCIÓN DEL ARTÍCULO  CANTIDAD    COSTO     PRECIO     TOTAL   INVERSIÓN   UTILIDAD"
    for i in range(len(articulos)): #SE RECORRE LA MATRIZ ARTÍCULOS
        #totalc=totalc+(articulos[i][2])
        for j in range(len(ventas)): #SE RECORRE LA MATRIZ VENTAS
            if ventas[j][1]==articulos[i][0]: #COMPARA EL CÓDIGO DE LA VENTA DEL ARTÍCULO PARA MOSTRAR TODAS LAS VENTAS QUE SE HAN REALIZADO SOBRE UN ARTÍCULO
                totalc=totalc+(articulos[i][2])
                inv=ventas[j][2]*articulos[i][2]
                total=ventas[j][2]*ventas[j][3]
                totalp=totalp+total
                totalb=totalb+(ventas[j][3])
                u=total-inv
                invt=invt+inv
                totalu=totalu+u
                print "%3d      "%(articulos[i][0]),articulos[i][1].ljust(20),
                print "     %3d"%(ventas[j][2]),
                print "   $%8.2f "%(articulos[i][2]),
                print "$%8.2f"%(ventas[j][3])," $%8.2f"%total," $%8.2f"%inv," $%8.2f"%u
    print "_________________________________________________________________________________________________"
    print "                             TOTALES:      $%8.2f  $%8.2f  $%8.2f  $%8.2f  $%8.2f"%(totalc,totalb,totalp,invt,totalu)
    print
    raw_input("Pulse ENTER para volver al menú")
#######################################################
def listarfactura():
    factura=" "
    total=0
    while True:
        factura=raw_input("Ingrese la FACTURA del registro que desea solicitar o ENTER para salir: ")
        if factura=="":
            break
        encontrado=False
        for i in range(len(ventas)):
            if ventas[i][0]==factura:
                encontrado=True
                print
                print "FACTURA    CÓDIGO    DESCRIPCIÓN DEL ARTÍCULO    CANTIDAD     PRECIO      TOTAL"
                for j in range(len(articulos)):
                    if articulos[j][0]==ventas[i][1]:
                        total=ventas[i][2]*ventas[i][3]
                        print ventas[i][0].ljust(10),"%3d      "%(articulos[j][0]),
                        print articulos[j][1].ljust(15),
                        print "             %3d"%(ventas[i][2]),
                        print "     $%8.2f"%(ventas[i][3])," $%8.2f "%total
                print
                raw_input("Pulse ENTER")
                break
        if not encontrado:
            print
            raw_input("EL REGISTRO SOLICITADO NO FUE ENCONTRADO. Pulse ENTER")
                        
#######################################################
def modificarventas():
    factura=" "
    while True:
        factura=raw_input("Ingrese la FACTURA del artículo a MODIFICAR o ENTER para salir: ") #SE PIDE LA FACTURA CON LA CUAL SE HA REGISTRADO UNA VENTA
        if factura=="":
            break
        encontrado=False
        for i in range(len(ventas)): #SE RECORRE LA MATRIZ VENTAS EN BUSCA DE LA EXISTENCIA DE LA FACTURA ANTES INGRESADA
            if ventas[i][0]==factura:
                encontrado=True
                print
                print "EL REGISTRO A MODIFICAR ES: "
                print
                print "FACTURA    CÓDIGO    DESCRIPCIÓN DEL ARTÍCULO    CANTIDAD     PRECIO"
                for j in range(len(articulos)):
                    if articulos[j][0]==ventas[i][1]:

                        print ventas[i][0].ljust(10),"%3d      "%(articulos[j][0]),
                        print articulos[j][1].ljust(15),
                        print "             %3d"%(ventas[i][2]),
                        print "     $%8.2f "%(ventas[i][3])
                        print
                        while True:
                            try:
                                cantidad=raw_input("Modifique la cantidad a vender o ENTER para salir: ")
                                if cantidad!="":
                                    ventas[i][2]=int(cantidad)
                                precio=raw_input("Modifique el precio de venta o ENTER para salir: ")
                                if precio!="":
                                    ventas[i][3]=float(precio)
                                break
                            except ValueError:
                                print "Los datos son incorrectos. Vuelva a intentarlo."
                                print
                            except:
                                print "Ha ocurrido un error"
                                print
                        print
                        print "VERIFICAR LOS DATOS ACTUALIZADOS: "
                        print
                        print ventas[i][0].ljust(10),"%3d      "%(articulos[j][0]),
                        print articulos[j][1].ljust(15),
                        print "             %3d"%(ventas[i][2]),
                        print "     $%8.2f "%(ventas[i][3])
                        print
                        pickle.dump(ventas,open("ventas.dat","w")) #SE GUARDAN LOS CAMBIOS
        if not encontrado:
            print
            raw_input("EL REGISTRO SOLICITADO NO FUE ENCONTRADO. Pulse ENTER.")
#######################################################
def borrarventas():
    factura=sn=" "
    while True:
        factura=raw_input("Ingrese la FACTURA del registro a BORRAR o ENTER para salir: ") #PIDE LA FACTURA DE UN REGISTRO, LA CUAL DEBE EXISTIR
        if factura=="":
            break
        encontrado=False
        for i in range (len(ventas)): #RECORRE LA MATRIZ VENTAS BUSCANDO LA FACTURA SOLICITADA
            if ventas[i][0]==factura: #VERIFICA LA EXISTENCIA DE LA FACTURA Y AL ENCONTARLA MUESTRA EL REGISTRO
                encontrado=True
                print
                print "EL REGISTRO A BORRAR ES: "
                print
                print "FACTURA    CÓDIGO    DESCRIPCIÓN DEL ARTÍCULO    CANTIDAD     PRECIO"
                for j in range (len(articulos)):
                    if articulos[j][0]==ventas[i][1]:
                        print ventas[i][0].ljust(10),"%3d      "%(articulos[j][0]),
                        print articulos[j][1].ljust(15),
                        print "             %3d"%(ventas[i][2]),
                        print "     $%8.2f "%(ventas[i][3])
                        print
                sn=raw_input("¿ESTÁ SEGURO DE BORRAR ESTE REGISTRO S/N: ")
                if sn.lower()=="s":
                    ventas.pop(i)
                    pickle.dump(ventas,open("ventas.dat","w")) #ELIMINA EL REGISTRO 
                    raw_input("Registro borrado. Pulse ENTER")
                    break
        if not encontrado:
            print
            raw_input("EL REGISTRO SOLICITADO NO FUE ENCONTRADO. Pulse ENTER")
                
                
                    
                
                
    
            

                

    
           

           
    
           

        
                
