from Algorithms.bres import bres

def getBinary(point: tuple, xBox: tuple, yBox: tuple) -> int:
  rep = 0b0000
  x, y = point
  xMin, xMax = xBox
  yMin, yMax = yBox
  
  if yMax - y < 0:
    rep += 0b1000

  if y - yMin < 0:
    rep += 0b0100

  if xMax - x < 0:
    rep += 0b0010

  if x - xMin < 0:
    rep += 0b0001

  return rep


def msb(c1, c2):
  n = c1 | c2

  if (n == 0):
    return 0

  msb = 0;
  n = int(n / 2)

  while (n > 0):
    n = int(n / 2)
    msb += 1

  return (1 << msb)


def getBit(number, bits):
  p = {
    0b1000: 4,
    0b0100: 3,
    0b0010: 2,
    0b0001: 1
  }
  return (((1 << 1) - 1) & (number >> (p[bits]-1)))


def findIntersection(points: tuple, xBox: tuple, yBox: tuple, bit: int) -> tuple:
  yMin, yMax = yBox
  xMin, xMax = xBox
  p1, p2 = points

  if bit == 0b1000:
    return ((((yMin - p1[1]) * (p2[0] - p1[0])) / (p2[1] - p1[1])) + p1[0], yMax)

  elif bit == 0b0100:
    return ((((yMax - p1[1]) * (p2[0] - p1[0])) / (p2[1] - p1[1])) + p1[0], yMin)

  elif bit == 0b0010:
    return (xMax, (((xMin - p1[0]) * (p2[1] - p1[1])) / (p2[0] - p1[0])) + p1[1])

  elif bit == 0b0001:
    return (xMin, (((xMax - p1[0]) * (p2[1] - p1[1])) / (p2[0] - p1[0])) + p1[1])

def cohenSutherland(points: tuple, xBox: tuple, yBox: tuple) -> tuple:
  p1, p2 = (points)

  c1 = getBinary(p1, xBox, yBox)
  c2 = getBinary(p2, xBox, yBox)

  if (c1 | c2) == 0b0000: 
    return bres(p1, p2)

  elif (c1 & c2) != 0b0000:
    return []

  else:
    difBit = msb(c1, c2)

    intersection = findIntersection(points, xBox, yBox, difBit)

    if getBit(c1, difBit):
      cohenSutherland((p1, intersection), xBox, yBox)

    else: 
      cohenSutherland((intersection, p2), xBox, yBox)