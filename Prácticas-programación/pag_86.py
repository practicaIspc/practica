# Teniendo en cuenta los principios y técnicas de la programación
# estructurada resolver:
# 1. Escribe un programa que tenga un menú para gestionar un
# inventario de productos:
# a. Agregar Producto
# b. Mostrar Inventario
# c. Buscar Producto
# d. Eliminar Producto
# e. Salir

# Inventario como diccionario global
inventario = {}

def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("a. Agregar Producto")
    print("b. Mostrar Inventario")
    print("c. Buscar Producto")
    print("d. Eliminar Producto")
    print("e. Salir")

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("Ingrese la cantidad: "))
    inventario[nombre] = cantidad
    print(f"Producto '{nombre}' agregado con éxito.")

def mostrar_inventario():
    print("\nInventario actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")
    if not inventario:
        print("El inventario está vacío.")

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ").lower()
    if nombre in inventario:
        print(f"{nombre}: {inventario[nombre]} unidades disponibles.")
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").lower()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado.")
    else:
        print("Producto no encontrado.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").lower()
        
        if opcion == "a":
            agregar_producto()
        elif opcion == "b":
            mostrar_inventario()
        elif opcion == "c":
            buscar_producto()
        elif opcion == "d":
            eliminar_producto()
        elif opcion == "e":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutamos el programa
if __name__ == "__main__":
    main()


