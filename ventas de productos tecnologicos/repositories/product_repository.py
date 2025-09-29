from models.product import Product

class ProductRepository:
    def __init__(self):
        self._products = {
            1: Product(1, "Notebook Lenovo IdeaPad 15\"", 720000),
            2: Product(2, "Smartphone Samsung Galaxy A55", 580000),
            3: Product(3, "Auriculares Inalámbricos JBL Tune", 95000),
            4: Product(4, "Mouse Logitech G305 Lightspeed", 45000),
            5: Product(5, "Monitor LG 24\" Full HD", 210000),
        }

    def list_all(self):
        return list(self._products.values())

    def get_by_id(self, id):
        return self._products.get(id)
