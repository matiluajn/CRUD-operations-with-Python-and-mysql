# Programa main.py sistema de gestion inmobiliaria
# Issue : 9 - Alfredo Palacios

from distutils.log import error
from CONTROLADORES.DBFuture import DAO
from os import system
from CONTROLADORES import funciones
import time


def menuPrincipal(): 
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print ("***********************************************************************")
            print ("*                       - Inmobiliaria - Future -                     *")
            print ("***********************************************************************")
            print ("*                    Sistema de Gestión Inmobiliaria                  *")
            print ("***********************************************************************")
            print ("")                                                                    
            print ("- 1. Ingresar una nueva propiedad ")                                    
            print ("- 2. Modificar datos de prpopiedad            ")                          
            print ("- 3. Eliminar datos de  propiedad             ")                      
            print ("- 4. Listar todas las propiedades              ")                         
            print ("- 5. Listar propiedades disponibles para la venta  ")                      
            print ("- 6. Listar propiedades disponibles para alquiler   ")                 
            print ("- 7. Listar propiedades vendidas                    ")                    
            print ("- 8. Listar propiedades alquiladas                   ")                   
            print (" ")                                                                    
            print ("- 9. Salir  ")                                                           
            print (" ")                                                                 
            print ("***********************************************************************")
            
            try:
                opcion = int(input("Seleccione una opción : "))
            except ValueError:
                continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                system("cls")
                continue
            if opcion < 1 or opcion > 9:
                continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                system("cls")
                continue
            elif opcion == 9:
                continuar = False
                print("\nGracias por usar nuestro sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)
    
def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:  
        try:
            oPropiedad=funciones.pedirDatosRegistro()            
            dao.registrarPropiedad(oPropiedad)   
            print("Propiedad registrada con exito...")
            time.sleep(3)
            menuPrincipal()
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))

    elif opcion == 2:
        try:
            prop = dao.listarPropiedades()
            if len(prop) > 0:
                propi = funciones.modificarPropiedad(prop)
                if propi:
                    dao.modificarPropiedad(propi)
                    print("Propiedad Modificada con exito...")
                    time.sleep(3)
                    print("")
                    menuPrincipal()
                else:
                    print("Propiedad a actualizar no encontrada...\n")
            else:
                print("No se encontraron PROPIEDADES...")
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))

    elif opcion == 3:
        try:
            prop = dao.listarPropiedades()
            if len(prop) > 0:
                Id_Propiedad = funciones.pedirDatosEliminacion(prop)
                if not(Id_Propiedad == ""):
                    dao.eliminarPropiedad(Id_Propiedad)
                    print("Propiedad Eliminada con exito...")
                    time.sleep(3)
                    print("")
                    menuPrincipal()
                else:
                    print("Propiedad a eliminar no encontrada.....\n")
            else:
                print("No se encontraron PROPIEDADES...")
                time.sleep(3)
        except error as ex:
            print("Ocurrió un error...".format(ex))
            
    elif opcion == 4:
        try:
            propiedad = dao.listarPropiedades()
            if len(propiedad) > 0:
                funciones.listarPropiedades(propiedad)
                time.sleep(3)
            else:
                print("No se encontraron PROPIEDADES...")  
                time.sleep(3)         
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))

    elif opcion == 5:
        try:
            propiedad = dao.listarPropiedadesDPV()
            if len(propiedad) > 0:
                funciones.listarPropiedades(propiedad)
            else:
                print("No se encontraron PROPIEDADES...")  
                time.sleep(3)         
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))
    elif opcion == 6:
        try:
            propiedad = dao.listarPropiedadesDPA()
            if len(propiedad) > 0:
                funciones.listarPropiedades(propiedad)
                time.sleep(3)
            else:
                print("No se encontraron PROPIEDADES...")   
                time.sleep(3)        
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))
    elif opcion == 7:
        try:
            propiedad = dao.listarPropiedadesVendidas()
            if len(propiedad) > 0:
                funciones.listarPropiedades(propiedad)
                time.sleep(3)
            else:
                print("No se encontraron PROPIEDADES...") 
                time.sleep(3)          
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))    
 
    elif opcion == 8:
        try:
            propiedad = dao.listarPropiedadesAlquiladas()
            if len(propiedad) > 0:
                funciones.listarPropiedades(propiedad)
                time.sleep(3)
            else:
                print("No se encontraron PROPIEDADES...")   
                time.sleep(3)        
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))
    else:
        print ("Opcion no valida...")


# def cargarDatosPropiedad():
#        print("Elija un tipo de propiedad")       

menuPrincipal()
