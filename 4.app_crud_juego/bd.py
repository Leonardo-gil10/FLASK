#Realizamos la importacion de la libreria con pip install pymysql
import pymysql

#configuramos los datosde conexion con la base de datos 

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user = 'root',
                                password='',
                                db='app_crud_juego')