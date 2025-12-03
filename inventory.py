class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        return f"Objet obtenu : {item.name}"

    def use(self, player, index):
        item = self.items[index]
        if getattr(item, "consumable", False):
            res = item.use(player)
            self.items.pop(index)
            return res
        return "Cet objet ne peut pas être utilisé."
