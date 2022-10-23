# -*- coding: iso-8859-15 -*-
print "REGISTRO DE VENTAS DE COMPUTADORAS Y SUS ACCESORIOS"
import pickle; import os
from validaciones import *
from abrirguardar import *
articulos=[] #SE DECLARA UNA LISTA VACÍA
articulos=abrir("articulos.dat") 
def agregararticulo():
    codigo=nombre=" "
    while True:
        try:
            codigo=raw_input("Ingrese el código del producto o ENTER para salir: ") #PIDE EL CÓDIGO DEL ARTÍCULO EL CUAL POSTERIORMENTE ES VERIFICADO PARA QUE NO SE REPITA
            if codigo=="":
                break
            codigo=int(codigo) 
            encontrado=False
            for i in range(len(articulos)): #SE RECORRE LA MATRIZ ARTÍCULOS PARA VERIFICAR QUE EL CÓDIGO SEA ÚNICO
                if articulos[i][0]==codigo:
                    encontrado=True
                    raw_input("El CÓDIGO ingresado ya existe. Pulse ENTER")
            if not encontrado:
                while True:
                    try: 
                        print
                        nombre=raw_input("Ingrese el nombre del artículo: ")
                        costo=float(raw_input("Ingrese el costo de %s: "%nombre))
                        articulos.append([codigo,nombre,costo]) #GUARDA LOS REGISTROS EN LA MATRIZ ARTÍCULOS
                        break
                    except ValueError:
                        print "Los datos son incorrectos. Vuelva a intentarlo."
                        print
                    except:
                        print "Ha ocurrido un error"
                        print
        except ValueError:
            print "Los datos son incorrectos. Vuelva a intentarlo."
            print
        except:
            print "Ha ocurrido un error"
            print
    if len(articulos)>0:   
        pickle.dump(articulos,open("articulos.dat","w")) #SE GUARDA LA MATRIZ EN UN ARCHIVO CON EL NOMBRE ARTÍCULOS
        print "Archivo guardado."
#######################################################    
def listaarticulos():
    totalc=0
    print
    print "CÓDIGO   DESCRIPCIÓN DEL ARTÍCULO        COSTO"
    for i in range(len(articulos)):
        codigo=articulos[i][0]
        n=articulos[i][1]
        costo=articulos[i][2]
        totalc=totalc+costo
        print "%2d      "%(articulos[i][0]),articulos[i][1].ljust(25),
        print "      $%8.2f "%(costo)
    print"                                        ___________"
    print "                             TOTALES:    $%8.2f"%(totalc)
    print
    raw_input("Pulse ENTER para volver al menú")
#######################################################
def modificararticulos():
    codigo=" "
    while True:
        try: #CAPTURA CUALQUIER ERROR POSIBLE
            codigo=raw_input("Ingrese el CODIGO del artículo a MODIFICAR o ENTER para salir: ") #PIDE EL CÓDIGO DE UN REGISTRO
            if codigo=="":
                break
            codigo=int(codigo) #CONVIERTE LOS CARACTERES A ENTEROS
            encontrado=False
            for i in range(len(articulos)): #SE RECORRE LA MATRIZ ARTÍCULOS EN BUSCA DEL CÓDIGO SOLICITADO
                if articulos[i][0]==codigo:
                    encontrado=True
                    print
                    print "EL REGISTRO A MODIFICAR ES: "
                    print
                    print "CÓDIGO   DESCRIPCIÓN DEL ARTÍCULO        COSTO"
                    print "%2d      "%(articulos[i][0]),articulos[i][1].ljust(25),
                    print "      $%8.2f "%(articulos[i][2])
                    print
                    while True:
                        try:
                            nombre=raw_input("Modifique el nombre del artículo o ENTER para salir: ")
                            if nombre!="":
                                articulos[i][1]=nombre
                            costo=raw_input("Modifique el costo del artículo o ENTER para salir: ")
                            if costo!="":
                                articulos[i][2]=float(costo)
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
                    print "%2d      "%(articulos[i][0]),articulos[i][1].ljust(25),
                    print "      $%8.2f "%(articulos[i][2])
                    print
                    pickle.dump(articulos,open("articulos.dat","w"))
            if not encontrado:
                print
                raw_input("EL REGISTRO SOLICITADO NO FUE ENCONTRADO. Pulse ENTER.")
        except ValueError:
            print "Los datos son incorrectos. Vuelva a intentarlo"
            print
        except:
            print "Ha ocurrido un error"
#######################################################
def borrararticulos():
    codigo=sn=" "
    while True:
        try:
            codigo=raw_input("Ingrese el CÓDIGO del registro a BORRAR o ENTER para salir: ")
            if codigo=="":
                break
            codigo=int(codigo)
            encontrado=False
            for i in range (len(articulos)):
                if articulos[i][0]==codigo:
                    encontrado=True
                    print
                    print "EL REGISTRO A BORRAR ES: "
                    print
                    print "CÓDIGO   DESCRIPCIÓN DEL ARTÍCULO        COSTO"
                    print "%2d      "%(articulos[i][0]),articulos[i][1].ljust(25),
                    print "      $%8.2f "%(articulos[i][2])
                    print
                    sn=raw_input("¿ESTÁ SEGURO DE BORRAR ESTE REGISTRO S/N?: ")
                    if sn.lower()=="s":
                        articulos.pop(i)
                        pickle.dump(articulos,open("articulos.dat","w"))
                        raw_input("Registro borrado. Pulse ENTER")
                        break
            if not encontrado:
                print
                raw_input("EL REGISTRO SOLICITADO NO FUE ENCONTRADO. Pulse ENTER")
        except ValueError:
             print "Los datos son incorrectos. Vuelva a intentarlo"
             print
        except:
            print "Ha ocurrido un error"
            print
                
                    
                
                
    
            

                

    
           

           
    
           

        
                
