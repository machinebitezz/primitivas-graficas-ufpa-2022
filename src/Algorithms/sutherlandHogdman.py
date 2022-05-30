def sutherlandHogdman(pointlist: list, xBox: tuple, yBox) -> list:
  newPolygon = []
  xMin, xMax = xBox
  yMin, yMax = yBox

  for i, p1 in enumerate(pointlist):
    p2 = pointlist[(i+1)%len(pointlist)]

    if p1[0] > xMin:
      if p2[0] > xMin:
        newPolygon.append(p2)
      
      else:
        newPolygon.append((xMin, round(((xMin - p1[0]) * (p2[1] - p1[1]) / (p2[0] - p1[0])) + p1[1])))

    else:
      if p2[0] > xMin:
        newPolygon.append((xMin, round(((xMin - p1[0]) * (p2[1] - p1[1]) / (p2[0] - p1[0])) + p1[1])))
        newPolygon.append(p2)

      else: 
        pass

  pointlist = newPolygon.copy()
  newPolygon = []

  for i, p1 in enumerate(pointlist):
    p2 = pointlist[(i+1)%len(pointlist)]

    if p1[0] < xMax:
      if p2[0] < xMax:
        newPolygon.append(p2)
      
      else:
        newPolygon.append((xMax, round(((xMax - p1[0]) * (p2[1] - p1[1]) / (p2[0] - p1[0])) + p1[1])))

    else:
      if p2[0] < xMax:
        newPolygon.append((xMax, round(((xMax - p1[0]) * (p2[1] - p1[1]) / (p2[0] - p1[0])) + p1[1])))
        newPolygon.append(p2)

      else: 
        pass

  pointlist = newPolygon.copy()
  newPolygon = []

  for i, p1 in enumerate(pointlist):
    p2 = pointlist[(i+1)%len(pointlist)]

    if p1[1] > yMin:
      if p2[1] > yMin:
        newPolygon.append(p2)
      
      else:
        newPolygon.append((round(((yMin - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])) + p1[0]), yMin))

    else:
      if p2[1] > yMin:
        newPolygon.append((round(((yMin - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])) + p1[0]), yMin))
        newPolygon.append(p2)

      else: 
        pass

  pointlist = newPolygon.copy()
  newPolygon = []

  for i, p1 in enumerate(pointlist):
    p2 = pointlist[(i+1)%len(pointlist)]

    if p1[1] < yMax:
      if p2[1] < yMax:
        newPolygon.append(p2)
      
      else:
        newPolygon.append((round(((yMax - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])) + p1[0]), yMax))

    else:
      if p2[1] < yMax:
        newPolygon.append((round(((yMax - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])) + p1[0]), yMax))
        newPolygon.append(p2)

      else: 
        pass

  return newPolygon