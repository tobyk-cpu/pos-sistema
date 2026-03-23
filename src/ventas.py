class Sale:
    def __init__(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price
        self.total = self.calculate_total()

    def calculate_total(self):
        return self.quantity * self.price


class SalesTransactionManager:
    def __init__(self):
        self.sales_records = []

    def process_sale(self, item, quantity, price):
        sale = Sale(item, quantity, price)
        self.sales_records.append(sale)
        print(f'Sale processed: {sale.item} - Quantity: {sale.quantity}, Total: ${sale.total:.2f}')

    def total_sales(self):
        return sum(sale.total for sale in self.sales_records)


# Example usage
if __name__ == '__main__':
    manager = SalesTransactionManager()
    manager.process_sale('Widget', 3, 19.99)
    manager.process_sale('Gadget', 2, 25.50)
    print(f'Total Sales: ${manager.total_sales():.2f}')