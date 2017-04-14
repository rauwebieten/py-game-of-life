import src.gameoflife as game
import tkinter as tk

game_map = game.Map(20, 10)
for i in range(3):
    game_map.map[1][i] = 1

window = tk.Tk()
canvas = tk.Canvas(window, bg='white')

renderer = game.CanvasRenderer(canvas)
renderer.render(game_map)

autorun = False


def stop_action():
    global autorun
    autorun = False


def start_action():
    global autorun
    autorun = True


def step_action():
    game_map.step()
    renderer.render(game_map)


button_step = tk.Button(window, text='step', command=step_action)
button_start = tk.Button(window, text='start', command=start_action)
button_stop = tk.Button(window, text='stop', command=stop_action)
# button_clear = tk.Button(window, text='clear', command=step_action)

button_step.grid(row=0, column=2)
button_start.grid(row=0, column=3)
button_stop.grid(row=0, column=4)
# button_clear.grid(row=0, column=5)
canvas.grid(row=1, column=0, columnspan=6)

while True:
    if autorun:
        step_action()
    window.update_idletasks()
    window.update()
