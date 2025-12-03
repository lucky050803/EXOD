from inventory import Inventory
from equipments import Sword, Shield

class Player:
    def __init__(self, name="Héros", hp=40, atk=5, defense=2):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.defense = defense
        self.xp = 0
        self.level = 1
        self.merchant_used = False

        self.inventory = Inventory()

        self.weapon = Sword()
        self.shield = Shield()

    @property
    def attack_value(self):
        return self.atk + self.weapon.bonus

    @property
    def defense_value(self):
        return self.defense + self.shield.bonus

    def add_xp(self, amount):
        self.xp += amount
        needed = 20 + self.level * 10

        if self.xp >= needed:
            self.level += 1
            self.max_hp += 5
            self.atk += 1
            self.defense += 1
            self.hp = self.max_hp
            self.xp -= needed
            return f"🎉 Niveau {self.level} atteint ! PV+5 ATK+1 DEF+1"
        return None
