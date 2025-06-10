from gestion import Gestion
from empleado import EmpleadoTemporal, EmpleadoFijo
from cliente import Cliente

def menu():
    gestion = Gestion()

    while True:
        print("\n===== Sistema de Gestión de Personas =====")
        print("1. Agregar Empleado Temporal")
        print("2. Agregar Empleado Fijo")
        print("3. Agregar Cliente")
        print("4. Mostrar todas las personas")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            salario = float(input("Salario: "))
            duracion = int(input("Duración del contrato (meses): "))
            empleado_temp = EmpleadoTemporal(nombre, edad, salario, duracion)
            gestion.agregar_persona(empleado_temp)
            print("Empleado Temporal agregado correctamente.")
        elif opcion == "2":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            salario = float(input("Salario: "))
            beneficios = input("Beneficios: ")
            empleado_fijo = EmpleadoFijo(nombre, edad, salario, beneficios)
            gestion.agregar_persona(empleado_fijo)
            print("Empleado Fijo agregado correctamente.")
        elif opcion == "3":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            email = input("Email: ")
            cliente = Cliente(nombre, edad, email)
            gestion.agregar_persona(cliente)
            print("Cliente agregado correctamente.")
        elif opcion == "4":
            print("\n----- Listado de Personas -----")
            gestion.mostrar_personas()
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor intenta de nuevo.")

if __name__ == "__main__":
    menu()
