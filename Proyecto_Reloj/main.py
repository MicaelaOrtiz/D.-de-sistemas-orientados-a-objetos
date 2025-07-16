from models.reloj import Reloj
from models.builder import RelojBuilder

if __name__ == "__main__":
    reloj1 = RelojBuilder().set_hora(10).set_minuto(30).set_segundo(45).build()
    reloj2 = RelojBuilder().set_hora(15).set_minuto(59).set_segundo(59).build()
    reloj3 = RelojBuilder().set_hora(23).set_minuto(58).set_segundo(59).build()

    print("Relojes creados:")
    print("Reloj 1:", reloj1)
    print("Reloj 2:", reloj2)
    print("Reloj 3:", reloj3)

    reloj2.adelantar_minuto()
    print("\nReloj 2 adelantado un minuto:")
    print("Reloj 2:", reloj2)

    reloj3.update_hora(5, 20, 0)
    print("\nReloj 3 modificado:")
    print("Reloj 3:", reloj3)

    print("\n¿Reloj 1 y Reloj 3 tienen la misma hora?")
    print("Resultado:", reloj1 == reloj3)
