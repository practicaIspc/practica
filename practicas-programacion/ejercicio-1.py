# Programa para buscar el mayor de 3 números

#Opción 1.

n1= int(input("Ingrese el 1er número: "))
n2 = int(input("Ingrese el 2do número: "))
n3 = int(input("Ingrese eñ 3er número: "))

if n1 > n2:
    print(f' El número mayor es el: {n1}')
elif n2 > n3:
    print(f'El número mayor es el: {n2}')
else:
    print(f'El número mayor es el: {n3}')
