import random
from rooms import generate_room, generate_boss_room

class Dungeon:
    def __init__(self, size=5):
        self.size = size
        self.grid = [[generate_room() for _ in range(size)] for _ in range(size)]
        self.player_x = size // 2
        self.player_y = size // 2

    def move(self, dx, dy):
        nx = self.player_x + dx
        ny = self.player_y + dy

        if 0 <= nx < self.size and 0 <= ny < self.size:
            self.player_x = nx
            self.player_y = ny
            return True
        return False

    def current_room(self):
        return self.grid[self.player_y][self.player_x]
    
    def generate_grid_boss_room(self,x,y):
        self.grid[x-1][y-1] = generate_boss_room()

