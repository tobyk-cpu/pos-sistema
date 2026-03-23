# Complete POS System Code

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity):
        self.items[item_name] = {'price': price, 'quantity': quantity}

    def update_item(self, item_name, price=None, quantity=None):
        if item_name in self.items:
            if price is not None:
                self.items[item_name]['price'] = price
            if quantity is not None:
                self.items[item_name]['quantity'] = quantity

    def get_items(self):
        return self.items


class Sales:
    def __init__(self, inventory):
        self.inventory = inventory
        self.sales_records = []

    def record_sale(self, item_name, quantity):
        if item_name in self.inventory.get_items() and self.inventory.get_items()[item_name]['quantity'] >= quantity:
            total_price = self.inventory.get_items()[item_name]['price'] * quantity
            self.sales_records.append({'item': item_name, 'quantity': quantity, 'total_price': total_price})
            self.inventory.update_item(item_name, quantity=self.inventory.get_items()[item_name]['quantity'] - quantity)
            return total_price
        else:
            return None


class Reporting:
    def __init__(self, sales):
        self.sales = sales

    def generate_report(self):
        report = "Sales Report:\n"
        total_sales = 0
        for record in self.sales.sales_records:
            report += f"Item: {record['item']}, Quantity: {record['quantity']}, Total: {record['total_price']}\n"
            total_sales += record['total_price']
        report += f"Total sales amount: {total_sales}\n"
        return report


# Example of using the POS system
inventory = Inventory()
inventory.add_item('Apple', 0.5, 100)
inventory.add_item('Banana', 0.3, 150)

sales = Sales(inventory)
sales.record_sale('Apple', 2)
sales.record_sale('Banana', 3)

reporting = Reporting(sales)
print(reporting.generate_report())
