class BacteriaProducer:
    # Допишите инициализатор класса
    def __init__(self, max_bacteria):
        self.max_bacteria = max_bacteria
        self.total_bacteria = 0

    # Допишите метод
    def create_new(self):
        if (self.total_bacteria + 1) > self.max_bacteria:
            print('Нет места под новую бактерию')
        else:
            self.total_bacteria += 1
            print(f'Добавлена одна бактерия. '
                  f'Количество бактерий в популяции: {self.total_bacteria}')

    # Допишите метод
    def remove_one(self):
        if (self.total_bacteria - 1) < 0:
            print('В популяции нет бактерий, удалять нечего')
        else:
            self.total_bacteria -= 1
            print(f'Одна бактерия удалена. '
                  f'Количество бактерий в популяции: {self.total_bacteria}')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
