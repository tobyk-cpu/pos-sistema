class ItemCarrito:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def total(self):
        return self.precio * self.cantidad

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def eliminar_item(self, nombre):
        self.items = [item for item in self.items if item.nombre != nombre]

    def total_carrito(self):
        return sum(item.total() for item in self.items)

    def __str__(self):
        return '\n'.join([f'{item.nombre}: {item.cantidad} x {item.precio} = {item.total()}' for item in self.items])