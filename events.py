import random
from ennemy import Enemy, BossEnemy, combat
from equipments import Sword, Shield
from itertools import cycle

class Event:
    def trigger(self, player):
        raise NotImplementedError

class CombatEvent(Event):
    def trigger(self, player):
        enemy = Enemy.random_enemy()
        log = combat(player, enemy)
        xp = random.randint(5, 12)
        log += f"\n💠 Vous gagnez {xp} XP."
        lvl = player.add_xp(xp)
        if lvl:
            log += "\n" + lvl
        return log

class BossEvent(Event):
    def trigger(self, player):
        boss = BossEnemy()
        log = combat(player, boss)
        xp = 50
        log += f"\n🔥 XP BOSS +{xp}"
        lvl = player.add_xp(xp)
        if lvl:
            log += "\n" + lvl
        return log

class TreasureEvent(Event):
    def trigger(self, player):
        loot = random.choice([Sword(), Shield()])
        player.inventory.add(loot)
        return f"Vous trouvez un coffre contenant : {loot.name}"

class TrapEvent(Event):
    def trigger(self, player):
        dmg = random.randint(3, 7)
        player.hp -= dmg
        return f"💥 Un piège ! Vous perdez {dmg} PV."

class HealEvent(Event):
    def trigger(self, player):
        heal = random.randint(5, 15)
        player.hp = min(player.max_hp, player.hp + heal)
        return f"✨ Une fontaine magique : +{heal} PV."

class MerchantEvent(Event):
    def trigger(self, player):
        if player.merchant_used:
            return "Le marchand vous salue, mais il n’a plus rien à vous offrir."

        upgrade = random.choice(["atk", "def"])

        player.merchant_used = True

        if upgrade == "atk":
            player.atk += 1
            return "Le marchand améliore votre arme : ATK +1"
        else:
            player.defense += 1
            return "Le marchand renforce votre armure : DEF +1"

