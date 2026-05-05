# C:\Users\artur\AppData\Local\Programs\Python\Python313\Lib\site-packages\sympy\solvers\ >> solvers.py >> line 363 (might come in handy) >> line 902 (break point)
# 

#Este es una prueba de la libreria, hice la primera parte del procedimeinto hasta llegar al segundo valor inicial, falta optimizar por supuesto
#Pero este es un ejmplo o idea de como puede ser las cosas, cada paso esta indicado y tiene un pode documentacion, espero que se entienda
#----------------------------------------------------
#Primero Importamos la Libreria
import sympy as sp
#----------------------------------------------
#Decirle a python que trate a "x1"y "x2"como variable matematica
x1 = sp.symbols('x1')
x2 = sp.symbols('x2')
t = sp.symbols('t') # para mantener organizado el acomodo, inicialice el simbolo 't' al inicio del codigo 
#Declaramos el valor inicial (se puede poner desde un inicio, pero ahorita con fines practicos lo haremos asi)
global val_i1 # se hacen globales para poder acceder a ellas dentro de main()
global val_i2 
val_i1 = 0 
val_i2 = 0

val_f1 = 0 # se utilizara val_fN para los valores finales de cada PASO, los cuales seran los parametros que se pasaran a main() cuando vuelva a iniciar
val_f2 = 0
#-------------------------------------------------------------
#Pedir la funcion (en este caso la daremos por determinada)
fx = 2*x1*x2 + 2*x2 - x1**2 - 2*x2**2
#-------------------------------------------------------
#Derivar la funcion principal de manera parcial
dp1 = sp.diff(fx, x1)#Derivada Parcial respecto a x1, se usa la funcion de esta libreria, le pasamos dos parametros, la funcion y la variable respecto a la cual va aderivar
dp2 = sp.diff(fx, x2)
# print(dp1) #Solo fueron para confirmar que funciono y asi fue gg
# print(dp2)
#-----------------------------------------------------------
#Sustituimos en las derivadas parciales
susdp1 = dp1.subs({x1:val_i1, x2:val_i2})
#el .subs es parte de la libreria para sustituir, esta es la notacion para  sustituir en dos variables, se pone la variable seguida de ":" y luego el valor
susdp2 = dp2.subs({x1:val_i1, x2:val_i2})
# print(susdp1)
# print(susdp2)
#----------------------------------------------------------
"""
Aqui comienza lo bueno ;)
1. Englobar las siguientes lineas de codigo en una funcion "main" 
2. Hacer la funcion de forma recursiva, enviando como parametros a x1, x2 
3. La condicion de paro sera la siguiente:
    if (fx < 0.998):
        return
    else:
        ....
4. Rezar por que funcione
"""
condicion_paro = 0.998
global c 
c = 0

# Condicion de paro; checar si x1/x2 son float o int; 
def main(A, B, index):
    # Para confirmar que la funcion aun no ha cumplido su proposito,
    # se debe evaluar la fn Objetivo con los respectivos valores actuales de x1 y x2.
    # Ya que buscamos maximizar z (fnObjetivo), nuestra condicion de paro sera cuando la fnObjetivo se aproxime a 1.0 
    
    # se sustituyen los simbolos x1, x2 por val_i1, val_i2 para que la fnObjetivo arroje un valor numerico, y no uno matematico (-x1**2 + 2*x1*x2 - 2*x2**2 + 2*x2)
    resultado_fnObjetio = sp.solve(2*A*B + 2*B - A**2 - 2*B**2, A, B) # arrojara un valor flotante (0.5, 0.75, 0.875, ..., 0.n ~= 0.999)
    print("===================== FUNCION OBJETIVO: ===================== ")
    print(resultado_fnObjetio[0])
    print("==============================================================")
    if (resultado_fnObjetio[0] > condicion_paro):
        return
    # obviamos el else, ya que si se cumple la condicion anterior, automaticamente rompera el ciclo recursivo

    # se vuelven a definir los valores iniciales para x1 y x2 al inicio de la funcion ya que tomaran los valores finales del paso anterior 
    val_i1 = A # TODO: Mejorar esta forma de reasignar valores a x1, x2. Considera la opcion de englobar la inicializacion de x1, x2, la fnObjetivo y sus derivadas primeras lineas de codigo en una funcion independiente y llamarla solo 1 vez al inicio de main()
    val_i2 = B 


    #Multiplicar por "t"
    #Tambien le decimos que trate a la "t" como simbolo matematico
    # t = sp.symbols('t') # para mantener organizado el acomodo, inicialice el simbolo 't' al inicio del codigo 
    #Se multiplica por "t"
    x1t = val_i1 + t*susdp1
    x2t = val_i2 + t*susdp2
    # print(x1t)
    # print(x2t)
    #------------------------------------------------
    #Sustituir en la funcion original con las "t"
    ft = fx.subs({x1:x1t, x2:x2t})
    # print(ft)
    #-------------------------------------------------
    #Derivar respecto a "t"
    dt = sp.diff(ft, t)
    # print(dt)
    #------------------------------------
    #Despejar "t"
    dt = sp.solve(dt, t)
    #Asi es como se resuleve una ecuacion en la libreria, en los parametros se pone la ecueacion, luego la variable
    # print(dt)
    #-----------------------------------------------------------------------------
    #Sustituir en la funcion respecto a t "x1t" y "x2t"
    val_f1 = x1t.subs(t, dt[0]) # se cambia de val_iN a val_fN para mantener la logica de tener un valor inicial y uno final
    val_f2 = x2t.subs(t, dt[0])
    print(val_f1)
    print(val_f2)

    index += 1
    # mandamos llamar a la misma funcion, con los nuevos valores de x1 y x2
    main(val_f1, val_f2, index)

main(val_i1, val_i2, c)