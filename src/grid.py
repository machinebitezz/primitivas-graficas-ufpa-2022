import tkinter as tk
from Algorithms.index import *


class Grid:
    def __init__(self, window, numPixels, tamanhoTela):
        self.numPixels = numPixels
        self.tamanhoTela = tamanhoTela
        self.tamanhoPixel = int(self.tamanhoTela / self.numPixels)
        self.window = window
        self.drawnPoints = []
        self.xBox = [-(numPixels / 2), (numPixels / 2)]
        self.yBox = [-(numPixels / 2), (numPixels / 2)]

        containerCanvas = tk.Frame(self.window)
        self.tela = tk.Canvas(
            containerCanvas, width=self.tamanhoTela, height=self.tamanhoTela
        )

        self.clear()

        self.tela.pack()
        containerCanvas.pack(padx=5, pady=5)

    def drawClip(self):
        xMin, xMax = self.xBox
        yMin, yMax = self.yBox
        xMin = ((round(self.numPixels / 2) + xMin) * self.tamanhoPixel) + 1
        xMax = (
            ((round(self.numPixels / 2) + xMax) * self.tamanhoPixel)
            + self.tamanhoPixel
            - 1
        )
        yMin = ((round(self.numPixels / 2) - yMin) * self.tamanhoPixel) - 1
        yMax = (
            ((round(self.numPixels / 2) - yMax) * self.tamanhoPixel)
            - self.tamanhoPixel
            + 1
        )

        self.tela.create_line(xMin, yMin, xMin, yMax, fill="#FF0000")
        self.tela.create_line(xMin, yMax, xMax, yMax, fill="#FF0000")
        self.tela.create_line(xMax, yMax, xMax, yMin, fill="#FF0000")
        self.tela.create_line(xMax, yMin, xMin, yMin, fill="#FF0000")

    def clear(self):
        self.drawnPoints = []
        self.tela.create_rectangle(
            0, 0, self.tamanhoTela + 1, self.tamanhoTela + 1, fill="#FFFFFF"
        )

        self.drawClip()

        for x in range(0, self.tamanhoTela, self.tamanhoPixel):
            self.tela.create_line(x, 0, x, self.tamanhoTela, fill="#808080")

        for y in range(0, self.tamanhoTela, self.tamanhoPixel):
            self.tela.create_line(0, y, self.tamanhoTela, y, fill="#808080")

    def drawPixel(self, coords, fill="#000000"):
        x, y = coords
        truex = (round(self.numPixels / 2) + x) * self.tamanhoPixel + 1
        truey = (round(self.numPixels / 2) - y - 1) * self.tamanhoPixel + 1

        self.tela.create_rectangle(
            truex,
            truey,
            truex + self.tamanhoPixel - 1,
            truey + self.tamanhoPixel - 1,
            fill=fill,
            width=0,
        )
        self.drawnPoints.append(coords)

    def drawFromList(self, list, color="#000000"):
        self.drawnPoints += list
        for point in list:
            self.drawPixel(point, color)

    def bres(self):
        def run():
            self.clear()
            p1 = int(entryx1.get()), int(entryy1.get())
            p2 = (int(entryx2.get()), int(entryy2.get()))

            self.drawFromList(
                cohenSutherland((p1, p2), tuple(self.xBox), tuple(self.yBox))
            )

            # self.drawFromList()

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

        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.grid(row=5, column=2)

    def cricle(self):
        def run():
            self.clear()
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

        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.grid(row=5, column=2)

    def ellipsis(self):
        def run():
            self.clear()
            center = (int(entryx.get()), int(entryy.get()))
            radii = (int(entryRadius1.get()), int(entryRadius2.get()))

            points = ellipsis(radii, center)
            singleList = []

            for list in points:
                singleList += list

            self.drawFromList(singleList)

        popup = tk.Toplevel(self.window, padx=5, pady=5)
        labelx = tk.Label(popup, text="Coordenada x do centro: ")
        labely = tk.Label(popup, text="Coordenada y do centro: ")
        labelRadius1 = tk.Label(popup, text="Raio X: ")
        labelRadius2 = tk.Label(popup, text="Raio Y: ")

        entryx = tk.Entry(popup)
        entryy = tk.Entry(popup)
        entryRadius1 = tk.Entry(popup)
        entryRadius2 = tk.Entry(popup)

        labelx.grid(row=1, column=1)
        labely.grid(row=2, column=1)
        labelRadius1.grid(row=3, column=1)
        labelRadius2.grid(row=4, column=1)

        entryx.grid(row=1, column=2)
        entryy.grid(row=2, column=2)
        entryRadius1.grid(row=3, column=2)
        entryRadius2.grid(row=4, column=2)

        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.grid(row=5, column=2)

    def polyline(self):
        def run():
            self.clear()
            nonlocal pointList
            if len(pointList) != 0:
                self.polyPoints = pointList.copy()
                points = []
                for index, point in enumerate(pointList):
                    if index == len(pointList) - 1:
                        points.append(
                            cohenSutherland(
                                (point, pointList[0]),
                                tuple(self.xBox),
                                tuple(self.yBox),
                            )
                        )

                    else:
                        points.append(
                            cohenSutherland(
                                (point, pointList[index + 1]),
                                tuple(self.xBox),
                                tuple(self.yBox),
                            )
                        )

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
            self.clear()
            nonlocal pointList
            if len(pointList) != 0:
                n = int(entryDegree.get())
                start = [[int(entryxInit.get()), int(entryyInit.get())]]
                end = [[int(entryxFinal.get()), int(entryyFinal.get())]]
                steps = int(entrySteps.get())
                bezierPoints = curve(n, start + pointList + end, steps)
                points = []

                for index, point in enumerate(bezierPoints):
                    if index < len(bezierPoints) - 1:
                        points.append(
                            cohenSutherland(
                                (tuple(point), tuple(bezierPoints[index + 1])),
                                tuple(self.xBox),
                                tuple(self.yBox),
                            )
                        )

                singleList = []
                for list in points:
                    singleList += tuple(list)

                self.drawFromList(singleList)
                pointList = []
                labelCount.config(text=f"Pontos inseridos: {pointList}")

        def add():
            point = [int(entryxControl.get()), int(entryyControl.get())]
            pointList.append(point)
            labelCount.config(text=f"Pontos inseridos: {pointList}")

        pointList = []
        popup = tk.Toplevel(self.window, padx=5, pady=5)
        labelCount = tk.Label(popup, text="Pontos inseridos: []")
        labelxInit = tk.Label(popup, text="Coordenada x do ponto inicial: ")
        labelyInit = tk.Label(popup, text="Coordenada y do ponto inicial: ")
        labelxControl = tk.Label(popup, text="Coordenada x do ponto de controle: ")
        labelyControl = tk.Label(popup, text="Coordenada y do ponto de controle: ")
        labelxFinal = tk.Label(popup, text="Coordenada x do ponto final: ")
        labelyFinal = tk.Label(popup, text="Coordenada y do ponto final: ")
        labelDegree = tk.Label(popup, text="Grau da curva: ")
        labelSteps = tk.Label(popup, text="Passos: ")

        entryxInit = tk.Entry(popup)
        entryyInit = tk.Entry(popup)
        entryxControl = tk.Entry(popup)
        entryyControl = tk.Entry(popup)
        entryxFinal = tk.Entry(popup)
        entryyFinal = tk.Entry(popup)
        entryDegree = tk.Entry(popup)
        entrySteps = tk.Entry(popup)

        entryDegree.insert(0, "3")
        entrySteps.insert(0, "5")

        labelxInit.grid(row=1, column=1)
        labelyInit.grid(row=2, column=1)
        labelxControl.grid(row=3, column=1)
        labelyControl.grid(row=4, column=1)
        labelxFinal.grid(row=5, column=1)
        labelyFinal.grid(row=6, column=1)
        labelDegree.grid(row=7, column=1)
        labelSteps.grid(row=8, column=1)

        entryxInit.grid(row=1, column=2)
        entryyInit.grid(row=2, column=2)
        entryxControl.grid(row=3, column=2)
        entryyControl.grid(row=4, column=2)
        entryxFinal.grid(row=5, column=2)
        entryyFinal.grid(row=6, column=2)
        entryDegree.grid(row=7, column=2)
        entrySteps.grid(row=8, column=2)

        labelCount.grid(row=9, column=1)

        btnAdd = tk.Button(popup, text="Adicionar", command=add)
        btnAdd.grid(row=11, column=1)
        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.grid(row=11, column=2)

    def sweepFill(self):
        def run():
            self.clear()
            if len(self.polyPoints) != 0:
                points = sweepFill(
                    sutherlandHogdman(self.polyPoints, self.xBox, self.yBox)
                )
                self.drawFromList(points, color="#00FF00")

                points = []
                for index, point in enumerate(self.polyPoints):
                    if index == len(self.polyPoints) - 1:
                        points.append(
                            cohenSutherland(
                                (point, self.polyPoints[0]),
                                tuple(self.xBox),
                                tuple(self.yBox),
                            )
                        )

                    else:
                        points.append(
                            cohenSutherland(
                                (point, self.polyPoints[index + 1]),
                                tuple(self.xBox),
                                tuple(self.yBox),
                            )
                        )

                singleList = []

                for list in points:
                    singleList += list

                self.drawFromList(singleList)

        popup = tk.Toplevel(self.window, padx=5, pady=5)

        label = tk.Label(
            popup, text="Preenche o ultimo poligono desenhado com a função polilinha"
        )
        label.pack()

        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.pack()

    def recursiveFill(self):
        def run(point):
            if not (point in self.drawnPoints):
                self.drawPixel(point, "#0000FF")
                run((point[0] + 1, point[1]))
                run((point[0] - 1, point[1]))
                run((point[0], point[1] + 1))
                run((point[0], point[1] - 1))

        popup = tk.Toplevel(self.window, padx=5, pady=5)
        labelx = tk.Label(popup, text="Coordenada x do ponto: ")
        labely = tk.Label(popup, text="Coordenada y do ponto: ")

        entryx = tk.Entry(popup)
        entryy = tk.Entry(popup)

        labelx.grid(row=1, column=1)
        labely.grid(row=2, column=1)

        entryx.grid(row=1, column=2)
        entryy.grid(row=2, column=2)

        btnDraw = tk.Button(
            popup,
            text="Desenhar",
            command=lambda: run((int(entryx.get()), int(entryy.get()))),
        )
        btnDraw.grid(row=3, column=2)

    def adjustClippingBox(self):
        def run():
            self.clear()
            self.xBox = [int(entryxmin.get()), int(entryxmax.get())]
            self.yBox = [int(entryymin.get()), int(entryymax.get())]

            self.clear()

        popup = tk.Toplevel(self.window, padx=5, pady=5)
        labelxmin = tk.Label(popup, text="Coordenada x minima: ")
        labelxmax = tk.Label(popup, text="Coordenada x máxima: ")
        labelymin = tk.Label(popup, text="Coordenada y minima: ")
        labelymax = tk.Label(popup, text="Coordenada y máxima: ")

        entryxmin = tk.Entry(popup)
        entryxmax = tk.Entry(popup)
        entryymin = tk.Entry(popup)
        entryymax = tk.Entry(popup)

        labelxmin.grid(row=1, column=1)
        labelxmax.grid(row=2, column=1)
        labelymin.grid(row=3, column=1)
        labelymax.grid(row=4, column=1)

        entryxmin.grid(row=1, column=2)
        entryxmax.grid(row=2, column=2)
        entryymin.grid(row=3, column=2)
        entryymax.grid(row=4, column=2)

        btnDraw = tk.Button(popup, text="Ajustar", command=run)
        btnDraw.grid(row=5, column=2)

    def translate(self):
        def run():
            self.clear()
            factors = int(entryx.get()), int(entryy.get())

            pointList = translate(self.polyPoints, factors)

            points = []

            for index, point in enumerate(pointList):
                if index == len(pointList) - 1:
                    points.append(
                        cohenSutherland(
                            (point, pointList[0]), tuple(self.xBox), tuple(self.yBox)
                        )
                    )

                else:
                    points.append(
                        cohenSutherland(
                            (point, pointList[index + 1]),
                            tuple(self.xBox),
                            tuple(self.yBox),
                        )
                    )

            singleList = []

            for list in points:
                singleList += list

            self.polyPoints = singleList

            self.drawFromList(singleList)

        popup = tk.Toplevel(self.window, padx=5, pady=5)
        labelx = tk.Label(popup, text="Fator de translação em x: ")
        labely = tk.Label(popup, text="Fator de translação em y: ")

        entryx = tk.Entry(popup)
        entryy = tk.Entry(popup)

        labelx.grid(row=1, column=1)
        labely.grid(row=2, column=1)

        entryx.grid(row=1, column=2)
        entryy.grid(row=2, column=2)

        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.grid(row=3, column=2)

    def scale(self):
        def run():
            self.clear()
            factors = float(entryx.get()), float(entryy.get())

            pointList = scale(self.polyPoints, factors)

            points = []

            for index, point in enumerate(pointList):
                if index == len(pointList) - 1:
                    points.append(
                        cohenSutherland(
                            (point, pointList[0]), tuple(self.xBox), tuple(self.yBox)
                        )
                    )

                else:
                    points.append(
                        cohenSutherland(
                            (point, pointList[index + 1]),
                            tuple(self.xBox),
                            tuple(self.yBox),
                        )
                    )

            singleList = []

            for list in points:
                singleList += list

            self.polyPoints = singleList

            self.drawFromList(singleList)

        popup = tk.Toplevel(self.window, padx=5, pady=5)
        labelx = tk.Label(popup, text="Fator de escala em x: ")
        labely = tk.Label(popup, text="Fator de escala em y: ")

        entryx = tk.Entry(popup)
        entryy = tk.Entry(popup)

        labelx.grid(row=1, column=1)
        labely.grid(row=2, column=1)

        entryx.grid(row=1, column=2)
        entryy.grid(row=2, column=2)

        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.grid(row=3, column=2)

    def rotate(self):
        def run():
            self.clear()
            pivot = int(entryx.get()), int(entryy.get())
            angle = float(entrydeg.get())

            pointList = rotate(self.polyPoints, angle, pivot)

            points = []

            for index, point in enumerate(pointList):
                if index == len(pointList) - 1:
                    points.append(
                        cohenSutherland(
                            (point, pointList[0]), tuple(self.xBox), tuple(self.yBox)
                        )
                    )

                else:
                    points.append(
                        cohenSutherland(
                            (point, pointList[index + 1]),
                            tuple(self.xBox),
                            tuple(self.yBox),
                        )
                    )

            singleList = []

            for list in points:
                singleList += list

            self.polyPoints = singleList

            self.drawFromList(singleList)

        popup = tk.Toplevel(self.window, padx=5, pady=5)
        labeldeg = tk.Label(popup, text="Graus: ")
        labelx = tk.Label(popup, text="Coordenada x do pivô: ")
        labely = tk.Label(popup, text="Coordenada y do pivô: ")

        entrydeg = tk.Entry(popup)
        entryx = tk.Entry(popup)
        entryy = tk.Entry(popup)

        labeldeg.grid(row=1, column=1)
        labelx.grid(row=2, column=1)
        labely.grid(row=3, column=1)

        entrydeg.grid(row=1, column=2)
        entryx.grid(row=2, column=2)
        entryy.grid(row=3, column=2)

        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.grid(row=4, column=2)

    def projection(self):
        pointList = []
        projection_type = tk.StringVar(value="Ortogonal")
        popup = tk.Toplevel(self.window, padx=5, pady=5)
        labelCount = tk.Label(popup, text="Pontos inseridos: []")
        labelx = tk.Label(popup, text="Coordenada x do ponto: ")
        labely = tk.Label(popup, text="Coordenada y do ponto: ")
        labelz = tk.Label(popup, text="Coordenada z do ponto: ")
        label_recuo = tk.Label(popup, text="Recuo: ")
        label_dist = tk.Label(popup, text="Distância: ")
        label_ddmenu = tk.Label(popup, text="Tipo de projeção: ")

        entryx = tk.Entry(popup)
        entryy = tk.Entry(popup)
        entryz = tk.Entry(popup)
        entry_recuo = tk.Entry(popup)
        entry_dist = tk.Entry(popup)
        entry_ddmenu = tk.OptionMenu(popup, projection_type, "Ortogonal", "Pespectiva")

        labelx.grid(row=1, column=1)
        labely.grid(row=2, column=1)
        labelz.grid(row=3, column=1)
        label_recuo.grid(row=4, column=1)
        label_dist.grid(row=5, column=1)
        label_ddmenu.grid(row=6, column=1)

        entryx.grid(row=1, column=2)
        entryy.grid(row=2, column=2)
        entryz.grid(row=3, column=2)
        entry_recuo.grid(row=4, column=2)
        entry_dist.grid(row=5, column=2)
        entry_ddmenu.grid(row=6, column=2)

        labelCount.grid(row=7, column=1)

        def run():
            self.clear()
            nonlocal pointList
            if len(pointList) != 0:
                obj = Projection(pointList, int(entry_recuo.get()))
                if projection_type.get() == "Ortogonal":
                    obj.ortogonal()
                else:
                    obj.perspectiva(int(entry_dist.get()))
                self.drawFromList(obj.saida)
                pointList = []
                labelCount.config(text=f"Pontos inseridos: {pointList}")

        def add():
            nonlocal pointList
            point = [int(entryx.get()), int(entryy.get()), int(entryz.get())]
            pointList.append(point)
            labelCount.config(text=f"Pontos inseridos: {pointList}")

        def rem():
            nonlocal pointList
            pointList = pointList[:-1]
            labelCount.config(text=f"Pontos inseridos: {pointList}")

        btnAdd = tk.Button(popup, text="Adicionar", command=add)
        btnAdd.grid(row=8, column=1)
        btnRem = tk.Button(popup, text="Remover", command=rem)
        btnRem.grid(row=8, column=2)
        btnDraw = tk.Button(popup, text="Desenhar", command=run)
        btnDraw.grid(row=8, column=3)
