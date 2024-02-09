'''
1) Создайте класс Car, который имеет атрибуты make (марка) и model (модель).
Реализуйте метод display_info(),
который выводит информацию о марке и модели автомобиля.
'''


class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Car: make: {self.make}; model: {self.model}')


a = Car(make='BMW', model='3')
b = Car(make='Lada', model='Largus')
a.display_info()
b.display_info()
