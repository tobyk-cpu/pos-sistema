class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            raise ValueError('Stock insuficiente')

    def aumentar_stock(self, cantidad):
        self.stock += cantidad
