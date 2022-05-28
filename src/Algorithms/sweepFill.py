from copy import deepcopy

def sweepFill(points: list) -> list:
  minY = float('inf')
  maxY = float('-inf')
  toPaint = []
  criticals = []

  for i, point in enumerate(points):
    minY = point[1] if point[1] < minY else minY
    maxY = point[1] if point[1] > maxY else maxY

    auxPoint = points[(i+1)%len(points)]

    if point[1] < auxPoint[1]:
      criticals.append({
        'index': i,
        'dir': 1,
        'xInt': point[0],
        'invSlope': float(auxPoint[0]-point[0])/float(auxPoint[1]-point[1] )
      })
    
    auxPoint = points[(i-1+len(points)%len(points))]

    if point[1] < auxPoint[1]:
      criticals.append({
        'index': i,
        'dir': -1,
        'xInt': point[0],
        'invSlope': float(auxPoint[0]-point[0])/float(auxPoint[1]-point[1] )
      })

  activeCriticals = []

  for y in range(minY, maxY+1):
    for criticalP in activeCriticals:
      criticalP['xInt'] += criticalP['invSlope']

    for critical in criticals:
      if points[critical['index']][1] == y:
        activeCriticals.append(deepcopy(critical))

    for point in reversed(activeCriticals):
      critical = deepcopy(point)
      pMax = points[(critical['index']+critical['dir']+len(points))%len(points)]
      if pMax[1] == y:
        activeCriticals.remove(point)

    activeCriticals = sorted(activeCriticals, key=lambda x: x['xInt'])

    for j in range(0, len(activeCriticals)+1, 2):
      if len(activeCriticals) > j:
        xStart = round(activeCriticals[j]['xInt'])
        xEnd = round(activeCriticals[j+1]['xInt'])

        for x in range(xStart, xEnd+1):
          toPaint.append((x, y))

  return toPaint