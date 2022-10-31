from CONTROLADORES.DBFuture import DAO
dao= DAO()

def listarPropiedades(propiedad):
    print("\nPropiedades: \n")
    contador = 1
    for prop in propiedad:
        datos = "{0}. Id_Propiedad: {1} | Nombre: {2} |Direccion: {3} | Contacto: {4})"
        print(datos.format(contador, prop[0], prop[5], prop[6], prop[7]))
        contador = contador + 1
    print(" ")

def listarTiposPropiedades(tipo):
    print("\nTipos Propiedades: \n")    
    contador = 1
    for tip in tipo:
        datos = "{0}. Id_Tipo: {1} | Nombre_Tipo: {2})"
        print(datos.format(contador, tip[0], tip[1]))
        contador = contador + 1      
    print(" ")

def listarEstadosPropiedades(estado):
    print("\nEstados Propiedades: \n")    
    contador = 1
    for est in estado:
        datos = "{0}. Id_Estado: {1} | Nombre_Estado: {2})"
        print(datos.format(contador, est[0], est[1]))
        contador = contador + 1      
    print(" ")  

def listarPropietariosPropiedades(propietario):
    print("\nPropietarios Propiedades: \n")    
    contador = 1
    for pro in propietario:
        datos = "{0}. Id_Propietario: {1} | Nombre: {2})"
        print(datos.format(contador, pro[0], pro[1]))
        contador = contador + 1      
    print(" ")    

def listarOperatoriaComercialPropiedades(operatoriaComercial):
    print("\nOperatoria Comercial Propiedades: \n")    
    contador = 1
    for opc in operatoriaComercial:
        datos = "{0}. Id_OperatoriaComercial: {1} | Nombre_OperatoriaComercial: {2})"
        print(datos.format(contador, opc[0], opc[1]))
        contador = contador + 1      
    print(" ")           


# Metodo para armar insercion en tabla propiedades
def pedirDatosRegistro():

    tipoCorrecto = False
    while(not tipoCorrecto):
        tipo = dao.listarTipo()
        if len(tipo) > 0:
            listarTiposPropiedades(tipo)
            idTipo = int(input("Seleccione un tipo de propiedad: "))   
            if(idTipo<1 or idTipo > 6):
                print("Tipo de propiedad incorrecto: Debe ingresar una opcion numerica referida a los tipos de propiedad listados anteriormente.")
            else:
                tipoCorrecto = True
        else:
            print("No se encontraron Tipos de propiedades...")    
     
        

    estadossCorrecto = False
    while(not estadossCorrecto):
        estado = dao.listarEstado()
        if len(estado) > 0:
            listarEstadosPropiedades(estado)
            idestado = int(input("Seleccione un estado de propiedad: "))   
            if(idestado<1 or idestado > 4):
                print("Estado de propiedad incorrecto: Debe ingresar una opcion numerica referida a los estados de propiedad listados anteriormente.")
            else:
                estadossCorrecto = True
        else:
            print("No se encontraron Estados de propiedades...")  


    operatoriaCorrecto = False
    while(not operatoriaCorrecto):
        operatoria = dao.listarOperatoriaComercial()
        if len(operatoria) > 0:
            listarOperatoriaComercialPropiedades(operatoria)
            idoperatoria = int(input("Seleccione una OperatoriaComercial de propiedad: "))   
            if(idoperatoria<1 or idoperatoria > 5):
                print("OperatoriaComercial de propiedad incorrecto: Debe ingresar una opcion numerica referida a los estados de propiedad listados anteriormente.")
            else:
                operatoriaCorrecto = True
        else:
            print("No se encontraron Estados de propiedades...")          

    propietariosCorrecto = False
    while(not propietariosCorrecto):
        propietario = dao.listarPropietario()
        if len(propietario) > 0:
            listarPropietariosPropiedades(propietario)
            idpropietario = int(input("Seleccione un propietario de propiedad: "))   
            if(idpropietario<1 or idTipo > len(propietario)+1):
                print("propietario de propiedad incorrecto: Debe ingresar una opcion numerica referida a los estados de propiedad listados anteriormente.")
            else:
                propietariosCorrecto = True
        else:
            print("No se encontraron propietario de propiedades...")  

    nombreCorrecto = False
    while(not nombreCorrecto):       
        nombre = str(input("Ingrese Nombre de la propiedad: "))   
        if(nombre==""):
            print("Debe ingrsar un nombre para la propiedad.")
        else:
            nombreCorrecto = True

    direccionCorrecto = False
    while(not direccionCorrecto):       
        direccion = str(input("Ingrese direccion de la propiedad: "))   
        if(direccion==""):
            print("Debe ingrsar una direccion para la propiedad.")
        else:
            direccionCorrecto = True

    contactoCorrecto = False
    while(not contactoCorrecto):       
        contacto = str(input("Ingrese contacto de la propiedad: "))   
        if(contacto==""):
            print("Debe ingrsar un contacto para la propiedad.")
        else:
            contactoCorrecto = True               
      


    propiedad = (idTipo,idestado,idoperatoria,idpropietario,nombre,direccion,contacto)

    return propiedad     

# Metodo para armar modificacion en tabla propiedades
def modificarPropiedad(propiedades):
    propiedad=listarPropiedades(propiedades)
    existeIdprop = False  
    propi= None  
    while(not existeIdprop):   
        IdpropEditar = int(input("Ingrese el Id_Propiedad de la propiedad a modificar: "))
        for prop in propiedades:
            if prop[0] == IdpropEditar:
                existeIdprop = True
                propi= prop
                break
            else:
                print("Id_Propiedad no encontrado")   
    
    print(f"Propiedad a modificar:{propi[5]} {propi[6]} {propi[7]} ")            
    print("")            
    if existeIdprop:
        nombreCorrecto = False
        while(not nombreCorrecto):       
            nombre = str(input("Ingrese Nombre de la propiedad a editar: "))   
            if(nombre==""):
                print("Debe ingrsar un nombre para la propiedad.")
            else:
                nombreCorrecto = True

        direccionCorrecto = False
        while(not direccionCorrecto):       
            direccion = str(input("Ingrese direccion de la propiedad a editar: "))   
            if(direccion==""):
                print("Debe ingrsar una direccion para la propiedad.")
            else:
                direccionCorrecto = True

        contactoCorrecto = False
        while(not contactoCorrecto):       
            contacto = str(input("Ingrese contacto de la propiedad a editar: "))   
            if(contacto==""):
                print("Debe ingrsar un contacto para la propiedad.")
            else:
                contactoCorrecto = True               
      

        propiedad = ( nombre, direccion,contacto,IdpropEditar)
    else:
        propiedad = None

    return propiedad

def pedirDatosEliminacion(propiedades):
    propiedad=listarPropiedades(propiedades)
    existeIdprop = False  
    propi= None  
    while(not existeIdprop):   
        IdpropEditar = int(input("Ingrese el Id_Propiedad de la propiedad a eliminar: "))
        for prop in propiedades:
            if prop[0] == IdpropEditar:
                existeIdprop = True
                propi= prop
                break
            else:
                print("Id_Propiedad no encontrado") 
                
    print(f"Propiedad a eliminar:{propi[5]} {propi[6]} {propi[7]} ")              
    print("Desea confirmar la operacion...?") 
    print("- 1. SI")   
    print("- 2. NO")   
    opcion= int(input("Selecione una opcion: "))
    if opcion == 1:   
        return IdpropEditar
    else:
        return ""          

