from Algorithms.bres import bres
from math import log2

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


def cohenSutherland(points: tuple, xBox: tuple, yBox: tuple) -> tuple:
  p1, p2 = (points)

  c1 = getBinary(p1, xBox, yBox)
  c2 = getBinary(p2, xBox, yBox)

  if (c1 | c2) == 0b0000: 
    return bres(p1, p2)

  elif (c1 & c2) != 0b0000:
    return []

  else:
    cOr = c1 | c2
    difBit = log2(cOr&-cOr)+1

    ...


cohenSutherland(((-2, -2), (-2, -2)), (-1, 11), (-1, 11))
