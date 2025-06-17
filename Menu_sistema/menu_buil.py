from menu_item import MenuItem          # permite agregar opciones de forma encadenada y modular
from menu_sing import MenuSing

class MenuBuilder:
    def __init__(self):
        self.menu = MenuSing.get_instance()

    def add_option(self, key, description, action):
        item = MenuItem(key, description, action)
        self.menu.add_item(item)
        return self

    def build(self):
        return self.menu
