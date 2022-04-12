def reflect(p1: tuple, p2: tuple) -> tuple:
  x1, y1 = p1
  x2, y2 = p2
  dX = x2 - x1
  dY = y2 - y1
  m = dY / dX if dX != 0 else 10

  reflections = {
    'xy': False,
    'x': False,
    'y': False
  }

  if (dX >= dY and dX >= 0 and dY >= 0):
    return (p1, p2, False)
  else:
    if (m > 1 or m < -1):
      x1, y1 = y1, x1
      x2, y2 = y2, x2
      reflections['xy'] = True


    if (x1 > x2):
      x1 *= -1
      x2 *= -1
      reflections['x'] = True


    if (y1 > y2):
      y1 *= -1
      y2 *= -1
      reflections['y'] = True


    return ((x1, y1), (x2, y2), reflections)
    

def unreflect(points: list, refl: dict) -> list:
  newPoints = []

  for point in points:
    x, y = point
    if refl['y']:
      y *= -1

    if refl['x']:
      x *= -1

    if refl['xy']:
      x, y = y, x

    newPoints.append((x, y))

  return newPoints

def bres(p1: tuple , p2: tuple) -> list:
  p1, p2, REFLECTED = reflect(p1, p2)

  x1, y1 = p1
  x2, y2 = p2

  dX = x2 - x1
  dY = y2 - y1
  m = dY / dX
  e = m - (1/2)
  points = [(x1, y1)]

  while (x1 < x2):
    if (e > 0):
      y1 += 1
      e -= 1

    x1 += 1
    e += m
    points.append((x1, y1))

  if REFLECTED:
    points = unreflect(points, REFLECTED)
  
  return points