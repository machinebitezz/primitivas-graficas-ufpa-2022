import tkinter as tk
from grid import *

window = tk.Tk()
window.iconphoto(False, tk.PhotoImage(file="src/assets/image.png"))
window.title(string="Primitivas Gráficas")

grid = Grid(window, 40, 400)

containerLaunchers = tk.Frame(window)
btnBresenham = tk.Button(containerLaunchers, text="Bresenham", command=lambda: grid.bres())
btnCircle = tk.Button(containerLaunchers, text="Circulo", command=lambda: grid.cricle())
btnEllipsis = tk.Button(containerLaunchers, text="Elipse", command=lambda: grid.ellipsis())
btnBezier = tk.Button(containerLaunchers, text="Curva", command=lambda: grid.curve())
btnPolyline = tk.Button(containerLaunchers, text="Polilinha", command=lambda: grid.polyline())
btnSweepF = tk.Button(containerLaunchers, text="Preenchimento (varredura)", command=lambda: grid.sweepFill())
btnRecursiveFill = tk.Button(containerLaunchers, text="Preenchimento (recursivo)", command=lambda: grid.recursiveFill())
btnClip = tk.Button(containerLaunchers, text="Recorte", command=lambda: grid.adjustClippingBox())
btnTranslate = tk.Button(containerLaunchers, text="Translação", command=lambda: grid.translate())
btnScale = tk.Button(containerLaunchers, text="Escala", command=lambda: grid.scale())
btnRotate = tk.Button(containerLaunchers, text="Rotação", command=lambda: grid.rotate())
btnClean = tk.Button(window, text="Limpar", command=grid.clear)

btnBresenham.grid(row=1, column=1, sticky='nesw')
btnCircle.grid(row=1, column=2, sticky='nesw')
btnEllipsis.grid(row=1, column=3, sticky='nesw')
btnBezier.grid(row=2, column=1, sticky='nesw')
btnPolyline.grid(row=2, column=2, sticky='nesw')
btnSweepF.grid(row=2, column=3, sticky='nesw')
btnRecursiveFill.grid(row=3, column=1, sticky='nesw')
btnClip.grid(row=3, column=2, sticky='nesw')
btnTranslate.grid(row=3, column=3, sticky='nesw')
btnScale.grid(row=4, column=1, sticky='nesw')
btnRotate.grid(row=4, column=2, sticky='nesw')

btnClean.pack()
containerLaunchers.pack(padx=5, pady=5)

window.mainloop()