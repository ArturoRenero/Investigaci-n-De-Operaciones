#-------------------------------------------------------------------Intento de automatizacion con ciclo incluido------------------------------------------------
#----------------------------------------------------
#Primero Importamos la Libreria de las mateprosss
import sympy as sp
#Importamos la libreria de las graficacion en numeros primos gg ff
import matplotlib.pyplot as plt
#----------------------------------------------
#Decirle a python que trate a "x1"y "x2"como variable matematica
x1 = sp.symbols('x1')
x2 = sp.symbols('x2')
#Declaramos el valor inicial fuera del ciclo
val_i1 = 0
val_i2 = 0
#-------------------------------------------------------
#Arreglo para meter los valores a graficar
gra_x1 = [0]
gra_x2 = [0]
#-------------------------------------------------------------
#Pedir la funcion (en este caso la daremos por determinada)
#-----------------------------------------------------------Igual debe estar fuera del ciclo
fx = 2*x1*x2 + 2*x2 - x1**2 - 2*x2**2
#-------------------------------------------------------
#Derivar la funcion principal de manera parcial
#-----------------------------------------------------------Fuera del ciclo tambien
dp1 = sp.diff(fx, x1)#Derivada Parcial respecto a x1, se usa la funcion de esta libreria, le pasamos dos parametros, la funcion y la variable respecto a la cual va aderivar
dp2 = sp.diff(fx, x2)
#-----------------------------------------------------------

# _______________________________________ Cambios por Arturo _______________________________________
#==========================================================================================================================





#==========================================================================================================================

#------------------------------------------------------------Aqui debe empezar el ciclo------------------------------------
resu = 0 #variable donde se almacena el resultado de la sustitucion
#Se puede modificar la condicion de paro, pdependiendo de la modificacion, saldran mas valores o menos....
while resu <= 0.998:

    #Sustituimos en las derivadas parciales
    susdp1 = dp1.subs({x1:val_i1, x2:val_i2})
    #el .subs es parte de la libreria para sustituir, esta es la notacion para  sustituir en dos variables, se pone la variable seguida de ":" y luego el valor
    susdp2 = dp2.subs({x1:val_i1, x2:val_i2})
    #----------------------------------------------------------
    #Multiplicar por "t"
    #Tambien le decimos que trate a la "t" como simbolo matematico
    t = sp.symbols('t')
    #Se multiplica por "t"
    x1t = val_i1 + t*susdp1
    x2t = val_i2 + t*susdp2
    #------------------------------------------------
    #Sustituir en la funcion original con las "t"
    ft = fx.subs({x1:x1t, x2:x2t}).expand()
    #-------------------------------------------------
    #Derivar respecto a "t"
    dt = sp.diff(ft, t)
    #------------------------------------
    #Despejar "t"
    dt = sp.solve(dt, t)
    #Asi es como se resuleve una ecuacion en la libreria, en los parametros se pone la ecueacion, luego la variable
    #-----------------------------------------------------------------------------
    #Sustituir en la funcion respecto a t "x1t" y "x2t"
    #Estas variables son para guardar el valor de "dt".....abajo se indica el por que
    dt1 = dt[0]
    dt2 = dt[0]
    val_i1 = x1t.subs(t, dt1)#Aqui de especifica que es la posicion 0, pq guarda el valor en un arreglo
    val_i2 = x2t.subs(t, dt2)#Se puede dejar asi o se puede meter a una variable...
    print("valor 1 " + str(val_i1) + " valor 2 " + str(val_i2))#Es solo para verificar si coincide con el libroo
    #Metemos a este arreglo los valores para despues graficar
    gra_x1.append(val_i1)
    gra_x2.append(val_i2)
    resu = fx.subs({x1:val_i1, x2:val_i2})#Sustituimos en la funcion original los nuevos puntos iniciales para ver la aproximacion q tiene
    
#----------------------GRAFICAMOS-----------------
plt.plot(gra_x1, gra_x2, marker='o', linestyle='-', color='purple', label='Datos calculados')

#  Detalles estéticos (Opcional pero recomendado)
plt.title("Metodo del gradiante")
plt.xlabel("Eje X1")
plt.ylabel("Eje x2")
plt.grid(True) # Agrega una cuadrícula de fondo
plt.legend()   # Muestra la leyenda

# 4. Mostrar el gráfico
plt.show()