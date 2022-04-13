def getPoints(points: tuple, center: tuple) -> list:
  x, y = points
  offX, offY = center
  return [
    (x+offX, y+offY),
    (-x+offX, y+offY),
    (-x+offX, -y+offY),
    (x+offX, -y+offY)
  ]


def ellipsis(radii: tuple, center: tuple) -> list:
  a, b = radii
  x = 0
  y = b
  asq = a**2
  bsq = b**2
  points = []

  dx = 2*bsq*x
  dy = 2*asq*y

  e = -(b*asq) + asq**(1/4)
  while (dx < dy):
    points.append(getPoints((x, y), center))

    x += 1
    e += dx + bsq
    dx += 2*bsq

    if e > 0:
      y -= 1
      e += asq - dy
      dy -= 2*asq

  e = bsq*((x+(1/2))**2) + asq*(y**2) - asq*bsq

  while (y >= 0):
    points.append(getPoints((x, y), center))

    y -= 1
    e += asq - dy
    dy -= 2*asq

    if e < 0:
      x += 1
      e += dx + bsq
      dx += 2*bsq

  return points