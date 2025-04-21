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

#Opcion 2

numero1 = int(input("Ingrese el primer numero"))
numero2 = int(input("Ingrese el segundo numero"))
numero3 = int(input("Ingrese el tercer numero"))

if numero1 > numero2 and numero1 > numero3:
   print(f"El numero {numero1} es mayor que los tres numeros")

if numero2 > numero1 and numero2 > numero3:
    print(f"El numero {numero2} es mayor que los tres numeros")

if numero3 > numero1 and numero3 > numero2:
    print(f"El numero {numero3} es mayor que los tres numeros")