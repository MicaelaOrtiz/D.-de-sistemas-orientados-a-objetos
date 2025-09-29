class DiscountContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def apply_discount(self, precio: float) -> float:
        return self._strategy.apply(precio)
