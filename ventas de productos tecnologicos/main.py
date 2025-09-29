from controllers.product_controller import ProductController

def menu():
    controller = ProductController()

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ver lista de productos")
        print("2. Ver detalle de producto con descuento")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            controller.list_products()

        elif opcion == "2":
            try:
                product_id = int(input("Ingresá el ID del producto: "))

                print("\nElegí tipo de descuento:")
                print("1. Sin descuento")
                print("2. 10% de descuento")
                print("3. Descuento fijo de $500")
                desc_opcion = input("Opción: ")

                if desc_opcion == "2":
                    strategy = "percentage"
                elif desc_opcion == "3":
                    strategy = "fixed"
                else:
                    strategy = "none"

                controller.show_product(product_id, strategy)

            except ValueError:
                print("⚠ Debes ingresar un número válido.")

        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("⚠ Opción no válida, intentá de nuevo.")

if __name__ == "__main__":
    menu()
