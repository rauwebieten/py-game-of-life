import numpy as np


class Map:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.map = np.zeros((self.height, self.width), dtype=np.int16)
        self.current_step = 1

    def clear(self):
        self.map = np.zeros((self.height, self.width), dtype=np.int16)
        self.current_step = 1

    def step(self):
        new_map = np.zeros((self.height, self.width), dtype=np.int16)
        for yi in range(self.height):
            for xi in range(self.width):
                value = self.map[yi][xi]
                neighbors = self.neighbors(xi, yi)
                if value == 1:
                    new_map[yi][xi] = 1 if (neighbors == 2 or neighbors == 3) else 0
                else:
                    new_map[yi][xi] = 1 if neighbors == 3 else 0
        self.map = new_map
        self.current_step += 1

    def steps(self, quantity):
        for i in range(quantity):
            self.step()

    def neighbors(self, x, y):
        count = 0
        ry = range(max(0, y - 1), 1 + min(self.height - 1, y + 1))
        rx = range(max(0, x - 1), 1 + min(self.width - 1, x + 1))
        for dy in ry:
            for dx in rx:
                count += self.map[dy][dx]
        count -= self.map[y][x]
        return count


class CanvasRenderer:
    def __init__(self, canvas, the_map):
        self.canvas = canvas
        self.cell_size = 5
        self.map = the_map

        self.canvas.bind('<Button-1>', self.on_cell_click)

    def on_cell_click(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        self.toggle_cell(x, y)

    def toggle_cell(self, x, y):
        self.map.map[y][x] = 1 - self.map.map[y][x]
        self.render()

    def render(self):
        self.canvas.config(width=self.map.width * self.cell_size, height=self.map.height * self.cell_size)
        self.canvas.delete("all")
        for yi in range(self.map.height):
            for xi in range(self.map.width):
                value = self.map.map[yi][xi]
                if value == 1:
                    self.canvas.create_rectangle(xi * self.cell_size, yi * self.cell_size,
                                                 xi * self.cell_size + self.cell_size,
                                                 yi * self.cell_size + self.cell_size, fill="black")
