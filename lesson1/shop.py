import datetime


class Product:
    def __init__(self, price, name, units, unique_code, discount=0.0):
        self.price = price
        self.name = name
        self.units = units
        self.unique_code = unique_code
        self.discount = discount

    def subtotal(self):
        # discount = self._find_discount()
        return self.price * (1 - self.discount)


class MondaySaleProduct(Product):
    def subtotal(self):
        today = datetime.date.today().isoweekday()
        if today == 4:
            return self.price / 2
        return self.price


class Cart:
    def __init__(self, items_list=None):
        if items_list is not None:
            self.items_list = items_list
        else:
            self.items_list = []

    def add_to_cart(self, product, quantity):
        self.items_list.append(dict(product=product, quantity=quantity))

    def calculate_total(self, discount=0.0):
        total = 0
        for item in self.items_list:
            product = item['product']
            quantity = item['quantity']
            total += product.subtotal() * quantity
        return total * (1 - discount)


# items_list -> {product, quant} {product2, quantity}
#                item               item
#                 item['item'] -> Product

if __name__ == '__main__':
    tomato = Product(price=80,
                     name="Red tomato",
                     units="kg",
                     unique_code="123wqe")
    bread = MondaySaleProduct(price=25,
                              name="White bread",
                              units="piece",
                              unique_code="432qsc",
                              discount=0.3)
    water = Product(price=30,
                    name="Sparkling Water",
                    units="piece",
                    unique_code="098eiu")
    # water._find_discount()
    cart = Cart()
    cart.add_to_cart(bread, 2)
    cart.add_to_cart(tomato, 0.6)
    print(cart.calculate_total(0.1))
