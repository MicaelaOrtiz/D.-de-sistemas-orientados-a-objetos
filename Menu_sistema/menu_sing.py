class MenuSing:              # solo hay una instancia del menú en toda la aplicación.
    __instance = None

    def __init__(self):
        if MenuSing.__instance is not None:
            raise Exception("Esta clase es un singleton. Usa get_instance().")
        self.items = []
        MenuSing.__instance = self

    @staticmethod
    def get_instance():
        if MenuSing.__instance is None:
            MenuSing()
        return MenuSing.__instance

    def add_item(self, item):
        self.items.append(item)

    def show(self):
        print("\n=== MENÚ PRINCIPAL ===")
        for item in self.items:
            print(f"{item.key}. {item.description}")
        print("x. Salir")

    def run(self):
        while True:
            self.show()
            choice = input("Selecciona una opción: ").lower()
            if choice == 'x':
                print("Saliendo del sistema...")
                break
            found = False
            for item in self.items:
                if item.key == choice:
                    item.execute()
                    found = True
                    break
            if not found:
                print("Opción no válida. Intenta de nuevo.")
