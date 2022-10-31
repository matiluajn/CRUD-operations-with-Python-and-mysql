# Programa DBFuture.py - conexion base de datos
# Issue : 10 - Alfredo Palacios

#from multiprocessing import connection
from distutils.log import error
import mysql.connector
from mysql.connector import Error

#from CLASES.Propietario import Propietario

class DAO():
    def __init__(self):
        try:
            self.connection=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',  #'',
                db='future'
            )            
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))

    def listarPropiedades(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM propiedad ORDER BY Nombre ASC")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")

    def listarPropiedadesDPV(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM propiedad WHERE Id_Estado =1 AND Id_OperatoriaComercial = 1 ORDER BY Nombre ASC")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")
            
    def listarPropiedadesDPA(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM propiedad WHERE Id_Estado = 2 AND Id_OperatoriaComercial = 1 ORDER BY Nombre ASC")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")      
    
    def listarPropiedadesVendidas(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM propiedad WHERE  Id_OperatoriaComercial = 2 ORDER BY Nombre ASC")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")  
            
    def listarPropiedadesAlquiladas(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM propiedad WHERE  Id_OperatoriaComercial = 3 ORDER BY Nombre ASC")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")                   
    
    def listarTipo(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM tipo")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")       

    def listarEstado(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM estado")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")  

    def listarPropietario(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM propietario")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")       

    def listarOperatoriaComercial(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM operatoriacomercial")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")                  

    def registrarPropiedad(self, Propiedad):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO propiedad (Id_Tipo, Id_Estado, Id_OperatoriaComercial,Id_Propietario,Nombre,Direccion,Contacto) VALUES ('{0}', '{1}', '{2}','{3}','{4}','{5}','{6}')"
                cursor.execute(sql.format(Propiedad[0], Propiedad[1], Propiedad[2],Propiedad[3],Propiedad[4],Propiedad[5],Propiedad[6]))
                self.connection.commit()
                print("CARGANDO...\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))        


    def modificarPropiedad(self, propiedad):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE propiedad SET Nombre = '{0}', Direccion = '{1}',Contacto = '{2}' WHERE Id_Propiedad = {3}"
                cursor.execute(sql.format(propiedad[0], propiedad[1], propiedad[2],propiedad[3]))
                self.connection.commit()
                print("CARGANDO...\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                
    def eliminarPropiedad(self, Id_Propiedad):        
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM propiedad WHERE Id_Propiedad = '{0}'"
                cursor.execute(sql.format(Id_Propiedad))
                self.connection.commit()
                print("CARGANDO...\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))            


        



