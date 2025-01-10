from enum import Enum


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} costs {self.price}'


class FoodProduct(Product):
    def __init__(self, name, price, expiration_date, is_vegan):
        super().__init__(name, price)
        self.expiration_date = expiration_date
        self.is_vegan = is_vegan

    def __str__(self):
        return f'{super().__str__()}, expires on {self.expiration_date} and {"is" if self.is_vegan else "is not"} vegan'


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period, power_usage):
        super().__init__(name, price)
        self.warranty_period = warranty_period
        self.power_usage = power_usage

    def __str__(self):
        return f'{super().__str__()}, warranty period: {self.warranty_period}, power usage: {self.power_usage}'


class Cart:
    def __init__(self):
        self._products = []

    def get_products(self):
        return self._products

    def add_product(self, prod):
        self._products.append(prod)

    def remove_product(self, prod):
        self._products.remove(prod)

    def get_total_price(self):
        return sum([int(prod.price) for prod in self._products])

    def __str__(self):
        product_list = ", ".join(str(prod) for prod in self._products)
        return f'Cart: {product_list}, total_price:{self.get_total_price()}'


class OrderStatus(Enum):
    PENDING = "PENDING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"


class Order:
    def __init__(self, phone_number):
        self.cart = Cart()
        self.status = OrderStatus.PENDING
        self.phone_number = phone_number

    def place_order(self):
        self.status = OrderStatus.SHIPPED

    def cancel_order(self):
        self.status = OrderStatus.CANCELED

    def __str__(self):
        return f'Order status: {self.status}, phone_number:{self.phone_number}, cart={self.cart}'


product = Product('banana', '10')
cart = Cart()
cart.add_product(product)
print(cart
      )
