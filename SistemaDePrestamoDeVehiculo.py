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

create()
class Vehiculos:
    #constructor del objeto vehiculo
    def init(self, nombreDueño, matricula, año, marca, color, pago):
        self.nombreDueño = nombreDueño
        self.matricula = matricula
        self.año = año
        self.marca = marca
        self.color = color
        self.pago = pago
    
    def str(self):
        return 'Marca: {}\nColor: {}\n Año: {}\n Matricula: {}\n Propietario: {}\n Pago Mensual {}'.format(self.marca,self.color,self.año,self.matricula,self.nombreDueño,self.pago)

class Gestor_vehiculo:
    def agregar_vehiculo(self,u):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database='Seguro'
        )
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO vehiculo VALUES ('{}','{}','{}','{}','{}','{}')".format(u.nombreDueño,u.matricula,u.año,u.marca,u.color,u.pago))
        except mysql.connector.errors.IntegrityError:
            print('el vehiculo que desea añadir a la base de datos ya existe')
        else:
            print(f'{u} añadido correctamente')
        conexion.commit()
        conexion.close()
    
    def borra_vehiculo(self,matricula):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database='Seguro'
        )
        cursor = conexion.cursor()

        sql = "SELECT * FROM vehiculo WHERE matricula='{}'".format(matricula)
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        for usuario in usuarios:
            if matricula == usuario[1]:
                cursor.execute("DELETE FROM vehiculo WHERE matricula='{}'".format(matricula))
                print('el vehiculo de matricula {} se ha borrado correctamente '.format(matricula))
                conexion.commit()
                conexion.close()
                return
        print('el vehiculo de matricula {} nunca existio en la base de datos'.format(matricula))
    
    def consulta_vehiculo(self,matricula):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database='Seguro'
        )
        cursor = conexion.cursor()
        sql = cursor.execute("SELECT nombreDueño, matricula, año, marca, color, pago FROM clientes WHERE matricula='{}'".format(matricula))
        cursor.execute(sql)
        cliente = cursor.fetchone()
        if cliente == None:
            print('no existe un vehiculo registrado con ese numero de matricula')
        else:
            print(cliente)
        conexion.close()

c = Gestor_vehiculo
print('sistema de seguros')
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Agregar Vehiculo")
    print ("2. Borrar Vehiculo")
    print ("3. Consulta Vehiculo")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        nombreDueño = input('introduce el nombre del propietario del vehiculo')
        matricula = input('introduce la matricula del vehiculo')
        año = input('introduce la año del vehiculo')
        marca = input('introduce la marca del vehiculo')
        color = input('introduce el color del vehiculo')
        pago = input('introduce la cantidad que ese vehiculo debe pagar mensual')
        c.agregar_vehiculo(Vehiculos(nombreDueño, matricula, año, marca, color, pago))
    elif opcion == 2:
        c.borra_vehiculo(matricula)
    elif opcion == 3:
        c.consulta_vehiculo(matricula)
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")