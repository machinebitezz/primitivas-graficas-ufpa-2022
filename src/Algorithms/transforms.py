import numpy as np
from math import cos, sin, radians

def toTuple(matrix: np.matrix) -> tuple:
  return (matrix[0, 0], matrix[0, 1]) 

def translate(points: list, factors: tuple) -> list:
  newPoints = []

  for point in points:
    x, y = point
    Tx, Ty = factors

    newPoints.append((x+Tx, y+Ty))

  return newPoints

def scale(points: list, factors: tuple) -> list:
  newPoints = []

  for point in points:
    x, y = point
    Ex, Ey = factors

    newPoint = np.matrix(f'{x} {y}') * np.matrix(f'{Ex} 0; 0 {Ey}')

    newPoints.append(toTuple(newPoint))

  return newPoints

def rotate(points: list, angle: float, pivot: tuple) -> list:
  newPoints = []

  for point in points:
    x, y = point
    px, py = pivot

    npx, npy = toTuple(np.matrix(f'{x-px} {y-py}') * np.matrix(f'{cos(radians(angle))} {-sin(radians(angle))}; {sin(radians(angle))} {cos(radians(angle))}'))

    newPoints.append((round(npx+px), round(npy+py)))

  return newPoints