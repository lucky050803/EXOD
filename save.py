import json
import os

SAVE_FILE = "save.json"

def save_game(game):
    data = {
        "player": game.player.to_dict()
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_game():
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r") as f:
        return json.load(f)
