import random as rd
lista= [] # lista vacia
for i in range (10): #inicio de un bucle es con el :el identado es importante
    num=rd.randint(1,10)#genera son numeros aleatorios del 1 al 10
    lista.append(num)#append añade a ala lista
print(lista)

vol_sqrt=[]
V = [4.5,2.32,4.88]
for i in V:
    vol_sqrt.append(i*i)
print(f"el voltaje al cuadrado es: {vol_sqrt}") #comando map

lectura = [4.95, 5.10, 4.88]
for idx, vol in enumerate(lectura, start=1):
    print(f"{idx}: {vol:.2f}v")