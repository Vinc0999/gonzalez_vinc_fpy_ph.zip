from os import system
from msvcrt import getch
from Funciones import  *


while True:
    print("presione una tecla para continuar")
    getch()
    system("cls")

    print("""
BIENVENIDO A LA MEJOR TIENDA😎🤞
        1.Registrar producto👌
        2.Listar producto📄
        3.Eliminar producto❌
        4.salir""")
    
    seleccion=int(input("ingrese su opcion : "))

    match seleccion:
        case 1:
            codigo=int(input("ingrese codigo : "))
            nombre=input("ingrese nombre : ")
            precio=int(input("ingrese precio : "))
            stock=int(input("ingrese el stock : "))
            registrar(codigo, nombre, precio, stock)
        
        case 2:
            listar()
        
        case 3:
            input("ingrese su codigo que quiera borrar : ")
            eliminar(codigo)
        case 4:
            break 

