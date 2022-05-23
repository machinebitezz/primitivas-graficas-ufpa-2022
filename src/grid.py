import tkinter as tk
from Algorithms.index import *

class Grid:
  def __init__(self, window, numPixels, tamanhoTela):
    self.numPixels = numPixels
    self.tamanhoTela = tamanhoTela
    self.tamanhoPixel = int(self.tamanhoTela / self.numPixels)
    self.window = window
    self.drawnPoints = []

    containerCanvas = tk.Frame(self.window)
    self.tela = tk.Canvas(containerCanvas, width=self.tamanhoTela, height=self.tamanhoTela)

    self.clear()

    self.tela.pack()
    containerCanvas.pack(padx=5, pady=5)

  
  def clear(self):
    self.drawnPoints = []
    self.tela.create_rectangle(0, 0, self.tamanhoTela+1, self.tamanhoTela+1, fill="#FFFFFF")

    for x in range(0, self.tamanhoTela, self.tamanhoPixel):
      self.tela.create_line(x, 0, x, self.tamanhoTela, fill="#808080")

    for y in range(0, self.tamanhoTela, self.tamanhoPixel):
      self.tela.create_line(0, y, self.tamanhoTela, y, fill="#808080")


  def drawPixel(self, coords):
    x, y = coords
    truex = (x)*self.tamanhoPixel + 1
    truey = (self.numPixels-y-1)*self.tamanhoPixel + 1

    self.tela.create_rectangle(truex, truey, truex+self.tamanhoPixel-1, truey+self.tamanhoPixel-1, fill="#000000", width=0)


  def drawFromList(self, list):
    self.drawnPoints += list
    for point in list:
      self.drawPixel(point)


  def bres(self):
    def run():
      p1 = int(entryx1.get()), int(entryy1.get())
      p2 = (int(entryx2.get()), int(entryy2.get()))

      self.drawFromList(bres(p1, p2))

    popup = tk.Toplevel(self.window, padx=5, pady=5)
    labelx1 = tk.Label(popup, text="Coordenada x do ponto 1: ")
    labely1 = tk.Label(popup, text="Coordenada y do ponto 1: ")
    labelx2 = tk.Label(popup, text="Coordenada x do ponto 2: ")
    labely2 = tk.Label(popup, text="Coordenada y do ponto 2: ")

    entryx1 = tk.Entry(popup)
    entryy1 = tk.Entry(popup)
    entryx2 = tk.Entry(popup)
    entryy2 = tk.Entry(popup)
    
    labelx1.grid(row=1, column=1)
    labely1.grid(row=2, column=1)
    labelx2.grid(row=3, column=1)
    labely2.grid(row=4, column=1)

    entryx1.grid(row=1, column=2)
    entryy1.grid(row=2, column=2)
    entryx2.grid(row=3, column=2)
    entryy2.grid(row=4, column=2)

    entryx1.insert(0, '0')
    entryy1.insert(0, '0')
    entryx2.insert(0, '0')
    entryy2.insert(0, '0')
    
    btnDraw = tk.Button(popup, text="Desenhar", command=run)
    btnDraw.grid(row=5, column=2)


  def cricle(self):
    def run():
      center = (int(entryx.get()), int(entryy.get()))
      radius = int(entryRadius.get())

      self.drawFromList(circle(center, radius))

    popup = tk.Toplevel(self.window, padx=5, pady=5)
    labelx = tk.Label(popup, text="Coordenada x do centro: ")
    labely = tk.Label(popup, text="Coordenada y do centro: ")
    labelRadius = tk.Label(popup, text="Raio: ")

    entryx = tk.Entry(popup)
    entryy = tk.Entry(popup)
    entryRadius = tk.Entry(popup)
    
    labelx.grid(row=1, column=1)
    labely.grid(row=2, column=1)
    labelRadius.grid(row=3, column=1)

    entryx.grid(row=1, column=2)
    entryy.grid(row=2, column=2)
    entryRadius.grid(row=3, column=2)

    entryx.insert(0, '0')
    entryy.insert(0, '0')
    entryRadius.insert(0, '5')

    btnDraw = tk.Button(popup, text="Desenhar", command=run)
    btnDraw.grid(row=5, column=2)


  def polyline(self):
    def run():
      nonlocal pointList
      if len(pointList) != 0:
        points = []
        for index, point in enumerate(pointList):
          if (index == len(pointList)-1):
            points.append(bres(point, pointList[0]))

          else:
            points.append(bres(point, pointList[index+1]))

        singleList = []
        for list in points:
          singleList += list

        self.drawFromList(singleList)
        pointList = []
        labelCount.config(text=f"Pontos inseridos: {pointList}")

    def add():
      point = (int(entryx.get()), int(entryy.get()))
      pointList.append(point)
      labelCount.config(text=f"Pontos inseridos: {pointList}")

    pointList = []
    popup = tk.Toplevel(self.window, padx=5, pady=5)
    labelCount = tk.Label(popup, text="Pontos inseridos: []")
    labelx = tk.Label(popup, text="Coordenada x do ponto: ")
    labely = tk.Label(popup, text="Coordenada y do ponto: ")

    entryx = tk.Entry(popup)
    entryy = tk.Entry(popup)
    entryx.insert(0, '0')
    entryy.insert(0, '0')

    labelx.grid(row=1, column=1)
    labely.grid(row=2, column=1)

    entryx.grid(row=1, column=2)
    entryy.grid(row=2, column=2)

    labelCount.grid(row=3, column=1)

    btnAdd = tk.Button(popup, text="Adicionar", command=add)
    btnAdd.grid(row=4, column=1)
    btnDraw = tk.Button(popup, text="Desenhar", command=run)
    btnDraw.grid(row=4, column=2)

  def curve(self):
    def run():
      nonlocal pointList
      if len(pointList) != 0:
        n = int(entryDegree.get())
        steps = int(entrySteps.get())
        bezierPoints = curve(n, pointList, steps)
        points = []

        print(bezierPoints)
        
        for index, point in enumerate(bezierPoints):
          if (index < len(bezierPoints)-1):
            points.append(bres(tuple(point), tuple(bezierPoints[index+1])))

        singleList = []
        for list in points:
          singleList += tuple(list)

        self.drawFromList(singleList)
        pointList = []
        labelCount.config(text=f"Pontos inseridos: {pointList}")

    def add():
      point = [int(entryx.get()), int(entryy.get())]
      pointList.append(point)
      labelCount.config(text=f"Pontos inseridos: {pointList}")

    pointList = []
    popup = tk.Toplevel(self.window, padx=5, pady=5)
    labelCount = tk.Label(popup, text="Pontos inseridos: []")
    labelx = tk.Label(popup, text="Coordenada x do ponto: ")
    labely = tk.Label(popup, text="Coordenada y do ponto: ")
    labelDegree = tk.Label(popup, text="Grau da curva: ")
    labelSteps = tk.Label(popup, text="Passos: ")

    entryx = tk.Entry(popup)
    entryy = tk.Entry(popup)
    entryDegree = tk.Entry(popup)
    entrySteps = tk.Entry(popup)
    entryx.insert(0, '0')
    entryy.insert(0, '0')
    entryDegree.insert(0, '3')
    entrySteps.insert(0, '5')

    labelx.grid(row=1, column=1)
    labely.grid(row=2, column=1)
    labelDegree.grid(row=3, column=1)
    labelSteps.grid(row=4, column=1)

    entryx.grid(row=1, column=2)
    entryy.grid(row=2, column=2)
    entryDegree.grid(row=3, column=2)
    entrySteps.grid(row=4, column=2)

    labelCount.grid(row=5, column=1)

    btnAdd = tk.Button(popup, text="Adicionar", command=add)
    btnAdd.grid(row=6, column=1)
    btnDraw = tk.Button(popup, text="Desenhar", command=run)
    btnDraw.grid(row=6, column=2)