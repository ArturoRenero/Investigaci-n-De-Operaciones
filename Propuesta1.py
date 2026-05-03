#Este es una prueba de la libreria, hice la primera parte del procedimeinto hasta llegar al segundo valor inicial, falta optimizar por supuesto
#Pero este es un ejmplo o idea de como puede ser las cosas, cada paso esta indicado y tiene un pode documentacion, espero que se entienda
#----------------------------------------------------
#Primero Importamos la Libreria
import sympy as sp
#----------------------------------------------
#Decirle a python que trate a "x1"y "x2"como variable matematica
x1 = sp.symbols('x1')
x2 = sp.symbols('x2')
#Declaramos el valor inicial (se puede poner desde un inicio, pero ahorita con fines practicos lo haremos asi)
val_i1 = 0
val_i2 = 0
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
#Multiplicar por "t"
#Tambien le decimos que trate a la "t" como simbolo matematico
t = sp.symbols('t')
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
val_i1 = x1t.subs(t, dt[0])
val_i2 = x2t.subs(t, dt[0])
print(val_i1)
print(val_i2)