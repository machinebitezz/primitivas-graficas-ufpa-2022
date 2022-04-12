import tkinter as tk
from wrappers import *

window = tk.Tk()
window.iconphoto(False, tk.PhotoImage(file="src/assets/image.png"))
window.title(string="Primitivas Gráficas")
containerInputs = tk.Frame()
labelPixelSizeX = tk.Label(containerInputs, text='Tamanho X do pixel:')
labelPixelSizeY = tk.Label(containerInputs, text='Tamanho Y do pixel:')
pixelSizeX = tk.Entry(containerInputs)
pixelSizeY = tk.Entry(containerInputs)

labelNumPixelsX = tk.Label(containerInputs, text="Numero de Pixels X:")
labelNumPixelsY = tk.Label(containerInputs, text="Numero de Pixels Y:")
numPixelsX = tk.Entry(containerInputs)
numPixelsY = tk.Entry(containerInputs)

pixelSizeX.insert(0, '15')
pixelSizeY.insert(0, '15')
numPixelsX.insert(0, '70')
numPixelsY.insert(0, '45')

labelPixelSizeX.grid(row=1, column=1,  pady=(3, 0))
labelPixelSizeY.grid(row=2, column=1, pady=(3, 0))
pixelSizeX.grid(row=1, column=2, pady=(3, 0))
pixelSizeY.grid(row=2, column=2, pady=(3, 0))

labelNumPixelsX.grid(row=3, column=1, pady=(3, 0))
labelNumPixelsY.grid(row=4, column=1, pady=(3, 0))
numPixelsX.grid(row=3, column=2, pady=(3, 0))
numPixelsY.grid(row=4, column=2, pady=(3, 0))

containerInputs.pack(padx=5, pady=5)

drawGrid = tk.IntVar()
drawGrid.set(1)

configTuple = (pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid)

containerLaunchers = tk.Frame(window)
btnPixelPainter = tk.Button(containerLaunchers, text="Ponto", command=lambda: cPixelPainter(configTuple))
btnBresenham = tk.Button(containerLaunchers, text="Bresenham", command=lambda: cBresenham(configTuple))
btnSquare = tk.Button(containerLaunchers, text="Retangulo", command=lambda: cSquare(configTuple))
btnTriangle = tk.Button(containerLaunchers, text="Triangulo", command=lambda: cTriangle(configTuple))
btnCircle = tk.Button(containerLaunchers, text="Circulo", command=lambda: cCircle(configTuple))

btnPixelPainter.grid(row=1, column=1, sticky='nesw')
btnBresenham.grid(row=1, column=2, sticky='nesw')
btnSquare.grid(row=1, column=3, sticky='nesw')
btnTriangle.grid(row=2, column=1, sticky='nesw')
btnCircle.grid(row=2, column=2, sticky='nesw')

containerLaunchers.pack(padx=5, pady=5)

drawGridCheck = tk.Checkbutton(window, text='Desenhar Grade', onvalue=1, offvalue=0, variable=drawGrid)
drawGridCheck.pack()

window.mainloop()