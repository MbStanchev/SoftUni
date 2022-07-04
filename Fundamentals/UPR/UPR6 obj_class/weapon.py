class Weapon():
    def __init__(self, bullest):
        self.bullest = bullest

    def shoot(self):
        if self.bullest > 0:
            self.bullest -= 1
            return 'shooting...'
        else:
            return 'no bullets left'

    def __repr__(self):
        return f"Remaining bullets: {self.bullest}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
