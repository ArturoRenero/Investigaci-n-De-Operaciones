restricciones = [] # lista de restricciones

fn = int(input("Dar una funcion objetivo a evaluar: "))
error = int(input("Dar un margen de error (Ej. 0.25, 0.001, etc.): "))
restriccion = input("¿El problema tiene restricciones? \nSi = \"S\"\nNo = \"N\"")

while (restriccion == "S"):
    restricciones.append(input("Da una restriccion: "))
    restriccion = input("¿Hay mas restricciones? \nSi = \"S\"\nNo = \"N\"")

