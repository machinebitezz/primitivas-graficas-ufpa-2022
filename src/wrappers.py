from threading import Thread
from grid import Grid

def cPixelPainter(config):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid = config
  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get()
  })

  t = Thread(target=draw.launchPixelPainter)
  t.start()

def cBresenham(config):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid = config

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get()
  })

  t = Thread(target=draw.launchBresenham)
  t.start()

def cSquare(config):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid = config

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get()
  })

  t = Thread(target=draw.launchSquares)
  t.start()

def cTriangle(config):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid = config

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get()
  })

  t = Thread(target=draw.launchTriangles)
  t.start()