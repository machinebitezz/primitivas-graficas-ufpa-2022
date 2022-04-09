import pygame
from math import floor
from bres import bres
from sys import exit

class Grid:
  def __init__(self, config: object):
    self.PIXELSIZE = config['pixels per rect']
    self.SIZE = config['size']
    self.shouldDrawGrid = config['grid']
    self.WHITE = (255, 255, 255)
    self.BLACK = (0, 0, 0)
    self.BLUE = (0, 0, 255)
    self.hLines = []
    self.vLines = []
    self.screen = pygame.display.set_mode((self.SIZE[0]*self.PIXELSIZE[0], self.SIZE[1]*self.PIXELSIZE[1]))
    pygame.display.set_caption('Grade')

    for hLine in range(1, self.SIZE[0]):
      start = (hLine*self.PIXELSIZE[0], 0)
      end = (hLine*self.PIXELSIZE[0], self.PIXELSIZE[1]*self.SIZE[1])
      self.hLines.append((start, end))

    for vLine in range(1, self.SIZE[1]):
      start = (0, vLine*self.PIXELSIZE[1])
      end = (self.PIXELSIZE[0]*self.SIZE[0], vLine*self.PIXELSIZE[1])
      self.vLines.append((start, end))

  
  def drawPixel(self, position, color):
    pos = (position[0]*self.PIXELSIZE[0], position[1]*self.PIXELSIZE[1])
    pygame.draw.rect(self.screen, color, pygame.Rect(pos, self.PIXELSIZE))


  def drawGrid(self):
    if self.shouldDrawGrid:
      for hLine in self.hLines:
        start, end = hLine
        pygame.draw.line(self.screen, (80, 0, 0), start, end)

      for vLine in self.vLines:
        start, end = vLine
        pygame.draw.line(self.screen, (80, 0, 0), start, end)


  def launchPixelPainter(self):
    pygame.init()
    self.screen.fill(self.BLACK)

    running = True
    clock=pygame.time.Clock()

    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          
        if event.type == pygame.MOUSEBUTTONUP:
          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()
  
    pygame.quit()
    exit()

  def launchBresenham(self):
    selected = []
    running = True
    clock = pygame.time.Clock()

    self.screen.fill(self.BLACK)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.display.quit()
          exit()

        if event.type == pygame.MOUSEBUTTONUP:
          if len(selected) == 0:
            self.screen.fill(self.BLACK)

          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)
          selected.append(coords)

          if len(selected) == 2:
            points = bres(selected[0], selected[1])
            start = selected[0]
            end = selected[1]
            selected = []
            self.screen.fill(self.BLACK)
            for point in points:
              self.drawPixel(point, self.WHITE)

              pygame.draw.line(self.screen, self.BLUE, (floor(start[0]*self.PIXELSIZE[0]+(self.PIXELSIZE[0]/2)), floor(start[1]*self.PIXELSIZE[1]+(self.PIXELSIZE[1]/2))), ((floor(end[0]*self.PIXELSIZE[0]+(self.PIXELSIZE[0]/2)), floor(end[1]*self.PIXELSIZE[1]+(self.PIXELSIZE[1]/2)))))

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()  
  
    pygame.display.quit()
    exit()

  
  def launchSquares(self):
    selected = []
    running = True
    clock = pygame.time.Clock()

    self.screen.fill(self.BLACK)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.display.quit()
          exit()

        if event.type == pygame.MOUSEBUTTONUP:
          if len(selected) == 0:
            self.screen.fill(self.BLACK)

          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)
          selected.append(coords)

          if len(selected) == 2:
            x1, y1 = selected[0]
            x2, y2 = selected[1]

            edges = [
              bres((x1, y1), (x2, y1)),
              bres((x2, y1), (x2, y2)),
              bres((x2, y2), (x1, y2)),
              bres((x1, y2), (x1, y1)),
            ]

            selected = []
            self.screen.fill(self.BLACK)
            for edge in edges:
              for point in edge:
                self.drawPixel(point, self.WHITE)

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()  
  
    pygame.display.quit()
    exit()

  
  def launchTriangles(self):
    selected = []
    running = True
    clock = pygame.time.Clock()

    self.screen.fill(self.BLACK)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.display.quit()
          exit()

        if event.type == pygame.MOUSEBUTTONUP:
          if len(selected) == 0:
            self.screen.fill(self.BLACK)

          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)
          selected.append(coords)

          if len(selected) == 3:
            x1, y1 = selected[0]
            x2, y2 = selected[1]
            x3, y3 = selected[2]

            edges = [
              bres((x1, y1), (x2, y2)),
              bres((x2, y2), (x3, y3)),
              bres((x3, y3), (x1, y1))
            ]

            selected = []
            self.screen.fill(self.BLACK)
            for edge in edges:
              for point in edge:
                self.drawPixel(point, self.WHITE)

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()  
  
    pygame.display.quit()
    exit()