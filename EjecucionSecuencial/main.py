import secondaryFile
import subprocess as sbp

# sbp toma como argumentos, el comando a ejecutar, el parametro (en este caso, nombre del archivo), y se le pueden enviar argumentos adicionales, si y solo sí, el .java los puede recibir y utilizar (puede recibir mas parametros, pero el .java va a fallar).
sbp.run(["javac", "javaFile.java"]) # compile Java program

# capture_output && text se aseguran de obtener el resultado del .java como un valor de tipo "subprocess" 
result = sbp.run(["java", "javaFile", "5", "8"], capture_output=True, text=True) # run Java program 


print("Result from Java: ", result.stdout.strip()) # se utiliza .strip() meramente para tener un resultado "limpio"
integer_result = int(result.stdout.strip()) # se hace un casting para convertir de str a int {"result.stdout.strip()" is instance of str}
print(isinstance(integer_result, int))

print("hello from Main file")