restricciones = [] # lista de restricciones

fn = int(input("Dar una funcion objetivo a evaluar: ")) #TODO: Agregar un input para saber si se requiere max o min z, por ahora solo requieren que maximicemos la fnObjetivo, asi que permanecera de esta forma hasta que requieran minimizar z 
error = int(input("Dar un margen de error (Ej. 0.25, 0.001, etc.): "))
restriccion = input("¿El problema tiene restricciones? \nSi = \"S\"\nNo = \"N\"")

while (restriccion == "S"):
    restricciones.append(input("Da una restriccion: ").split(",")) # Ej. x1 + x2  <= 1; x1 >= 0, x2 >= 0 // Se usa .spli() para restricciones complejas
    restriccion = input("¿Hay mas restricciones? \nSi = \"S\"\nNo = \"N\"")

# restricciones = ["x1 + x2  <= 1"]
def ChecarRestricciones(Restricciones, u, v): # ("x1 + x2 > 0"; 1; 1) >>> if (1 + 1 > 0) ? continue : return False
    X1, X2 = u, v
    for restriccion in Restricciones:
        for i in range(len(restriccion)): # buscamos el char "x" para confirmar el inidice posterior (1 ó 2); y aprovechamos para checar que hay despues de la igualdad y convertirlo a valor numerico ("x1 >= 1") >>> "1" > 1
            if (restriccion[i] == "x"):
                match restriccion[i]:
                    case "1": 
                        
         
        if (restriccion):
            continue
        else:
            return False
    return True


