from inventario_funciones import (
    registrar_producto,
    realizar_venta,
    buscar_productos,
    cambiar_estado_producto,
    ventas_rango_fecha,
    top_5_mas_vendidos,
    top_5_menos_vendidos,
)


def mostrar_menu():
    """
    Muestra menu de opciones disponibles
    """
    print("1. Registrar nuevo producto  ")
    print("2. Vender un producto  ")
    print("3. Buscar un producto por su codigo  ")
    print("4. Cambiar disponibilidad de un producto  ")
    print("5. Productos vendidos en un rango de fechas  ")
    print("6. Top 5 de productos mas vendidos  ")
    print("7. Top 5 de productos menos vendidos  ")
    print("0. Salir  ")


def capturar_entero(mensaje):
    """
    Captura un numero entero, valida el ingreso de datos
    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de un numero entero.
    Returns:
    Numero entero resultado de la captura
    """
    while True:
        try:
            numero = int(input(f"{mensaje: }"))
            return numero
        except ValueError:
            print("Error debe digitar un numero entero.")
        print()


def capturar_real(mensaje):
    """
    Captura un numero real, valida el ingreso de datos
    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de un numero real.
    Returns:
    Numero entero resultado de la captura
    """
    while True:
        try:
            numero = float(input(f"{mensaje: }"))
            return numero
        except ValueError:
            print("Error debe digitar un numero entero.")
        print()


def capturar_cadena(mensaje):
    """
    Captura un cadena de caracteres, valida el ingreso de datos
    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de un cadena de caracteres.
    Returns:
    Cadena de caracteres resultado de la captura
    """
    while True:
        cadena = input(f"{mensaje: }").strip()
        if len(cadena) != 0:
            return cadena
        else:
            print("Debe digitar una cadena de caracteres con texto")
        print()


def listar_productos(productos):
    for p in productos:
        print(f"{p["id_producto"]}- {p["nombre"]}")


def main():
    productos = []
    ventas = []
    while True:
        while True:
            try:
                mostrar_menu()
                opcion = int(input("Digite una opcion:    "))
                if 0 <= opcion <= 7:
                    break
                else:
                    print("Debe digitar un numero mayor o igual a 0")
            except ValueError as e:
                print("Error debe digitar un entero valido   ")
        if opcion == 0:
            break
        elif opcion == 1:
            while True:
                id_producto = capturar_entero("Ingrese el id del nuevo producto:")
                producto = buscar_productos(productos, id_producto)
                if producto is None:
                    break
                else:
                    print("Ya existe un producto con el id Digitado")
            nombre_producto = capturar_cadena("Digite el nombre del nuevo producto")

            while True:
                precio = capturar_real("Digite el precio del nuevo producto")
                if precio > 0:
                    break
                else:
                    print("Debe digitar un precio de producto mayor a 0")
            while True:
                cantidad_producto = capturar_entero(
                    "Digite la cantidad del nuevo producto"
                )
                if cantidad_producto >= 0:
                    break
                else:
                    print("Debe digitar una cantidad positiva")
            while True:
                print("1.Disponible")
                print("2.No Disponible")
                disponible = capturar_entero(
                    "Digite la opcion para la disponibilidad del producto"
                )
                if disponible == 1 or disponible == 2:
                    disponible = disponible == 1
                    break

            nuevo_producto = {
                "id_producto": id_producto,
                "nombre": nombre_producto,
                "precio": precio,
                "cantidad": cantidad_producto,
                "disponible": disponible,
            }
            registrar_producto(producto, nuevo_producto)
            print("El producto se ha creado de forma satisfactoria")

        if opcion == 2:
            if len(productos):
                while True:
                    listar_productos(productos)
                    id_producto = capturar_entero("Digite el ID del producto")
                    producto = buscar_productos(productos, id_producto)
                    if producto:
                        break
                    else:
                        print("Mensaje: Debe escribir un ID de producto existente")

                while True:
                    cantidad_producto = capturar_entero(
                        "Digite la cantidad del nuevo producto"
                    )
                    if cantidad_producto >= 0:
                        if cantidad_producto <= producto["cantidad"]:
                            break
                        else:
                            print(
                                f"No existe cantidad suficiente para la venta, solo hay {producto["cantidad"]}"
                            )
                    else:
                        print("Debe digitar una cantidad positiva")
                nueva_venta = {
                    "id_producto": id_producto,
                    "cantidad": cantidad_producto,
                    "total_sin_iva": producto["precio"] * cantidad_producto,
                }
                realizar_venta(ventas, nueva_venta)
                print("La venta se ha realizado de forma satisfactoria")
            else:
                print("Aun no ha registrado productos.")
        elif opcion == 3:
            if len(productos):
                while True:
                    listar_productos(productos)
                    id_producto = capturar_entero("Digite el ID del producto")
                    producto = buscar_productos(productos, id_producto)
                    if producto:
                        break
                    else:
                        print("Mensaje: Debe escribir un ID de producto existente")
                
            else:
                print("Aun no ha registrado productos.")
    print()
    print("El programa ha finalizado")


if __name__ == "__main__":
    main()
