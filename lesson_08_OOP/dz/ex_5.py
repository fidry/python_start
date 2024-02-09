'''
Создайте систему регистрации на конференцию.
Реализуйте классы Conference (конференция), Participant (участник) и
RegistrationSystem (система регистрации).
Класс Conference должен иметь атрибуты name (название) и capacity (вместимость),
класс Participant - атрибуты name (имя) и email (электронная почта),
а класс RegistrationSystem - атрибуты conference (конференция) и participants (список участников),
а также методы register(participant) для регистрации участника и
is_registration_available() для проверки доступности регистрации на конференцию.
Реализуйте проверку наличия свободных мест на конференции перед регистрацией.
'''


class Conference:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity


class Participant:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email

    def __str__(self):
        return f'name: {self.name}; email: {self.email}'

    def __repr__(self):
        return f'name: {self.name}; email: {self.email}'


class RegistrationSystem:
    def __init__(self, conference: Conference, participants: list[Participant]):
        self.conference = conference
        self.participants = participants

    def register(self, participant: Participant):
        if len(self.participants) >= self.conference.capacity:
            print(f'на конференции {self.conference.name} уже максимальное количество участников')
            return
        if participant in self.participants:
            print(f'Участник {participant} уже зарегестрирован')
            return
        self.participants.append(participant)

    def is_registration_available(self, participant: Participant) -> bool:
        if participant in self.participants:
            return True
        return False


c = Conference(name='conf_1', capacity=3)
p1 = Participant(name='p1', email='e1')
p2 = Participant(name='p2', email='e2')
p3 = Participant(name='p3', email='e3')
p4 = Participant(name='p4', email='e4')

rs = RegistrationSystem(conference=c, participants=[p1, p2])
# print(rs.is_registration_available(participant=p1))
# print(rs.is_registration_available(participant=p2))
# print(rs.is_registration_available(participant=p3))
rs.register(participant=p3)
rs.register(participant=p4)
print(rs.participants)
