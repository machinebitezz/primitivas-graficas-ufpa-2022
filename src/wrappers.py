from threading import Thread
from grid import Grid

def cPixelPainter(config: object):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid, animate, animationDelay = config
  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get(),
    'animate': animate.get(),
    'delay': float(animationDelay.get())/1000
  })

  t = Thread(target=draw.launchPixelPainter)
  t.start()

def cBresenham(config: object):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid, animate, animationDelay = config

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get(),
    'animate': animate.get(),
    'delay': float(animationDelay.get())/1000
  })

  t = Thread(target=draw.launchBresenham)
  t.start()

def cSquare(config: object):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid, animate, animationDelay = config

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get(),
    'animate': animate.get(),
    'delay': float(animationDelay.get())/1000
  })

  t = Thread(target=draw.launchSquares)
  t.start()

def cTriangle(config: object):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid, animate, animationDelay = config

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get(),
    'animate': animate.get(),
    'delay': float(animationDelay.get())/1000
  })

  t = Thread(target=draw.launchTriangles)
  t.start()


def cCircle(config: object):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid, animate, animationDelay = config

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get(),
    'animate': animate.get(),
    'delay': float(animationDelay.get())/1000
  })

  t = Thread(target=draw.launchCircles)
  t.start()


def cEllipsis(config: object):
  pixelSizeX, pixelSizeY, numPixelsX, numPixelsY, drawGrid, animate, animationDelay = config

  draw = Grid(config={
    'pixels per rect': (int(pixelSizeX.get()), int(pixelSizeY.get())),
    'size': (int(numPixelsX.get()), int(numPixelsY.get())),
    'grid': drawGrid.get(),
    'animate': animate.get(),
    'delay': float(animationDelay.get())/1000
  })

  t = Thread(target=draw.launchEllipsis)
  t.start()