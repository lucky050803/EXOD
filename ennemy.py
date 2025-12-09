import random

class Enemy:
    def __init__(self, name="Gobelin", hp=10, atk=3, defense=1, xp_gain=10):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.xp_gain = xp_gain

    def attack(self, player):
        dmg = max(1, self.atk - player.defense_value)
        player.hp -= dmg
        return dmg

    @staticmethod
    def random_enemy():
        enemies = [
            Enemy("Gobelin", 10, 3, 1, xp_gain=8),
            Enemy("Orc", 20, 5, 2, xp_gain=15),
            Enemy("Squelette", 12, 4, 2, xp_gain=12),
        ]
        return random.choice(enemies)


class BossEnemy(Enemy):
    def __init__(self):
        super().__init__(name="Ogre Colossal", hp=40, atk=10, defense=3, xp_gain=50)


def combat(player, enemy):
    log = []

    while player.hp > 0 and enemy.hp > 0:
        # Joueur attaque
        dmg = max(1, player.attack_value - enemy.defense)
        enemy.hp -= dmg
        log.append(f"🗡️ Vous infligez {dmg} dégâts à {enemy.name}.")

        if enemy.hp <= 0:
            log.append(f"🏆 {enemy.name} est vaincu !")
            return "\n".join(log)

        # Ennemi attaque
        dmg = enemy.attack(player)
        log.append(f"💥 {enemy.name} vous inflige {dmg} dégâts.")

        if player.hp <= 0:
            log.append("☠️ Vous êtes mort…")
            return "\n".join(log)

    return "\n".join(log)
