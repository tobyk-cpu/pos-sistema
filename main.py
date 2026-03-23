def mostrar_menu_principal():
    print("=== Menu Principal ===")
    print("1. Hacer Compra")
    print("2. Ver Compras")
    print("3. Salir")


def menu_hacer_compra():
    print("--- Hacer Compra ---")
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    total = precio * cantidad
    print(f'Total de la compra: ${total:.2f}')
    # Aquí se podría añadir lógica para guardar la compra


def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            menu_hacer_compra()
        elif opcion == '2':
            print("Funcionalidad de ver compras no implementada.")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == '__main__':
    main()