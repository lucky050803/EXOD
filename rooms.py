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

    # 5 % de chance d'engendrer un boss
    if random.random() < 0.05:
        return 

    return Room(random.choice(descriptions), random.choice(events))
