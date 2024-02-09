"""
переменная -> поле, свойство, атрибут
функция -> метод
"""
import random


class Human:
    population = 0

    def __init__(self, name: str = 'John',
                 age: int = 18, height: int | None = None):
        self.name = name
        self.age = age
        self.height = height
        if not self.height:
            self.height = random.randint(150, 200)

        Human.population += 1

    @staticmethod
    def adult_age(age: int) -> bool:
        return age >= 18

    def __str__(self) -> str:
        return f'name: {self.name}; age: {self.age}; height: {self.height}'

    def __repr__(self) -> str:
        return f'Human(name="{self.name}", age={self.age}, height={self.height})'

    def __len__(self) -> int:
        return self.height + self.age

    def __del__(self):
        # print(f"{self.name} is being destroyed")
        Human.population -= 1

    def __call__(self, action):
        print(f"{self.name} is {action}")

    def __gt__(self, other):
        if isinstance(other, Human):
            return self.age > other.age
        if isinstance(other, int):
            return self.age > other

    def __eq__(self, other):
        if isinstance(other, Human):
            return (self.name == other.name and
                    self.age == other.age and
                    self.height == other.height)
        return False

    def __add__(self, other):
        if isinstance(other, Human):
            return self.age + other.age
        return NotImplemented


human_1 = Human(name='John', age=18, height=100)
human_2 = Human(name='Bob', age=17)

# print(human_1 + human_2)
# print(human_1.__add__(human_2))

# print(human_1 > human_2)
# print(human_1 > 100)
# print(human_1.__gt__(human_2))

# print(human_1.__eq__(human_2))
