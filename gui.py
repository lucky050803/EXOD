import tkinter as tk
from tkinter import messagebox

class GameGUI:
    def __init__(self, game):
        self.game = game

        # --- Fenêtre principale ---
        self.root = tk.Tk()
        self.root.title("Mini RPG Amélioré")
        self.root.geometry("800x600")
        self.root.configure(bg="#222222")

        self.font = ("Consolas", 11)

        # --- Cadre principal ---
        container = tk.Frame(self.root, bg="#222222")
        container.pack(expand=True, fill="both", padx=10, pady=10)

        # ============================
        #        CARTE + STATS
        # ============================
        top_frame = tk.Frame(container, bg="#222222")
        top_frame.pack(fill="x")

        # CARTE
        map_frame = tk.LabelFrame(top_frame, text="Carte", font=self.font,
                                  fg="white", bg="#333333", bd=2)
        map_frame.pack(side="left", padx=10)

        self.map_label = tk.Label(map_frame, text="", font=("Consolas", 14),
                                  fg="white", bg="#333333", justify="left")
        self.map_label.pack(padx=10, pady=10)

        # STATISTIQUES
        stats_frame = tk.LabelFrame(top_frame, text="Statistiques", font=self.font,
                                    fg="white", bg="#333333", bd=2)
        stats_frame.pack(side="right", padx=10)

        self.stats_label = tk.Label(stats_frame, text="", font=self.font,
                                    fg="white", bg="#333333", justify="left")
        self.stats_label.pack(padx=10, pady=10)

        # ============================
        #      ZONE DE TEXTE
        # ============================
        self.text_frame = tk.LabelFrame(container, text="Journal", font=self.font,
                                        fg="white", bg="#333333", bd=2)
        self.text_frame.pack(pady=10, fill="both", expand=True)

        self.text = tk.Text(self.text_frame, width=60, height=14,
                            wrap="word", bg="#222222", fg="white",
                            insertbackground="white", font=self.font)
        self.text.pack(expand=True, fill="both", padx=10, pady=10)

        # ============================
        #   COMMANDES + DÉPLACEMENT
        # ============================

        bottom_frame = tk.Frame(container, bg="#222222")
        bottom_frame.pack(fill="x", pady=10)

        # Déplacements
        move_frame = tk.Frame(bottom_frame, bg="#222222")
        move_frame.pack(side="left", padx=10)

        def btn(text, cmd):
            return tk.Button(move_frame, text=text, command=cmd, font=self.font,
                             bg="#444444", fg="white", activebackground="#555555",
                             width=8)

        btn("Nord", lambda: self.move(0, -1)).grid(row=0, column=1)
        btn("Ouest", lambda: self.move(-1, 0)).grid(row=1, column=0)
        btn("Est",  lambda: self.move(1, 0)).grid(row=1, column=2)
        btn("Sud",  lambda: self.move(0, 1)).grid(row=2, column=1)

        # Actions
        action_frame = tk.Frame(bottom_frame, bg="#222222")
        action_frame.pack(side="right", padx=10)

        def act(text, cmd):
            return tk.Button(action_frame, text=text, command=cmd,
                             font=self.font, bg="#333366", fg="white",
                             activebackground="#444488", width=12)

        act("Inventaire", self.open_inventory).pack(side="left", padx=5)
        act("Sauver", self.save).pack(side="left", padx=5)
        act("Charger", self.load).pack(side="left", padx=5)

        # Premier affichage
        self.show("Bienvenue dans le donjon !")
        self.update_map()
        self.update_stats()

    # ===============================================
    #   FONCTIONS D'AFFICHAGE
    # ===============================================

    def show(self, msg):
        self.text.insert(tk.END, msg + "\n\n")
        self.text.see(tk.END)

    def update_stats(self):
        p = self.game.player
        self.stats_label.config(text=(
            f"HP : {p.hp}/{p.max_hp}\n"
            f"LVL : {p.level}\n"
            f"XP : {p.xp}\n"
            f"ATK : {p.attack_value}\n"
            f"DEF : {p.defense_value}"
        ))

    def update_map(self):
        d = self.game.dungeon

        size = d.size
        x, y = d.player_x, d.player_y

        rows = []
        for j in range(size):
            row = []
            for i in range(size):
                if i == x and j == y:
                    row.append("🧍")  # joueur
                else:
                    row.append("□")
            rows.append(" ".join(row))

        self.map_label.config(text="\n".join(rows))

    # ===============================================
    #        LOGIQUE DES BOUTONS
    # ===============================================

    def move(self, dx, dy):
        if self.game.dungeon.move(dx, dy):

            room = self.game.dungeon.current_room()
            self.show(f"Nouvelle salle : {room.description}")

            # Déclenchement automatique de l'événement
            event_text = self.game.enter_room()
            self.show(event_text)

            self.update_map()
            self.update_stats()
        else:
            self.show("Impossible d'aller dans cette direction.")

    # INVENTAIRE
    def open_inventory(self):
        win = tk.Toplevel(self.root)
        win.title("Inventaire")
        win.configure(bg="#222222")

        inv = self.game.player.inventory.items

        if not inv:
            tk.Label(win, text="Inventaire vide.", fg="white", bg="#222222",
                     font=self.font).pack(padx=20, pady=20)
            return

        for i, item in enumerate(inv):
            tk.Button(
                win,
                text=f"{item.name}",
                font=self.font,
                bg="#444444", fg="white",
                width=30,
                command=lambda i=i: self.use_item(i, win)
            ).pack(pady=3, padx=10)

    def use_item(self, index, window):
        p = self.game.player
        inv = p.inventory
        result = inv.use(p, index)
        self.show(result)
        window.destroy()
        self.update_stats()

    # SAUVEGARDE
    def save(self):
        self.game.save()
        messagebox.showinfo("Sauvegarde", "Partie sauvegardée.")

    # CHARGEMENT
    def load(self):
        self.game.load()
        self.update_stats()
        self.update_map()
        self.show("Partie chargée.")

    def run(self):
        self.root.mainloop()
