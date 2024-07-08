# Родительский класс.
class Phone:

    # Атрибут базового класса.
    line_type = 'проводной'

    # Инициализатор базового класса.
    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    # Метод базового класса.
    def ring(self):
        print('Дзззззыыыыыыыынь!')

    # Ещё один метод базового класса.
    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


# Дочерний класс, унаследованный от класса Phone.
class MobilePhone(Phone):

    line_type = 'беспроводной'

    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        self.network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзинь-дзинь!')

    def start_game(self):
        print('Игра запущена!')


rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный', 'LTE')

print(rotary_phone.line_type)

rotary_phone.ring()

print(mobile_phone.line_type)
print(mobile_phone.battery_type)
print(mobile_phone.network_type)

mobile_phone.ring()

mobile_phone.start_game
