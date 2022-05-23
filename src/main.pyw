import tkinter as tk
from grid import *

window = tk.Tk()
window.iconphoto(False, tk.PhotoImage(file="src/assets/image.png"))
window.title(string="Primitivas Gráficas")

grid = Grid(window, 40, 400)

containerLaunchers = tk.Frame(window)
btnBresenham = tk.Button(containerLaunchers, text="Bresenham", command=lambda: grid.bres())
btnCircle = tk.Button(containerLaunchers, text="Circulo", command=lambda: grid.cricle())
btnBezier = tk.Button(containerLaunchers, text="Curva", command=lambda: grid.curve())
btnPolyline = tk.Button(containerLaunchers, text="Polilinha", command=lambda: grid.polyline())
btnClean = tk.Button(window, text="Limpar", command=grid.clear)

btnBresenham.grid(row=1, column=1, sticky='nesw')
btnCircle.grid(row=1, column=2, sticky='nesw')
btnBezier.grid(row=1, column=3, sticky='nesw')
btnPolyline.grid(row=2, column=1, sticky='nesw')

btnClean.pack()
containerLaunchers.pack(padx=5, pady=5)

window.mainloop()