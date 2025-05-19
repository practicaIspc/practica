#Ejercicios con Tuplas

#Crea una tupla con los días de la semana.
dias_de_la_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
#Accede al tercer elemento.
print(dias_de_la_semana[2])
#Intenta modificar un elemento (¿qué sucede?).

#Conversión entre tuplas y listas

#Convierte la tupla en una lista, modifica un elemento y luego conviértela de nuevo en tupla.
dias_de_la_semana_lista = list(dias_de_la_semana)
list(dias_de_la_semana_lista).append("nuevo_dia")
print(dias_de_la_semana_lista)
#Convierte la lista de nuevo en una tupla.
dias_de_la_semana = tuple(dias_de_la_semana_lista)
print(dias_de_la_semana_lista)