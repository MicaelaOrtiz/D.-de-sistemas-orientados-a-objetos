from menu_buil import MenuBuilder

def option_1():
    print("\n--- Mostrar perfil ---")
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    print(f"\nHola {nombre}, tienes {edad} años.")
    input("Presiona ENTER para continuar...")

def option_2():
    print("\n--- Configuraciones ---")
    print("1. Cambiar idioma")
    print("2. Activar notificaciones")
    print("3. Desactivar notificaciones")

    seleccion = input("Seleccione una opción: ")
    if seleccion == "1":
        print("Idioma cambiado a Español.")
    elif seleccion == "2":
        print("Notificaciones activadas.")
    elif seleccion == "3":
        print("Notificaciones desactivadas.")
    else:
        print("Opción no válida.")
    input("Presiona ENTER para continuar...")

def option_3():
    print("\n--- Ayuda ---")
    print("Este es un sistema de menú interactivo.")
    print("Elige una opción del menú escribiendo su número.")
    input("Presiona ENTER para continuar...")

if __name__ == "__main__":
    builder = MenuBuilder()
    builder.add_option("1", "Mostrar perfil", option_1)\
           .add_option("2", "Configuraciones", option_2)\
           .add_option("3", "Ayuda", option_3)

    menu = builder.build()
    menu.run()
