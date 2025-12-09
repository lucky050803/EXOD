import random
from rooms import generate_room, generate_boss_room

class Dungeon:
    def __init__(self, size=5):
        self.size = size
        self.grid = [[generate_room() for _ in range(size)] for _ in range(size)]
        self.player_x = size // 2
        self.player_y = size // 2
        position = random.randint(1, 4)
        print(position)
        if position == 1:
            self.boss_posx = 0
            self.boss_posy = 0
        if position == 2:
            self.boss_posx = size -1
            self.boss_posy = 0
        if position == 3:
            self.boss_posx = 0
            self.boss_posy = size -1
        if position == 4:
            self.boss_posx = size -1
            self.boss_posy = size -1
        self.generate_grid_boss_room(self.boss_posx,self.boss_posy)

    def move(self, dx, dy):
        nx = self.player_x + dx
        ny = self.player_y + dy

        if 0 <= nx < self.size and 0 <= ny < self.size:
            self.player_x = nx
            self.player_y = ny
            return True
        return False
    #def reset_pos(self):
        
    def current_room(self):
        return self.grid[self.player_y][self.player_x]
    
    def generate_grid_boss_room(self,x,y):
        self.grid[y][x] = generate_boss_room()

