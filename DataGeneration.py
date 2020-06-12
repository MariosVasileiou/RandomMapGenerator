from MapGeneration import getMap, Map
from PathFinding import getPath
import numpy as np
import matplotlib.pyplot as plt

# # Define parameters

# number of maps to be generated
n_maps = 1000

# name of the maps
name = 'map_'

# number of start-end point for each map
n_points = 2

for i in range(0, n_maps):

    map1 = getMap(n_points) # (map, startL, endL)

    for i in range(0, n_points):
        path = getPath(np.array(map1.map).tolist(), (map1.start[i][0], map1.start[i][1]), (map1.end[i][0], map1.end[i][1])) # map, path, start, end

        print(path.path)

        plt.imshow(path.map, cmap=plt.cm.Greys);
        plt.show()

        # TODO save the path



#with open('Data/test', 'w') as f:
#    f.write()
