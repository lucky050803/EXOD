import tkinter as tk
from tkinter import messagebox
import random

class GameGUI:
    def __init__(self, game):
        self.game = game

        # --- Fenêtre principale ---
        self.root = tk.Tk()
        self.root.title("Mini RPG Amélioré")
        self.root.geometry("800x600")
        self.root.state('zoomed')
        
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

        self.map_cells = []
        for j in range(self.game.dungeon.size):
            row = []
            for i in range(self.game.dungeon.size):
                cell = tk.Label(
                    map_frame,
                    text="  ",
                    width=2,
                    height=1,
                    bg="#555555",
                    fg="white",
                    font=("Consolas", 16),
                    bd=1,
                    relief="solid"
                )
                cell.grid(row=j, column=i, padx=1, pady=1)
                row.append(cell)
            self.map_cells.append(row)


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

        btn("↑", lambda: self.move(0, -1)).grid(row=0, column=1)
        btn("←", lambda: self.move(-1, 0)).grid(row=1, column=0)
        btn("→",  lambda: self.move(1, 0)).grid(row=1, column=2)
        btn("↓",  lambda: self.move(0, 1)).grid(row=2, column=1)

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
        act("Sortir", self.sortir).pack(side="left", padx=5)

        # Premier affichage
        self.show("Bienvenue dans le donjon !")
        self.update_map()
        self.update_stats()

        # Boss
        position = random.randint(1, 4)
        if position == 1:
            self.boss_posx = 0
            self.boss_posy = 0
        if position == 2:
            self.boss_posx = self.game.dungeon.size 
            self.boss_posy = 0
        if position == 3:
            self.boss_posx = 0
            self.boss_posy = self.game.dungeon.size
        if position == 4:
            self.boss_posx = self.game.dungeon.size
            self.boss_posy = self.game.dungeon.size
        self.game.dungeon.generate_grid_boss_room(self.boss_posx,self.boss_posy)
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

        for j in range(size):
            for i in range(size):
                cell = self.map_cells[j][i]

                if i == d.player_x and j == d.player_y:
                    cell.config(bg="#00AAFF")   # couleur du joueur
                else:
                    cell.config(bg="#555555")   # couleur normale


    # ===============================================
    #        LOGIQUE DES BOUTONS
    # ===============================================

    def move(self, dx, dy):
        if self.game.dungeon.move(dx, dy) :
            
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
        
    def sortir(self):
        return 0
