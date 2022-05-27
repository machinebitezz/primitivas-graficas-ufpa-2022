def sutherlandHogdman(pointlist, xBox, yBox, side = 0):
  newPolygon = []
  xMin, xMax = xBox
  yMin, yMax = yBox

  temp = [xMin, yMin, xMax, yMax]

  comparator = temp[side]

  i1 = 0 if side // 2 == 0 else 1
  i2 = 0 if side // 2 != 0 else 1

  for i, p1 in enumerate(pointlist):
    p2 = pointlist[(i+1)%len(pointlist)]

    if p1[i1] > comparator:
      if p2[i1] > comparator:
        newPolygon.append(p2)
      
      else:
        newPolygon.append((comparator, round(((comparator - p1[i1]) * (p2[i2] - p1[i2]) / (p2[i1] - p1[i1])) + p1[i2])))

    else:
      if p2[i1] > comparator:
        newPolygon.append((comparator, round(((comparator - p1[i1]) * (p2[i2] - p1[i2]) / (p2[i1] - p1[i1])) + p1[i2])))
        newPolygon.append(p2)

      else: 
        pass

  if side != 3:
    return sutherlandHogdman(newPolygon, xBox, yBox, side=side+1)
  else:
    return newPolygon