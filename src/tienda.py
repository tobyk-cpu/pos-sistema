class Tienda:
    def __init__(self):
        self.products = {}
        self.inventory = {}

    def add_product(self, product_id, product_name, price):
        self.products[product_id] = {'name': product_name, 'price': price}
        self.inventory[product_id] = 0  # Initialize inventory to 0

    def update_inventory(self, product_id, quantity):
        if product_id in self.inventory:
            self.inventory[product_id] += quantity
        else:
            print(f"Product ID {product_id} not found.")

    def sell_product(self, product_id, quantity):
        if product_id in self.inventory and self.inventory[product_id] >= quantity:
            self.inventory[product_id] -= quantity
            total_price = self.products[product_id]['price'] * quantity
            return total_price
        elif product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
        else:
            print(f"Not enough inventory for product {product_id}.")
        return 0

    def get_inventory(self):
        return self.inventory

    def get_products(self):
        return self.products
