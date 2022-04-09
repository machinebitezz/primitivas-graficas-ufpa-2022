import tkinter as tk
from threading import Thread
from grid import Grid

def cPixelPainter():
  global pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get()
  })

  def wrapper():
    draw.launchPixelPainter()

  t = Thread(target=wrapper)
  t.start()

def cBresenham():
  global pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get()
  })

  def wrapper():
    draw.launchBresenham()

  t = Thread(target=wrapper)
  t.start()

def cSquare():
  global pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get()
  })

  def wrapper():
    draw.launchSquares()

  t = Thread(target=wrapper)
  t.start()

def cTriangle():
  global pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get()
  })

  def wrapper():
    draw.launchTriangles()

  t = Thread(target=wrapper)
  t.start()

window = tk.Tk()
containerInputs = tk.Frame()
labelPixelSizeX = tk.Label(containerInputs, text='Tamanho X do pixel:')
labelPixelSizeY = tk.Label(containerInputs, text='Tamanho Y do pixel:')
pixelSizeX = tk.Entry(containerInputs)
pixelSizeY = tk.Entry(containerInputs)

labelNumPixelsX = tk.Label(containerInputs, text="Numero de Pixels X:")
labelNumPixelsY = tk.Label(containerInputs, text="Numero de Pixels Y:")
numPixelsX = tk.Entry(containerInputs)
numPixelsY = tk.Entry(containerInputs)

pixelSizeX.insert(0, '31')
pixelSizeY.insert(0, '31')
numPixelsX.insert(0, '50')
numPixelsY.insert(0, '40')

labelPixelSizeX.grid(row=1, column=1,  pady=(3, 0))
labelPixelSizeY.grid(row=2, column=1, pady=(3, 0))
pixelSizeX.grid(row=1, column=2, pady=(3, 0))
pixelSizeY.grid(row=2, column=2, pady=(3, 0))

labelNumPixelsX.grid(row=3, column=1, pady=(3, 0))
labelNumPixelsY.grid(row=4, column=1, pady=(3, 0))
numPixelsX.grid(row=3, column=2, pady=(3, 0))
numPixelsY.grid(row=4, column=2, pady=(3, 0))

containerInputs.pack(padx=5, pady=5)

containerLaunchers = tk.Frame(window)
btnPixelPainter = tk.Button(containerLaunchers, text="Pixel Painter", command=cPixelPainter)
btnBresenham = tk.Button(containerLaunchers, text="Bresenham", command=cBresenham)
btnSquare = tk.Button(containerLaunchers, text="Square", command=cSquare)
btnTriangle = tk.Button(containerLaunchers, text="Triangle", command=cTriangle)

btnPixelPainter.grid(row=1, column=1)
btnBresenham.grid(row=1, column=2)
btnSquare.grid(row=1, column=3)
btnTriangle.grid(row=2, column=1)

containerLaunchers.pack(padx=5, pady=5)

drawGrid = tk.IntVar()
drawGrid.set(1)

c1 = tk.Checkbutton(window, text='Desenhar Grade', onvalue=1, offvalue=0, variable=drawGrid)
c1.pack()

window.mainloop()