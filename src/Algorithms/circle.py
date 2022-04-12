def getPoints(point: tuple, center: tuple) -> list:
  x, y = point
  offsetX, offsetY = center
  points = []

  for factor in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    points.append((x*factor[0]+offsetX, y*factor[1]+offsetY))
    points.append((y*factor[0]+offsetX, x*factor[1]+offsetY))

  return points

def circle(center: tuple, radius: int) -> list:
  x = 0
  y = radius
  e = -radius
  points = []

  points.append(getPoints((x, y), center))
  while x <= y:
    e += (2*x) + 1
    x += 1
    if (e >= 0):
      e += 2 - (2*y)
      y -= 1

    points.append(getPoints((x, y), center))

  return points
