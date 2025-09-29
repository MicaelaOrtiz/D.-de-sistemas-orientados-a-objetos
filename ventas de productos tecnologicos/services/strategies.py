from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, precio: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, precio: float) -> float:
        return precio

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply(self, precio: float) -> float:
        return precio * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply(self, precio: float) -> float:
        return max(precio - self.amount, 0)
