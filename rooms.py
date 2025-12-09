import random
from events import CombatEvent, HealEvent, MerchantEvent, TreasureEvent, TrapEvent, BossEvent

class Room:
    def __init__(self, description, event):
        self.description = description
        self.event = event
        self.visited = False

def generate_room():
    descriptions = [
        "Une caverne humide.",
        "Un autel ancien.",
        "Une salle circulaire.",
        "Un couloir effondré.",
        "Une chambre rituelle.",
        "Une arène sombre."
    ]

    # Liste des événements possibles
    events = [
        CombatEvent(),
        HealEvent(),
        MerchantEvent(),
        TreasureEvent(),
        TrapEvent()
    ]

    return Room(random.choice(descriptions), random.choice(events))

def generate_boss_room():
    return Room(random.choice("Une salle gigantesque... un boss approche !"), BossEvent())
