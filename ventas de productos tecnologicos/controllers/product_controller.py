from repositories.product_repository import ProductRepository
from services.discount_context import DiscountContext
from services.strategies import NoDiscount, PercentageDiscount, FixedDiscount
from views.product_view import ProductView

class ProductController:
    def __init__(self):
        self.repo = ProductRepository()
        self.context = DiscountContext(NoDiscount())

    def list_products(self):
        products = self.repo.list_all()
        ProductView.show_products(products)

    def show_product(self, product_id, strategy_type="none"):
        product = self.repo.get_by_id(product_id)
        if not product:
            print("Producto no encontrado")
            return

        # Estrategias disponibles
        if strategy_type == "percentage":
            self.context.set_strategy(PercentageDiscount(10))  
        elif strategy_type == "fixed":
            self.context.set_strategy(FixedDiscount(500))  
        else:
            self.context.set_strategy(NoDiscount())

        final_precio = self.context.apply_discount(product.precio)
        ProductView.show_product(product, final_precio)
