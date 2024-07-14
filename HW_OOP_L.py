class Product:
    # Опишите инициализатор класса и метод get_info()
    def __init__(self, name, amount) -> None:
        self.product_name = name
        self.product_amount = amount

    def get_info(self):
        return f'{self.product_name} (в наличии: {self.product_amount})'


class Kettlebell(Product):
    # Опишите инициализитор класса и метод get_weight()
    def __init__(self, name, amount, weight) -> None:
        super().__init__(name, amount)
        self.product_weight = weight

    def get_weight(self):
        return (f'{self.product_name} (в наличии: {self.product_amount}) '
                f'Вес: {self.product_weight} кг')


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    def __init__(self, name, amount, size) -> None:
        super().__init__(name, amount)
        self.product_size = size

    def get_size(self):
        return (f'{self.product_name} (в наличии: {self.product_amount}) '
                f'Размер: {self.product_size}')


# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
