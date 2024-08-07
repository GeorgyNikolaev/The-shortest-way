import math
import random
import numpy as np


def initMatrix(length, minDistance, maxDistance, inf=1000, pInf=0.9):
    vertex = set()
    distances = np.zeros(shape=(length, length), dtype=float)
    while len(vertex) < length:
        x = round(random.uniform(minDistance, maxDistance), 1)
        y = round(random.uniform(minDistance, maxDistance), 1)
        # y = round(math.sqrt(maxDistance**2 - x**2), 1)
        vertex.add((x, y))
    vertex = list(vertex)

    for i in range(length-1):
        for j in range(i+1, length):
            distance = round(math.sqrt((vertex[i][0] - vertex[j][0])**2 + (vertex[i][1] - vertex[j][1])**2), 2)
            distances[i][j] = distance
            distances[j][i] = distance
            # if j != end and random.random() < pInf:
            if random.random() < pInf:
                distances[i][j] = inf
                distances[j][i] = inf

    return vertex, distances


def pointInint(length, minDistance, maxDistance, inf=1000, pInf=0.3, cntPoint=1):
    vertex = []
    layerCount = (length - 1) // cntPoint
    x_rate = (maxDistance - minDistance) // layerCount
    y_rate = (maxDistance - minDistance) // cntPoint
    distances = np.ones(shape=(length, length), dtype=float) * inf
    vertex.append([0, y_rate])
    for i in range(layerCount):
        for j in range(cntPoint):
            x = (i+1) * x_rate
            y = j * y_rate
            vertex.append([x, y])

    for p in range(cntPoint):
        i = p + 1
        distance = round(math.sqrt((vertex[i][0] - vertex[0][0]) ** 2 + (vertex[i][0] - vertex[0][0]) ** 2), 2)
        distances[i][0] = distance
        distances[0][i] = distance
        if random.random() < pInf:
            distances[i][0] = inf
            distances[0][i] = inf

    for i in range(layerCount-1):
        for p in range(cntPoint):
            j = p + cntPoint * i + 1
            for k in range(j+1, cntPoint * (i+2) + 1):
                distance = round(math.sqrt((vertex[j][0] - vertex[k][0]) ** 2 + (vertex[j][1] - vertex[k][1]) ** 2), 2)
                distances[j][k] = distance
                distances[k][j] = distance
                # if j != end and random.random() < pInf:
                if random.random() < pInf:
                    distances[j][k] = inf
                    distances[k][j] = inf

    return vertex, distances
