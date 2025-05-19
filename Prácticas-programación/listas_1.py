#Crear y modificar listas 

#Ejercicio 1. Crear una lista de 5 números enteros del 1 al 10 y mostrarla por pantalla.
lista_numeros_enteros = [1, 2, 3, 4, 5]
print(lista_numeros_enteros)
#Ejericio 2. Agregar un numero al final de la lista creada en el ejercicio 1 y mostrarla por pantalla.
lista_numeros_enteros.append(6)
print(lista_numeros_enteros)
#Ejercicio 3 agregar un numero en el medio
lista_numeros_enteros.insert(3, 7)
print(lista_numeros_enteros)
#Ejerciocio 4. Invertir el orden de la Lista y mostrarla por pantalla.
lista_numeros_enteros.reverse()
print(lista_numeros_enteros)



#Operaciones con listas

#Suma todos los elementos de una lista.
lista_numeros_enteros_sumados = sum(lista_numeros_enteros)
print(lista_numeros_enteros_sumados)
#Encuentra el número mayor y el menor en una lista.
numero_mayor = max(lista_numeros_enteros)
numero_menor = min(lista_numeros_enteros)
print(f'El número mayor es: {numero_mayor}')
print(f'El número menor es: {numero_menor}')
#Filtra solo los números pares de una lista de enteros

lista_numeros_enteros_pares = [num for num in lista_numeros_enteros if num % 2 == 0]

print(f'Los números pares son: {lista_numeros_enteros_pares}')


