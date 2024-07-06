class Employee:
    # Вместо инструкции pass напишите свой код.
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name='Роберт', second_name='Крузо', gender='м')
employee2 = Employee(first_name='Taylor', second_name='Swift', gender='ж')

# Допишите код для вывода информации о сотрудниках.
print(f'Имя: {employee1.first_name}, '
      f'Фамилия: {employee1.second_name}, '
      f'Пол: {employee1.gender}, '
      f'Отпускных дней в году: {Employee.vacation_days}.')
print(f'Имя: {employee2.first_name}, '
      f'Фамилия: {employee2.second_name}, '
      f'Пол: {employee2.gender}, '
      f'Отпускных дней в году: {Employee.vacation_days}.')
