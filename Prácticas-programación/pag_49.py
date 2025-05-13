#Pruebas pagina 49 del Cuadernillo
#1. Escribe un programa que solicite tres lados de un triangulo e indique si es equilatero, isoceles o escaleno.




#2. Escribe program que solicite al usuario que ingrese una contraseña y confirme contraseña


contrasenia_original = "hola_mundo_01"

# Pedimos al usuario que ingrese y confirme la contraseña
contrasenia_ingresada = input("Ingrese la contraseña: ").strip().lower()

# Mientras la contraseña no coincida, permitimos un segundo intento
if contrasenia_ingresada == contrasenia_original:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
    contrasenia_ingresada = input("Ingrese nuevamente la contraseña: ").strip().lower()
    if contrasenia_ingresada == contrasenia_original:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta, se ha bloqueado el acceso")





#3. Escribe programa que solicite al usuario precio y cantidad de un producto . clasifique como "caro" si el precio es mayor de $100 o si la cantidad es menor que 10 y el precio es mayor de $50. De lo contrario, clasifíquelo como "barato". Incluye condiciones para manejar valores falsos (0 o vacío).
#4. Escribe un programa que solicite al usuario su nombre, edad y número de teléfono. Verifica que ninguno de estos datos esté vacío o sea un valor falso (por ejemplo, 0).



