def bezierPoint(n: int, ctrlPts: list, t: float) -> list:
  pts = []
  for i in range(n+1):
    try:
      pts.append(ctrlPts[i].copy())
    except IndexError:
      pts.append([0, 0])

  for r in range(1, n+1):
    for i in range(i-r+1):
      pts[i][0] = (1-t) * pts[i][0] + t * pts[i+1][0]
      pts[i][1] = (1-t) * pts[i][1] + t * pts[i+1][1]

  return pts[0]

def curve(n: int, ctrlPts: list, numPoints: int) -> list:
  step = 1/numPoints
  points = []

  for i in range(numPoints+1):
    points.append(bezierPoint(n, ctrlPts, step*i))

  for i, point in enumerate(points):
    for j, coord in enumerate(point):
      point[j] = round(coord)

  return points