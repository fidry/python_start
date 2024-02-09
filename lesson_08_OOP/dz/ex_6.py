'''
Создайте игру "Магазин животных".
Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена),
а также методом sound(), который возвращает звук, издаваемый животным.
От него унаследуйте классы Dog, Cat и Bird,
каждый из которых переопределяет метод sound() для возврата соответствующего звука для каждого типа животного.
Класс Shop должен иметь атрибуты animals (список доступных животных)
и budget (бюджет магазина),

а также методы buy_animal(animal) для покупки животного и
sell_animal(animal) для продажи животного.

Реализуйте проверки наличия достаточного бюджета у магазина для покупки и наличия животного в магазине для продажи.
'''


class Animal:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def sound(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'


class Dog(Animal):
    def sound(self):
        print('гав-гав')


class Cat(Animal):
    def sound(self):
        print('мяу')


class Bird(Animal):
    def sound(self):
        print('чик-чирык')


class Shop:
    def __init__(self, animals: list[Animal], budget: float):
        self.animals = animals
        self.budget = budget

    def buy_animal(self, animal: Animal):
        # проверки наличия достаточного бюджета у магазина для покупки
        if animal.price <= self.budget:
            self.animals.append(animal)
            self.budget -= animal.price
        else:
            print('недостаточный бюджет')

    def sell_animal(self, animal: Animal):
        # наличия животного в магазине для продажи.
        if animal in self.animals:
            self.animals.remove(animal)
            self.budget += animal.price
        else:
            print(f'Животного {animal.name} нет в магазине')

    def __str__(self):
        return f'{self.animals} | {self.budget}'


d = Dog(name='John', price=100_000_000)
c = Cat(name='Bob', price=100_500_000)
b = Bird(name='Чикчирык', price=10_000_000)

shop = Shop(animals=[d], budget=100_500_000)
print(shop)
shop.buy_animal(c)
print(shop)
shop.sell_animal(animal=d)
print(shop)
shop.buy_animal(b)
print(shop)
