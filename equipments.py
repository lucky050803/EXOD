class Equipment:
    def __init__(self, name, bonus=0):
        self.name = name
        self.bonus = bonus
        self.consumable = False  # <-- tous les équipements ne sont pas consommables


class Sword(Equipment):
    def __init__(self):
        super().__init__("Épée rouillée", bonus=2)


class Shield(Equipment):
    def __init__(self):
        super().__init__("Bouclier en bois", bonus=1)


# =======================================
# Exemple d’objet consommable
# =======================================
class Potion:
    def __init__(self):
        self.name = "Potion de soin"
        self.heal_amount = 20
        self.consumable = True

    def use(self, player):
        player.hp = min(player.max_hp, player.hp + self.heal_amount)
        return f"Vous utilisez une potion et récupérez {self.heal_amount} PV."