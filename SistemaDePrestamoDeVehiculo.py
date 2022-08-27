import mysql.connector

class create:
    def _init_(self):
        self.crear_bd()
        self.vehiculo()
    def crear_bd(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456"
        )
        self.cursor = self.conexion.cursor()
        try:
            self.cursor.execute('CREATE DATABASE nombre de la base de datos')
        except mysql.connector.errors.DatabaseError:
            print('bienvenido a la base de datos -nombre de la base de datos-')
        else:
            print('base de datos creada exitosamente')

        self.conexion.close()