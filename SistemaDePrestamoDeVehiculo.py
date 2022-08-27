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

    def vehiculo(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="Seguro"
        )
        self.cursor = self.conexion.cursor()
        try:
            self.cursor.execute('''
                    CREATE TABLE vehiculo (
                        nombreDueño VARCHAR(100) NOT NULL,
                        matricula VARCHAR(100) UNIQUE NOT NULL PRIMARY KEY,
                        año VARCHAR(100) NOT NULL,
                        marca VARCHAR(100) NOT NULL,
                        Color VARCHAR(100),
                        pago INTEGER NOT NULL
                    )
                ''')
        except mysql.connector.errors.ProgrammingError:
            print('bienvenido a la tabla vehiculo')
        else:
            print('tabla vehiculo creada correctamente')
        self.conexion.close()