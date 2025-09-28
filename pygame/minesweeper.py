import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows=9, cols=9, mines=15):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.first_click = True
        self.reset_ui()

    def reset_ui(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        top = tk.Frame(self.master)
        top.pack(pady=4)
        self.mine_label = tk.Label(top, text=f"Mines: {self.mines}")
        self.mine_label.pack(side=tk.LEFT, padx=6)
        reset_btn = tk.Button(top, text="Reset", command=self.reset_game, width=8)
        reset_btn.pack(side=tk.LEFT, padx=6)
        self.status_label = tk.Label(top, text="")
        self.status_label.pack(side=tk.LEFT, padx=6)

        board = tk.Frame(self.master)
        board.pack()
        self.buttons = []
        self.revealed = [[False]*self.cols for _ in range(self.rows)]
        self.flagged = [[False]*self.cols for _ in range(self.rows)]
        self.mines_grid = [[0]*self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                b = tk.Button(board, width=2, height=1, font=(None, 12))
                b.grid(row=r, column=c)
                b.bind('<Button-1>', lambda e, rr=r, cc=c: self.on_left(rr, cc))
                b.bind('<Button-3>', lambda e, rr=r, cc=c: self.on_right(rr, cc))
                row.append(b)
            self.buttons.append(row)
        self.remaining = self.rows * self.cols - self.mines

    def reset_game(self):
        self.first_click = True
        self.reset_ui()
        self.status_label.config(text="")

    def place_mines(self, safe_r, safe_c):
        positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        exclude = []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                rr, cc = safe_r + dr, safe_c + dc
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    exclude.append((rr, cc))
        for e in exclude:
            if e in positions:
                positions.remove(e)
        mines_pos = random.sample(positions, self.mines)
        for (r, c) in mines_pos:
            self.mines_grid[r][c] = -1
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mines_grid[r][c] == -1:
                    continue
                count = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        rr, cc = r + dr, c + dc
                        if 0 <= rr < self.rows and 0 <= cc < self.cols:
                            if self.mines_grid[rr][cc] == -1:
                                count += 1
                self.mines_grid[r][c] = count

    def on_left(self, r, c):
        if self.status_label.cget('text'):
            return
        if self.flagged[r][c] or self.revealed[r][c]:
            return
        if self.first_click:
            self.place_mines(r, c)
            self.first_click = False
        if self.mines_grid[r][c] == -1:
            self.reveal_mines()
            self.status_label.config(text="You lost")
            return
        self.reveal_cell(r, c)
        if self.remaining == 0:
            self.status_label.config(text="You won")
            self.reveal_all()

    def on_right(self, r, c):
        if self.status_label.cget('text'):
            return
        if self.revealed[r][c]:
            return
        if not self.flagged[r][c]:
            self.buttons[r][c].config(text='F')
            self.flagged[r][c] = True
        else:
            self.buttons[r][c].config(text='')
            self.flagged[r][c] = False

    def reveal_cell(self, r, c):
        if self.revealed[r][c] or self.flagged[r][c]:
            return
        self.revealed[r][c] = True
        self.buttons[r][c].config(relief=tk.SUNKEN, state=tk.DISABLED)
        val = self.mines_grid[r][c]
        if val == 0:
            self.buttons[r][c].config(text='')
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < self.rows and 0 <= cc < self.cols:
                        if not self.revealed[rr][cc]:
                            self.reveal_cell(rr, cc)
        else:
            self.buttons[r][c].config(text=str(val))
        self.remaining -= 1

    def reveal_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mines_grid[r][c] == -1:
                    self.buttons[r][c].config(text='M', relief=tk.SUNKEN, state=tk.DISABLED)

    def reveal_all(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.revealed[r][c]:
                    self.revealed[r][c] = True
                    val = self.mines_grid[r][c]
                    if val == -1:
                        self.buttons[r][c].config(text='M', relief=tk.SUNKEN)
                    elif val != 0:
                        self.buttons[r][c].config(text=str(val), relief=tk.SUNKEN)
                    self.buttons[r][c].config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Minesweeper')
    app = Minesweeper(root, rows=9, cols=9, mines=10)
    root.mainloop()
