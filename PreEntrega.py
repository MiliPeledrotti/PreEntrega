# Lista para almacenar los productos
inventario = []

# Función para registrar un nuevo producto
def registrar_producto():
    id = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' registrado exitosamente.")

# Función para visualizar todos los productos en el inventario
def visualizar_productos():
    if inventario:
        print("Inventario de productos:")
        for producto in inventario:
            print(f"{producto['id']} - {producto['nombre']}: ${producto['precio']} (Stock: {producto['cantidad']})")
    else:
        print("El inventario está vacío.")

# Función para actualizar un producto
def actualizar_producto():
    id = int(input("Ingrese el ID del producto a actualizar: "))
    for producto in inventario:
        if producto["id"] == id:
            nombre = input("Ingrese el nuevo nombre (presione Enter para mantener el actual): ")
            precio = input("Ingrese el nuevo precio (presione Enter para mantener el actual): ")
            cantidad = input("Ingrese la nueva cantidad (presione Enter para mantener el actual): ")
            if nombre:
                producto["nombre"] = nombre
            if precio:
                producto["precio"] = float(precio)
            if cantidad:
                producto["cantidad"] = int(cantidad)
            print(f"Producto con ID {id} actualizado exitosamente.")
            return
    print(f"No se encontró un producto con ID {id}.")

# Función para eliminar un producto
def eliminar_producto():
    id = int(input("Ingrese el ID del producto a eliminar: "))
    global inventario
    nuevo_inventario = [producto for producto in inventario if producto["id"] != id]
    if len(nuevo_inventario) < len(inventario):
        inventario = nuevo_inventario
        print(f"Producto con ID {id} eliminado exitosamente.")
    else:
        print(f"No se encontró un producto con ID {id}.")

# Función para buscar productos por nombre
def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    resultados = [producto for producto in inventario if nombre.lower() in producto["nombre"].lower()]
    if resultados:
        print("Productos encontrados:")
        for producto in resultados:
            print(f"{producto['id']} - {producto['nombre']}: ${producto['precio']} (Stock: {producto['cantidad']})")
    else:
        print(f"No se encontraron productos con el nombre '{nombre}'.")

# Función para generar reporte de bajo stock
def reporte_bajo_stock():
    limite = int(input("Ingrese el límite de stock para el reporte: "))
    productos_bajo_stock = [producto for producto in inventario if producto["cantidad"] < limite]
    if productos_bajo_stock:
        print("Productos con bajo stock:")
        for producto in productos_bajo_stock:
            print(f"{producto['id']} - {producto['nombre']}: Stock actual de {producto['cantidad']}")
    else:   
        print(f"Todos los productos tienen un stock igual o superior a {limite}.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Registrar producto")
        print("2. Visualizar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            visualizar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecución del menú
menu()
