def esnumero(x):
    j=0;b=""
    a=str(x)
    if a!="":
        if a[0]=="-" or a[0]=="+":
            a=a[1:]
        for i in a:
            if i==".":
                j=j+1
            else:
                b=b+i
        print b
        if j<=1 and b.isdigit():
            return True
        else:
            return False
    else:
        return False
############################    
def entero(x):
    while True:
        if x.isdigit():
            return int(x)
        else:
            x=raw_input("No es un entero positivo ...Vuelva a intentarlo:")
###############################
def real(x):
    a=x
    while True:
        c=0
        for i in range(len(a)):
            if a[i].isdigit():
                bandera=0
            else:
                if a[i]==".":
                    bandera=0
                    c=c+1
                else:
                    bandera=1
        if bandera==1 or c>=2:
            a=raw_input("No es un real positivo...Vuelva a intentarlo:")
        else:
            return round(float(a),2)
###############################
def entero2(x):
    j=0;b=""
    a=str(x)
    if a!="":
        if a[0]=="-" or a[0]=="+":
            b=b+a[0]
            a=a[1:]
        for i in a:
            if i==".":
                j=j+1
                if j<=1:
                    b=b+i
            else:
                if i.isdigit():
                    b=b+i
                else:
                    print "formato de numero desconocido"
                    return x
        if j<=1:
            print b
            return int(round(float(b)))
        else:
            print "No es un numero"
            return x
    else:
        print "No es un numero"
        return x    

def real2(x):
    j=0;b=""
    a=str(x)
    if a!="":
        if a[0]=="-" or a[0]=="+":
            b=b+a[0]
            a=a[1:]
        for i in a:
            if i==".":
                j=j+1
                if j<=1:
                    b=b+i
            else:
                if i.isdigit():
                    b=b+i
                else:
                    print "Formato de numero desconocido"
                    return x
        if j<=1:
            print b
            return float(b)
        else:
            print "No es un numero"
            return x
    else:
        print "No es un numero"
        return x  
###############################
def esentero(x):
    while True:
        #print x,
        #a=raw_input()
        if x.isdigit():
            return True
        else:
            return False
            #print
            #print "Debe digitar un nnmero entero...revisar los datos"
            #print
########################
def esreal(x):
    j=0;b=""
    a=str(x)
    if a!="":
        if a[0]=="-" or a[0]=="+":
            b=b+a[0]
            a=a[1:]
        for i in a:
            if i==".":
                j=j+1
                if j<=1:
                    b=b+i
            else:
                if i.isdigit():
                    b=b+i
                else:
                    print "Formato de numero desconocido"
                    return x
        if j<=1:
            print b
            return float(b)
        else:
            print "No es un numero"
            return x
    else:
        print "No es un numero"
        return x  
###############################
#print
#salario=real(raw_input("Digite el salario del empleado:"))
#print salario
#if entero(a):
#    print "ES NUMERO ENTERO"
#else:
#    print "NO ES NUMERO"

