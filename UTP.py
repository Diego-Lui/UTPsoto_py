import datetime as dt
import random as rd

nombre = "Diego Soto" 
fecha = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
v = rd.randint(1, 1023)
texto = "Buenas tardes, estos son los valores de medicion:  " + str(v)  +  " voltios "

print ( "Sr. Ingeniero Luis Torres")
print (texto )
print("De parte:  "+ nombre )
print("Datos del dia: " + fecha)