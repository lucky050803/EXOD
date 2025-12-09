from player import Player
from dungeon import Dungeon
from save import save_game, load_game

class Game:
    def __init__(self):
        self.player = Player()
        self.dungeon = Dungeon()

    def enter_room(self):
        """Déclenche automatiquement l'événement d'une salle nouvelle"""
        room = self.dungeon.current_room()

        if room.visited:
            return "Cette salle a déjà été explorée."

        room.visited = True  # marquer la salle comme explorée
        
        return room.event.trigger(self.player)
    
    def enter_boss_room(self):
        """Déclenche automatiquement l'événement d'une salle nouvelle"""
        room = self.dungeon.current_room()

        if room.visited:
            return "Cette salle a déjà été explorée."

        room.visited = True  # marquer la salle comme explorée
        if room.event.trigger(self.player) == 0 :
            return 0
        else : return room.event.trigger(self.player)

    def save(self):
        save_game(self)

    def load(self):
        data = load_game()
        if not data:
            return
        self.player = Player.from_dict(data["player"])
