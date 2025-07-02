
productos=[]



def buscar(codigo : int):
    for a in range(len(productos)):
        if productos(len(productos))==codigo:
            return a
        else:   
            return -1

def registrar(codigo : int,nombre : str,precio,stock):
    if (codigo)>=0:
        
        if len(nombre)>=3:
            
            if precio>0:
                
                if stock>0:
                  
                    dates = {
                      "codigo": codigo,
                      "nombre": nombre,
                      "precio": precio,
                      "stock":  stock }
                    productos.append(dates)
                    print("producto listo")
                else:
                    print("stock invalido ❌")
            else:
                print("precio debe ser mayor a 0 ❌")
        else:
            print("nombre debe tener al menos 3 letras ❌")
    else:
        print("codigo no valido ❌")
    return False


def listar():
    for a in range(len(productos)):
        if productos[a]["stock"] >0:
            print(f"{a+1} {productos[a]["stock"]} {productos[a]["precio"]} {productos[a]["nombre"]} {productos[a]["codigo"]}")


def eliminar(codigo):
    if buscar(codigo) >0:
        print("ingrese codigo") 
        if productos(codigo) == codigo:
                codigo.pop()
                print("eliminado")
        else:
                print("producto no valido")    
    else:
        print("codigo invalido")

