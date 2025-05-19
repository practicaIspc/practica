#Ejercicios con Diccionarios

#Crea un diccionario con tres claves: "nombre", "edad" y "ciudad".
#Diccionario PErsona Estudiante
estudiante = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Córdoba",
    "carrera":"Diseño Web y Aplicaciones Digitales",
    "materias": ["Programación", "Etica y Deontologia", "Base de Datos"]
}
#Modifica el valor de "edad".
estudiante["edad"] = 31
#print(estudiante)
#Agrega una nueva clave llamada "profesión".
estudiante['profesión'] = "Diseñador Web"
#print(estudiante)
#Borra la clave "ciudad".
estudiante.pop("ciudad")
#print(estudiante)


#Iteración y búsqueda

#Itera sobre las claves e imprime los valores.
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
#Busca si existe una clave específica en el diccionario.
if "nombre" in estudiante:
    print("La clave 'nombre' existe en el diccionario.")
    
#Ejercicio 2. Crea un diccionario con los días de la semana y sus respectivos números (1-7).
dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}
#Accede al nombre del día correspondiente al número 3.
#print(dias_semana[3])


#Aplicar Manejo de Excepciones. Funciones
#Ejercicio 1. Crear una función que reciba un número del 1 al 7 y devuelva un mensaje saludando.

def saludar_dia(numero_dia):
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    try:
        return f"¡Hola! Hoy es {dias_semana[numero_dia]}."
    except KeyError:
        return "Número de día inválido. Debe ser del 1 al 7."
    
    
#saludar_dia(0) no me imprimer el saludo

#loop en diccionario
for dias in dias_semana:
    print(f"¡Hola! Hoy es {dias_semana[dias]}.")