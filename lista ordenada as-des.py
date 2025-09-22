import random as rd
num = [rd.randint(1,100)for _ in range(10) ]
print("Lista original:", num)

for i in range (len(num)):
    for j in range (0, len(num)- i -1):
        if num[j]>num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print("lista ordenada ascendente: ", num)
 
for i in range (len(num)):
    for j in range (0, len(num)- i - 1):
        if num[j]< num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print("Lista ordenada descendente:", num)