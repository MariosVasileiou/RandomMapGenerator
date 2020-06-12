import matplotlib.pyplot as plt
import numpy as np

from MapGeneration import getMap, Map
from PathFinding import getPath

map1 = getMap(1)

#plt.imshow(map1.map, cmap= plt.cm.Greys);
#plt.show()

print("Finding Path")

path = getPath(np.array(map1.map).tolist(), (map1.start[0][0],map1.start[0][1]), (map1.end[0][0], map1.end[0][1]))

#if not(len(map1.map) == 0):
    #for i in path:
        #map1.map[i[0]][i[1]] = 0.6

print(path.path)

plt.imshow(path.map, cmap=plt.cm.Greys);
plt.show()
