import mysql.connector
from dueno import Dueno
from menuDueno import MenuDueno
from menuinvernadero import MenuInvernadero
from menuUsuario import MenuUsuario
from menuplanta import MenuPlanta
from menuregistro import MenuRegistro

conexion = mysql.connector.connect(user='dana', password='12345', database='invernadero')
cursor = conexion.cursor()

while True:
    print("1) Menu deuño")
    print("2) Menu invernadero")
    print("3) Menu usuario")
    print("4) Menu planta")
    print("5) Menu registro")
    print("0) Salir")
    op = input()

    if op == "1":
        menuD = MenuDueno(conexion, cursor)
    elif op == "2":
        menuI = MenuInvernadero(conexion, cursor)
    elif op == "3":
        menuU = MenuUsuario(conexion, cursor)
    elif op == "4":
        menuP = MenuPlanta(conexion, cursor)
    elif op == "5":
        menuR = MenuRegistro(conexion, cursor)
    elif op == "0":
        break

#menuD = menuDueno()


#d = Dueno(conexion, cursor)
#d.crear('dana', 'gomez morales')
#print(d.recuperar())
