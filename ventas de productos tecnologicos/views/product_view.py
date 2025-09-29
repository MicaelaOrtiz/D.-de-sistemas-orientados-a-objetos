class ProductView:
    @staticmethod
    def show_product(product, final_precio=None):
        print(f"\nProducto: {product.name}")
        print(f"Precio base: ${product.price:,.2f}")
        if final_precio is not None:
            print(f"Precio con descuento aplicado: ${final_precio:,.2f}")

    @staticmethod
    def show_products(products):
        print("\nListado de productos:")
        for p in products:
            print(f"{p.id}. {p.name} - ${p.precio:,.2f}")

