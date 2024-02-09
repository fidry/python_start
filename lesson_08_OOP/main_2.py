class Weapon:
    def fire(self):
        pass


class Pistol(Weapon):
    def fire(self):
        print("пиф-паф")


class Bazooka(Weapon):
    def fire(self):
        print("бабах")


class Human:
    def shoot(self, weapon: Weapon):
        print('Человек стреляет: ', end='')
        weapon.fire()


pistol = Pistol()
# pistol.fire()

bazooka = Bazooka()
# bazooka.fire()

human = Human()
# human.shoot(weapon=pistol)
human.shoot(weapon=bazooka)
