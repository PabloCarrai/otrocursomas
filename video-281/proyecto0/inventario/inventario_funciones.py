from datetime import datetime
from collections import Counter


def registrar_producto(productos, producto):
    """
    Registra un nuevo producto en el inventario

    Parameters:
    productos: Lista de productos en el inventario
    producto: Producto a agrgar al inventario
    """
    productos.append(producto)


def realizar_venta(ventas, venta):
    """
    Crea una nueva venta

    Parameters:
    ventas: lista de las ventas realizadas hasta el momento
    venta: venta recien realizada
    """
    venta["fecha"] = datetime.now()
    ventas.append(venta)


def buscar_productos(productos, id_producto):
    """
    Busca un producto a partir de su id
    Parameters:
    productos: lista de productos en el inventario
    id_producto: id del producto a buscar
    Returns:
    el producto encontrado, si no se encuentra None
    """
    for p in productos:
        if p["id_producto"] == id_producto:
            return p

    return None


def cambiar_estado_producto(producto):
    """
    Cambia el estado de un producto
    Parameters:
    producto: producto sobre el que se cambiara el estado
    """
    producto["disponible"] = not producto["disponible"]


def ventas_rango_fecha(ventas, fecha_inicio, fecha_final):
    """
    Obtiene las ventas realizadas en un rango de fecha

    Parameters:
    ventas: lista de ventas realizadas hasta el momento
    fecha_inicio: fecha de inicio del rango
    fecha_final: fecha final del rango

    Returns:
    lista de ventas realizadas en el rango especificado

    """
    ventas_rango = []
    for v in ventas:
        if fecha_inicio <= v["fecha"] <= fecha_final:
            ventas_rango.append(v)
    return ventas_rango


def top_5_mas_vendidos(ventas):
    """
    Obtiene el top 5 de los mas vendidos

    Parameters:
    ventas: Lista de ventas realizadas hasta el momento
    Returns:
    Lista de tuplas (id,cantidad_total_venta) de los 5 productos mas vendidos
    """
    conteo_ventas = {}
    for v in ventas:
        if v["id_producto"] in conteo_ventas:
            conteo_ventas[v["id_producto"]] += v["cantidad"]
        else:
            conteo_ventas[v["id_producto"]] = v["cantidad"]

    conteo_ventas = {
        k: v
        for k, v in sorted(
            conteo_ventas.items(), key=lambda item: item[1], reverse=True
        )
    }
    contador = Counter(conteo_ventas)
    return contador.most_common(5)


def top_5_menos_vendidos(ventas):
    """
    Obtiene el top 5 de los menos vendidos

    Parameters:
    ventas: Lista de ventas realizadas hasta el momento
    Returns:
    Lista de tuplas (id,cantidad_total_venta) de los 5 productos menos vendidos
    """
    conteo_ventas = {}
    for v in ventas:
        if v["id_producto"] in conteo_ventas:
            conteo_ventas[v["id_producto"]] += v["cantidad"]
        else:
            conteo_ventas[v["id_producto"]] = v["cantidad"]

    conteo_ventas = {
        k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1])
    }
    contador = Counter(conteo_ventas)
    return contador.most_common()[:-6:-1]


def mostrar_datos_producto(producto):
    """
    Muestra datos particulares de un producto

    :param producto: Producto a consultar los datos
    """
    print(f"ID: {producto["id_producto"]}")
    print(f"Nombre: {producto["nombre"]}")
    print(f"Precio: ${producto["precio"]}")
    print(f"Cantidad: {producto["cantidad"]}")
    print(f"Disponible?: {"Si" if producto["disponible"] else "No"}")


def mostrar_datos_venta(venta):
    """
    Muestra datos particulares de una venta

    :param venta: Venta a consultar los datos
    """
    print(f"ID: {venta["id_producto"]}")
    print(f"Fecha: {venta["fecha"]}")
    print(f"Cantidad: ${venta["cantidad"]}")
    print(f"Total sin Iva: {venta["total_sin_iva"]}")
    print(f"Total: {venta["total_sin_iva"]}*1.19")
    print()
    print("Datos del producto:")
    mostrar_datos_producto(venta["id_producto"])


def mostrar_datos_venta_producto(datos_venta):
    pass
